from distutils.core import setup
from distutils.extension import Extension
import re

INC = ['..', 'cdec/', '../decoder', '../utils', '../mteval']
LIB = ['../decoder', '../utils', '../mteval', '../training/utils', '../klm/lm', '../klm/util', '../klm/util/double-conversion', '../klm/search']

# Set automatically by configure
LIBS = re.findall('-l([^\s]+)', '-ldl  -lboost_program_options-mt -lboost_serialization-mt -lboost_system-mt -lboost_filesystem-mt  -lz -lbz2')
CPPFLAGS = re.findall('-[^\s]+', '-DPIC  -I/usr/local/Cellar/boost/1.55.0/include  -DHAVE_CONFIG_H -DKENLM_MAX_ORDER=6 -std=gnu++11  -fPIC -g -O3')
LDFLAGS = re.findall('-[^\s]+', ' -L/usr/local/Cellar/boost/1.55.0/lib -Wl,-rpath,/usr/local/Cellar/boost/1.55.0//lib -L/usr/local/Cellar/boost/1.55.0/lib -Wl,-rpath,/usr/local/Cellar/boost/1.55.0//lib -L/usr/local/Cellar/boost/1.55.0//lib -Wl,-rpath,/usr/local/Cellar/boost/1.55.0//lib -L/usr/local/Cellar/boost/1.55.0//lib -Wl,-rpath,/usr/local/Cellar/boost/1.55.0//lib')

ext_modules = [
    Extension(name='cdec._cdec',
        sources=['cdec/_cdec.cpp'],
        include_dirs=INC,
        library_dirs=LIB,
        libraries=['cdec', 'utils', 'mteval', 'training_utils', 'klm', 'klm_util', 'klm_util_double', 'ksearch'] + LIBS,
        extra_compile_args=CPPFLAGS,
        extra_link_args=LDFLAGS),
    Extension(name='cdec.sa._sa',
        sources=['cdec/sa/_sa.cpp', 'cdec/sa/strmap.cc'],
        extra_compile_args=CPPFLAGS)
]

setup(
    name='cdec',
    ext_modules=ext_modules,
    packages=['cdec', 'cdec.sa']
)
