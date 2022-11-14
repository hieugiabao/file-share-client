import socket
from typing import Dict
from .header import *
from .tftp import TFTP


class TFTPClient(TFTP):
    """
    Class that handles communication with a TFTP server and allows to download
    and upload files.
    """

    def __init__(self, host: str, port: int,
                 block_size: int = BLOCK_SIZE, window_size: int = 1) -> None:
        """
        :param host: hostname/IP of the server to connect to
        :param port: UDP port of the server to connect to
        :param block_size: block size, as in RFC 2347
        :param window_size: window size, as in RFC 7440
        """
        super(TFTPClient, self).__init__(
            socket.socket(socket.AF_INET, socket.SOCK_DGRAM),
            Address((host, port)), block_size, window_size)
        self.__options = self._format_options(self.__create_options_dict())

    def __create_options_dict(self) -> Dict[bytes, bytes]:
        """Create options dictionary to feed into TFTP._format_options method.

        The method omits the options that have default value.

        :return: generated dictionary
        """
        d = {}

        if self._block_size != BLOCK_SIZE:
            d[TFTPOptions.BLKSIZE] = str(self._block_size).encode('utf-8')
        if self._window_size != 1:
            d[TFTPOptions.WINDOWSIZE] = str(self._window_size).encode('utf-8')

        return d

    def __send_rq(self, opcode: bytes, file_name: str,
                  mode: str = 'octet') -> None:
        """Send an RRQ/WRQ packet.

        :param opcode: opcode to send (see TFTPOpcodes.RRQ and TFTPOpcodes.WRQ)
        :param file_name: name of the file requested
        :param mode: requested file transfer mode ('octet' by default)
        """
        self._send(b'%s%s\x00%s\x00%s' % (
            opcode, bytes(file_name, 'utf-8'), bytes(mode, 'utf-8'),
            self.__options))

    def __send_rrq(self, file_name: str, mode: str = 'octet') -> None:
        """Send an RRQ packet.

        :param file_name: name of the file requested
        :param mode: requested file transfer mode ('octet' by default)
        """
        self.__send_rq(TFTPOpcodes.RRQ, file_name, mode)

    def __send_wrq(self, file_name: str, mode: str = 'octet') -> None:
        """Send a WRQ packet.

        :param file_name: name of the uploaded file
        :param mode: requested file transfer mode ('octet' by default)
        """
        self.__send_rq(TFTPOpcodes.WRQ, file_name, mode)

    def get_file(self, file_name: str) -> bytes:
        """Retrieve a file from the connected server.

        :param file_name: name of the file to download
        :return: file data returned by the server
        """
        self.__send_rrq(file_name)
        # get new socket from server
        addr, port = self._recv_ack(handle_timeout=False)
        self._send_ack(0, (addr[0], port))
        self._check_addr = False
        self.__recv_first_rrq_packet()
        return self._recv_file()

    def __recv_first_rrq_packet(self):
        """Receive and respond (in case of OACK) to the first packet after
        sending RRQ - either OACK or DATA.
        """
        addr, opcode, data = self._recv_packet_mul(
            [TFTPOpcodes.OACK, TFTPOpcodes.DATA], 0)
        if opcode == TFTPOpcodes.DATA:
            self._set_packet_buffer(opcode + data, addr)
        else:
            self.__process_oack(data)
            self._send_ack(b'\x00\x00')

    def put_file(self, file_name: str, data: bytes) -> None:
        """Upload a file to the connected server.

        :param file_name: name of the uploaded file
        :param data: data to be sent
        """
        self.__send_wrq(file_name)
        addr, port = self._recv_ack(handle_timeout=False)
        self._send_ack(0, (addr[0], port))
        self._check_addr = False
        self.__recv_first_wrq_packet()
        self._send_file(data)

    def __recv_first_wrq_packet(self):
        """Receive the first packet after sending WRQ - either OACK or ACK."""
        addr, opcode, data = self._recv_packet_mul(
            [TFTPOpcodes.OACK, TFTPOpcodes.ACK], 0)
        if opcode == TFTPOpcodes.OACK:
            self.__process_oack(data)

    def __process_oack(self, data: bytes):
        """Process and apply the options from the OACK packet.

        :param data: raw data got from the packet
        """
        self._process_options(data.split(b'\0'))
