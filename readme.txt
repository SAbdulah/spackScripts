1.Stars-H
-----------------------------

Started work on stars-H writing the script from the given Installation instructions:

## STARS-H
cd $STARSHDIR
rm -rf build
mkdir -p build/install_dir


cd build

cmake ..  -DCMAKE_INSTALL_PREFIX=$STARSHDIR/build/install_dir

make -j
make install

export PKG_CONFIG_PATH=$STARSHDIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$STARSHDIR/build/install_dir/lib:$LD_LIBRARY_PATH


From what I learned, I think lines 6-14,19-20 are done automatically through spack. I have added the dependancies and prepended the path using the supplied
kratos spack package as a starting point. This is what I have currently:

from spack.package import *
import os


class StarsH(Package):
    """Package for installing stars-H"""

    homepage = "https://ecrc.github.io/stars-h/index.html"
    url      = "https://github.com/ecrc/stars-h/archive/refs/heads/master.zip"

    # FIXME: Add proper versions and checksums here.
    version('0.3.0')

    #dependencies.
    depends_on('openblas') #queries the system for the best BLAS
    depends_on('gsl')

    #variants
    #no variants needed for stars-H
    
    def setup_run_environment(self, env):
        #I don't know if line 45 is the correct syntax for the second argument self.prefix.pkgconfig
        env.prepend_path('PKG_CONFIG_PATH', self.prefix.pkgconfig) #export PKG_CONFIG_PATH=$STARSHDIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib) #export LD_LIBRARY_PATH=$STARSHDIR/build/install_dir/lib:$LD_LIBRARY_PATH

    def cmake_args(self):
        args = []
        #args.append('-j') apparently not needed, done by default.
       
        return args



2.HiCMA
---------------------


3.ExaGeoStat
----------------------

