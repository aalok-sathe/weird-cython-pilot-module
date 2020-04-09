from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize
from Cython.Compiler import Options

import os
from glob import glob
from pathlib import Path

Options.cimport_from_pyx = True

def mkcythonexts(base, allowed_ext={'.pyx', '.py'}, allow_cwd=False, 
                 exclude={'setup.py'}):
    '''
    given a base directory, constructs a cython module for each source file
    found within, of a matching extension type
    '''
    base = Path(base)
    exts = []
    for src in base.rglob('*.py*'):
        if src.suffix not in allowed_ext: continue
        name = '.'.join(str(src.parent).split('/')) + '.' + src.stem
        if allow_cwd and src.parent == base:
            name = src.stem
        elif src.parent == base: continue
        if str(src) in exclude: continue
        print('INFO found matching source', src, name)
        exts += [Extension(name, [str(src)], language='c++')]
    return cythonize(exts, annotate=False, 
                     compiler_directives={'language_level': '3str',
                                          'annotation_typing': True})

class build_ext(build_ext):
    def build_extensions(self):
        if '-Wstrict-prototypes' in self.compiler.compiler_so:
            self.compiler.compiler_so.remove('-Wstrict-prototypes')
        super().build_extensions()

setup(
        name = 'cymodule',
        ext_modules = mkcythonexts(Path('.'), allow_cwd=True,
                                   exclude=['setup.py']),
        include_dirs=['.'],
        package_data = { 'cymodule': map(str, Path('.').rglob('*.pxd')) },
        cmdclass={'build_ext': build_ext},
    )
