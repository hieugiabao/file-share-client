

class TFTPErrorCodes:
    """Class containing all the error codes and their messages used in TFTP."""
    UNKNOWN = 0
    FILE_NOT_FOUND = 1
    ACCESS_VIOLATION = 2
    DISK_FULL = 3
    ILLEGAL_OPERATION = 4
    UNKNOWN_TRANSFER_ID = 5
    FILE_EXISTS = 6
    NO_SUCH_USER = 7
    INVALID_OPTIONS = 8

    __MESSAGES = {
        UNKNOWN: '',
        FILE_NOT_FOUND: 'File not found',
        ACCESS_VIOLATION: 'Access violation',
        DISK_FULL: 'Disk full or allocation exceeded',
        ILLEGAL_OPERATION: 'Illegal TFTP operation',
        UNKNOWN_TRANSFER_ID: 'Unknown transfer ID',
        FILE_EXISTS: 'File already exists',
        NO_SUCH_USER: 'No such user',
        INVALID_OPTIONS: 'Invalid options specified',
    }

    @classmethod
    def get_message(cls, error_code: int) -> str:
        """Return an error message for given error code.

        :param error_code: error code to get the message for
        :return: error message
        """
        return cls.__MESSAGES[error_code]

