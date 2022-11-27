
def checksum(len_: int, payload: bytes) -> bytes:
    """Add checksum to the packet."""
    checksum = 0
    for i in range(0, len_, 2):
        checksum += ((payload[i] << 8) & 0xFF00)
        if i + 1 < len_:
            checksum += (payload[i + 1] & 0xFF)
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    checksum = ~checksum & 0xFFFF
    return checksum.to_bytes(2, byteorder='big')


if __name__ == '__main__':
    a = 'abc'
    byte = a.encode('utf-8')
    print(byte + checksum(3, byte))
    print((checksum(5, checksum(3, byte) + byte)))
