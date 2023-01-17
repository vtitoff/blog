import abc
from app.constants import USERS_PER_PAGE

class BasicQueryValidator(abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def get_int(value):
        pass


class LimitQueryValidator(BasicQueryValidator):
    def get_int(value):
        try:
            int_value = int(value)
        except ValueError:
            int_value = USERS_PER_PAGE
        return int_value


class PageQueryValidator(BasicQueryValidator):
    def get_int(value):
        try:
            int_value = int(value)
        except ValueError:
            int_value = 0
        return int_value