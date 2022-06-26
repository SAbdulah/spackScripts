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
#     spack install exageostat
#
# You can edit this file again by typing:
#
#     spack edit exageostat
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Exageostat(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/ecrc/exageostat/archive/refs/tags/v1.1.0.tar.gz"
    git      = "https://github.com/ecrc/exageostat"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    
    version('master', branch='master',submodules = "update")
    version('1.1.0', sha256='c37fc21c88358b2e93153c28a74a84641ff4df272070f360dc8e71ec24e618bd')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('chameleon')
    depends_on('hicma')
    depends_on('starpu')
    depends_on('stars-h')
    depends_on('hwloc')
    depends_on('openblas')
    depends_on('cuda')
    depends_on('openmpi')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
