import os

import my


def test_pickling():
    shrugs = r'¯\_(ツ)_/¯'
    filename = 'shrugs.pickle'

    try:
        os.remove(filename)
    except OSError:
        pass

    my.dump(shrugs, filename)
    x = my.load(filename)
    assert x == shrugs

    os.remove(filename)
