"""
Based on code from the PyStan docs:
https://pystan.readthedocs.io/en/latest/avoiding_recompilation.html
"""

import pystan
from .pickle import load_or_do
from hashlib import md5


def StanModel(model_code=None, model_name=None, **kwargs):
    """pystan.StanModel that caches the model"""
    if model_code is None:
        return pystan.StanModel(model_name=model_name, **kwargs)
    code_hash = md5(model_code.encode()).hexdigest()
    if model_name is None:
        cache_file = 'cached-model-{}.pkl'.format(code_hash)
    else:
        cache_file = 'cached-{}-{}.pkl'.format(model_name, code_hash)

    return load_or_do(cache_file, lambda: pystan.StanModel(model_code=model_code, **kwargs))
