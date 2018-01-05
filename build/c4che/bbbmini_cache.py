AP_LIBRARIES = ['AP_HAL_Linux']
AP_LIBRARIES_OBJECTS_KW = {}
AR = ['/usr/bin/arm-linux-gnueabihf-ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
BOARD = 'bbbmini'
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/usr/bin/arm-linux-gnueabihf-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('7', '2', '0')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/arm-linux-gnueabihf-g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Werror=format-security', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=switch', '-Wfatal-errors', '-Werror=unused-but-set-variable', '-O3']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/home/light/drone/FlyMew_Ardupilot"', 'CONFIG_HAL_BOARD=HAL_BOARD_LINUX', 'CONFIG_HAL_BOARD_SUBTYPE=HAL_BOARD_SUBTYPE_LINUX_BBBMINI']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_CMATH_ISINF': '', 'HAVE_LIBDL': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'WAF_BUILD': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', '__STDC_FORMAT_MACROS': '', 'HAVE_ENDIAN_H': '', 'HAVE_BYTESWAP_H': '', 'PYTHONDIR': '', 'HAVE_CMATH_ISFINITE': '', 'HAVE_CMATH_ISNAN': '', '_GNU_SOURCE': '', 'PYTHONARCHDIR': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
DSDL_COMPILER = '/home/light/drone/FlyMew_Ardupilot/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/light/drone/FlyMew_Ardupilot/modules/uavcan/libuavcan/dsdl_compiler'
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['gtest', 'mavlink']
HAS_GTEST = True
HAVE_BYTESWAP_H = 1
HAVE_CMATH_ISFINITE = 1
HAVE_CMATH_ISINF = 1
HAVE_CMATH_ISNAN = 1
HAVE_DL = 1
HAVE_ENDIAN_H = 1
INCLUDES = ['/home/light/drone/FlyMew_Ardupilot/libraries/', '/home/light/drone/FlyMew_Ardupilot/libraries/AP_Common/missing']
LIB = ['m', 'dl']
LIBDIR = '/usr/local/lib'
LIBPATH = []
LIBPATH_ST = '-L%s'
LIB_DL = ['dl']
LIB_ST = '-l%s'
LINKFLAGS = ['-Wl,--gc-sections', '-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/arm-linux-gnueabihf-gcc']
LINK_CXX = ['/usr/bin/arm-linux-gnueabihf-g++']
MAVGEN = '/home/light/drone/FlyMew_Ardupilot/modules/mavlink/pymavlink/tools/mavgen.py'
MAVLINK_DIR = '/home/light/drone/FlyMew_Ardupilot/modules/mavlink'
NEED_CMATH_ISFINITE_STD_NAMESPACE = 1
NEED_CMATH_ISINF_STD_NAMESPACE = 1
NEED_CMATH_ISNAN_STD_NAMESPACE = 1
PKGCONFIG = ['/usr/bin/arm-linux-gnueabihf-pkg-config']
PREFIX = '/usr/local'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/local/lib/python2.7/dist-packages'
PYTHONDIR = '/usr/local/lib/python2.7/dist-packages'
PYTHON_VERSION = '2.7'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/usr/bin/arm-linux-gnueabihf-size']
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'arm-linux-gnueabihf'
cfg_files = ['/home/light/drone/FlyMew_Ardupilot/build/bbbmini/ap_config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'
