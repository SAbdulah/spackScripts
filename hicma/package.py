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
#     spack install hicma
#
# You can edit this file again by typing:
#
#     spack edit hicma
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Hicma(Package):
    """Package for installing HiCMA"""

    # URL
    homepage = "https://github.com/ecrc/hicma"
    url      = "https://github.com/ecrc/hicma/archive/refs/heads/master.zip"

    
    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    # FIXME: 
    depends_on('openblas')
    depends_on('chameleon')
    depends_on('stars-h')

        #variant
    variant('mpi', default=False, description='Builds a MPI version of the library [Distributed]')
    depends_on('mpi', when='+mpi')
    variant('cuda', default=False, description='Builds a cuda version of the library [Cuda]')
    depends_on('cuda', when='+cuda')
    
    env.prepend_path('PKG_CONFIG_PATH', self.prefix.pkgconfig) #export PKG_CONFIG_PATH=$STARSHDIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
    env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib) #export LD_LIBRARY_PATH=$STARSHDIR/build/install_dir/lib:$LD_LIBRARY_PATH
    
    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = []
        if self.spec.variants['mpi'].value == True:
            args.append('HICMA_USE_MPI=ON')
        else:
            args.append('HICMA_USE_MPI=OFF')
        if self.spec.variants['cuda'].value == True:
            args.append('HICMA_USE_CUDA=ON')
        else:
            args.append('HICMA_USE_CUDA=OFF')
        return args
