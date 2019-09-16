import pickle


def dump(obj, filename: str, *args, **kwargs):
    """Pickle dump object to a file"""
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, *args, **kwargs)


def load(filename: str, *args, **kwargs):
    """Pickle load an object from a file"""
    with open(filename, 'rb') as f:
        obj = pickle.load(f, *args, **kwargs)

    return obj

def load_or_do(filename, func):
    """Load a stored object or assign the return value if the file can't be unpickled"""
    try:
        with open(filename, 'rb') as f:
            obj = pickle.load(f)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        obj = func()
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)

    return obj
