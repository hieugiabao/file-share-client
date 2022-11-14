

from core.tftp.tftp import TFTPException


class TFTPError(TFTPException):
    """Exception meaning that a TFTP ERROR packet received."""

    def __init__(self, error_id: int, message: str) -> None:
        super(TFTPError, self).__init__(
            'Error {}: {}'.format(error_id, message))
        self.error_id = error_id
        self.message = message
