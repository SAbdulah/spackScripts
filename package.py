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

from spack.package import *


class StarsH(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    # DONE, but the  link is for a zip file
    homepage = "https://ecrc.github.io/stars-h/"
    url      = "https://github.com/ecrc/stars-h/archive/refs/heads/master.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions here.
    version('0.3.0') # some examples have sha 256 ask  prof

    # FIXME: Add dependencies if required.
    depends_on('openblas') #is this the right choice for BLAS?
    depends_on('gsl')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
       #check if 2 otherfunctions are necessary with prof.
    def cmake_args(self):
        args = []
        # add arguments other than CMAKE INSTALL PREFIX and BUILD  type.
        return args
