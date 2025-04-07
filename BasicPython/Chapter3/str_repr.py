#!/usr/bin/env python3


def auto_repr(cls):
    def __repr__(self):
        cls_module = self.__class__.__module__
        cls_name = self.__class__.__name__
        members = [ f"{key}={repr(value)}" for key, value in self.__dict__.items()]
        return f"{cls_module}.{cls_name}({', '.join(members)})"
    cls.__repr__ = __repr__
    return cls


@auto_repr
class ConfigObject:
    def __init__(self, count: int = 1, debug: bool = False) -> None:
        self.count: int = count
        self.debug: bool = debug
        self.message: str = "message"
        self.__private_member: str = "private member"

    def __str__(self):
        return ', '.join([ f"{key}={repr(value)}" for key , value in self.__dict__.items()])


def __Test():
    config: ConfigObject = ConfigObject()
    print(repr(config))
    print(str(config))
    return


if __name__ == "__main__":
    __Test()
