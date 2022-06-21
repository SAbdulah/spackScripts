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
Started work on HiCMA writing the script from the given Installation instructions:

cd $HICMADIR
rm -rf build
mkdir -p build/install_dir
cd build
#===============
cmake ..  -DCMAKE_INSTALL_PREFIX=$PWD/install_dir -DCMAKE_COLOR_MAKEFILE:BOOL=ON -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DBUILD_SHARED_LIBS=ON -DHICMA_USE_MPI=OFF 
 
make -j
make install

export PKG_CONFIG_PATH=$HICMADIR/build/install_dir/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$HICMADIR/build/install_dir/lib:$LD_LIBRARY_PATH

Currently I have this:

from spack.package import *


class Hicma(Package):
    """Package for installing HiCMA"""

    # URL
    homepage = "https://github.com/ecrc/hicma"
    url      = "https://github.com/ecrc/hicma/archive/refs/heads/master.zip"

    
    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    #dependancies 
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

3.ExaGeoStat
----------------------

