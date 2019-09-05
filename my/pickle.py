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
