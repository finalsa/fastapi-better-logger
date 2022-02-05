from logging import Logger, _Level


class DefaultLogger(Logger):
    """
    """

    def __init__(self, name: str, level: _Level = ...) -> None:
        super().__init__(name, level)
