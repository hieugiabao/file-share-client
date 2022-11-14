from core.tftp.tftp import TFTPException


class TFTPTerminatedError(TFTPException):
    """Exception meaning that the TFTP connection was terminated for the
    reason passed in `error_id` and `message` arguments."""

    def __init__(self, error_id: int, error_message: str,
                 message: str) -> None:
        super(TFTPTerminatedError, self).__init__(
            'Terminated with error {}: {}; cause: {}'.format(
                error_id, error_message, message))
        self.error_id = error_id
        self.error_message = message
        self.message = message