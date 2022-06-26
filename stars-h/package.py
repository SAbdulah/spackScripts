# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install stars-h
#
# You can edit this file again by typing:
#
#     spack edit stars-h
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from importlib_metadata import version
from spack.package import *
import os


class StarsH(CMakePackage):
    """Package for installing stars-H"""

    homepage = "https://ecrc.github.io/stars-h/index.html"
    url      = "https://github.com/ecrc/stars-h/archive/refs/tags/v0.3.0.tar.gz"
    git      = "https://github.com/ecrc/stars-h"


    #git submodule update --init --recursive?
    version('master', branch='master',submodules = "update") 
    #version('rabab/RBF', branch='rabab/RBF')
    #version('release/v0.1.1', branch='release/v0.1.1')
    version('0.3.0', sha256='883c2091c7910c24ed22ffc99ce29b2b2d21e4b4c9df6764b6157457fd9b167b')
    version('0.2.0', sha256='b58c0fdb2f157cb0320c7da8062c200d4bd20a779ff7f790bb5177e6df20e48b')

    #dependencies.
    depends_on('openblas') #queries the system for the best BLAS
    depends_on('gsl')

    #variants
    #no variants needed for stars-H
    
    def setup_run_environment(self, env):
        #I don't know if line 45 is the correct syntax for the second argument self.prefix.pkgconfig
        #put in different function?
        #env.prepend_path('PKG_CONFIG_PATH', self.prefix.pkgconfig) #export PKG_CONFIG_PATH=$STARSHDIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib) #export LD_LIBRARY_PATH=$STARSHDIR/build/install_dir/lib:$LD_LIBRARY_PATH

    def cmake_args(self):
        args = []
        #args.append('-j') apparently not needed, done by default.
        #args.append('-DMPI=OFF -DOPENMP=OFF -DSTARPU=OFF -DCMAKE_C_FLAGS="-fPIC"')
        return args
