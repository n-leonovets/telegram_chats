
def get_exception_detail(e: Exception):
    return {
        "module": e.__class__.__module__,
        "name": e.__class__.__name__,
        "message": e.args[0]
    }
