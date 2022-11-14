from typing import Tuple, NewType

BLOCK_SIZE = 512
BUF_SIZE = 65536
TIMEOUT = 0.5
MAX_RETRIES = 10


class TFTPOpcodes:
    """Class containing all the opcodes used in TFTP."""
    RRQ = b'\x00\x01'
    WRQ = b'\x00\x02'
    DATA = b'\x00\x03'
    ACK = b'\x00\x04'
    ERROR = b'\x00\x05'
    OACK = b'\x00\x06'


class TFTPOptions:
    # RFC 2348
    BLKSIZE = b'blksize'
    # RFC 7440
    WINDOWSIZE = b'windowsize'


Address = NewType('Address', tuple)
Packet = NewType('Packet', Tuple[bytes, Address])
