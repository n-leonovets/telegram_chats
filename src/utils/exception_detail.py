
def get_exception_detail(e: Exception):
    args = e.args[0] if isinstance(e.args, list) else e.args
    return {
        "module": e.__class__.__module__,
        "name": e.__class__.__name__,
        "message": args
    }
