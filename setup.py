from setuptools import setup, Extension
# from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options as cyopts
from glob import glob
from pathlib import Path


cyopts.cimport_from_pyx = True


def mkcythonexts(base, allowed_ext={'.pyx', '.py'}, allow_cwd=False):
    '''
    given a base directory, constructs a cython module for each source file
    found within, of a matching extension type
    '''
    base = Path(base)
    exts = []
    for src in base.rglob('*.py*'):
        if src.suffix not in allowed_ext: continue
        name = str(src.parent) + '.' + src.stem
        if allow_cwd and src.parent == base:
            name = src.stem
        elif src.parent == base: continue
        if 'setup' in str(src): continue
        print('INFO found matching source', src, name)
        exts += [Extension(name, [str(src)], language='c++')]
    return cythonize(exts, annotate=False)#, compiler_directives={'language_level': '3'})

setup(
        ext_modules = mkcythonexts(Path('.'), allowed_ext=['.pyx'], 
                                   allow_cwd=True) 
        )
