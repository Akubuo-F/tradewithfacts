from abc import ABC


class Logger(ABC):

    @staticmethod
    def log(message: str) -> None:
        ...