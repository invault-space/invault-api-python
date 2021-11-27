from typing import (
    Any,
    Callable,
    Type
)


def to_type(tpy: Type) -> Callable[[Any], Any]:
    def cast_f(v: Any):
        if v is None:
            return v
        return tpy(v)
    return cast_f

def to_bytes(s, encoding="latin-1"):
    if isinstance(s, bytes):
        return s
    elif isinstance(s, bytearray):
        return bytes(s)
    elif isinstance(s,str):
        return s.encode(encoding)
    else:
        return bytes([s])

def to_self(v: Any) -> Any:
    return v

def cast_dict_with_formater(formater: dict, val: dict) -> dict:
    if not isinstance(val, dict):
        raise TypeError("val is not dict instance")
    fmt = formater.copy()
    val_fmt = {}
    for k, v in val.items():
        fmt_f = fmt.pop(k)
        val_fmt[k] = fmt_f(v)
    return val_fmt