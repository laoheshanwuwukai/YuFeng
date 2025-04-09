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


def BaseStrSplite():
    message = "cpp c java python rust csharp"
    msg_list = message.split()
    print(len(msg_list))


def BaseStrReplace():
    message = "level1, level2"
    old = ["level1", "level2"]
    new = ["A+", "A"]
    for i in range(len(old)):
        message = message.replace(old[i], new[i])
    print(message)

    for n, o in zip(new, old):
        message = message.replace(n, o)
    print(message)


def BaseStrStrip():
    message = "#-m#-sg#-"
    message = message.strip("#-")
    print(message)


def BaseStrFind():
    message = "01234567891"
    start = message.find("12")
    print(start)
    rstart = message.rfind("91")
    print(rstart)


def BaseFor():
    message = " xiaomi11, xiaomi12, xiaomi13, huawei14, huawei15"
    msg_list = message.split(',')
    msg_list = [m.strip() for m in msg_list if "xiaomi" in m]
    print(msg_list)


def BaseList():
    vector = ["first", "second", "third", 4, 5.0]
    res = []
    for v in vector:
        if isinstance(v, str):
            res.append(v)
        elif isinstance(v , int):
            continue
        elif isinstance(v , float):
            print(f"float value: {v}")
        else:
            print(f"Unknown type: {v}")
    print(res)


def BaseListMax():
    vector = ['190', '98', '-1']
    val = [float(v) for v in vector]
    print(max(val))
    print(min(val))

    print(max(vector, key=len))


if __name__ == "__main__":
    # BaseStrStrip()
    # BaseStrReplace()
    # BaseStrFind()
    # BaseFor()
    # BaseStrSplite()
    # BaseList()
    BaseListMax()
    __Test()
