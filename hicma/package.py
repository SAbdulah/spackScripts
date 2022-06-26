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


class Hicma(CMakePackage):
    """FIXME: Put a proper description of your package here."""


    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/ecrc/hicma/archive/refs/tags/v0.1.3.tar.gz"
    git      = "https://github.com/ecrc/hicma"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
        #git submodule update --init --recursive?
    version('master', branch='master',submodules = "update") 
    version('0.1.3', sha256='556013d00139ebe7961d7d4f6ac0fadc6fc6c1b58c70ee49345fad2a881fd1a7')
    version('0.1.1', sha256='f5ccc69e22644c4ff0559e2af02dcc1dfd40d73e825b17eac119d807642e7fdb')

        # FIXME: 
    depends_on('openblas')
    depends_on('chameleon')
    depends_on('stars-h')

        #variant
    variant('mpi', default=False, description='Builds a MPI version of the library [Distributed]')
    depends_on('mpi', when='+mpi')
    variant('cuda', default=False, description='Builds a cuda version of the library [Cuda]')
    depends_on('cuda', when='+cuda')
    
    def setup_run_environment(self, env):
        #I don't know if line 50 is the correct syntax for the second argument self.prefix.pkgconfig
        #put in different function?
        #env.prepend_path('PKG_CONFIG_PATH', self.prefix.pkgconfig) #export PKG_CONFIG_PATH=$STARSHDIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
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