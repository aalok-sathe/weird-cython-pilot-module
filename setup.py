from distutils.core import setup, Extension
from glob import glob
from pathlib import Path
from Cython.Build import cythonize

def mkcythonexts(base, allowed_ext={'.pyx', '.py'}):
    '''
    given a base directory, constructs a cython module for each source file
    found within, of a matching extension type
    '''
    base = Path(base)
    exts = []
    for src in base.rglob('*.py*'):
        if src.suffix not in allowed_ext: continue
        if src.parent == base: continue
        name = str(src.parent) + '.' + src.stem
        exts += [Extension(name, [str(src)])]
    return cythonize(exts, annotate=False, language_level='3')

setup( ext_modules = mkcythonexts(Path('.')) )
