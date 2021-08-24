from .const import VALID_VALUES


class StatusError(ValueError):
    def __init__(self, msg: str = None, value: str = None) -> None:
        message = (
            f'Valid values {VALID_VALUES}, given \'{value.lower()}\''
        )
        msg = msg or message
        super().__init__(msg)
