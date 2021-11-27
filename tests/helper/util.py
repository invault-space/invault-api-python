
def to_underline_name(name: str):
    return ''.join(["_" + i.lower() if i.isupper() else i for i in name])

def upper_first_char(name: str):
    if not name:
        return name
    return name[0].upper() + name[1:]

def get_method_fn(client, fn_name):
    method_fn = getattr(client.assets, fn_name, None)
    if method_fn is not None:
        return method_fn
    method_fn = getattr(client.withdraw, fn_name, None)
    if method_fn is not None:
        return method_fn
    method_fn = getattr(client.transaction, fn_name, None)
    if method_fn is not None:
        return method_fn