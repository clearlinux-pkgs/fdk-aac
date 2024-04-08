#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : fdk-aac
Version  : 2.0.3
Release  : 1
URL      : https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v2.0.3.tar.gz
Source0  : https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v2.0.3.tar.gz
Summary  : AAC codec library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: fdk-aac-lib = %{version}-%{release}
Requires: fdk-aac-license = %{version}-%{release}
BuildRequires : buildreq-cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Fuzzer for libFraunhoferAAC decoder
## Plugin Design Considerations
The fuzzer plugin for aac decoder is designed based on the understanding of the
codec and tries to achieve the following:

%package dev
Summary: dev components for the fdk-aac package.
Group: Development
Requires: fdk-aac-lib = %{version}-%{release}
Provides: fdk-aac-devel = %{version}-%{release}
Requires: fdk-aac = %{version}-%{release}

%description dev
dev components for the fdk-aac package.


%package lib
Summary: lib components for the fdk-aac package.
Group: Libraries
Requires: fdk-aac-license = %{version}-%{release}

%description lib
lib components for the fdk-aac package.


%package license
Summary: license components for the fdk-aac package.
Group: Default

%description license
license components for the fdk-aac package.


%prep
%setup -q -n fdk-aac-2.0.3
cd %{_builddir}/fdk-aac-2.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712616543
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1712616543
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fdk-aac
cp %{_builddir}/fdk-aac-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/fdk-aac/fbf78018934c1dee3df441ee708d17167b956d22 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/fdk-aac/FDK_audio.h
/usr/include/fdk-aac/aacdecoder_lib.h
/usr/include/fdk-aac/aacenc_lib.h
/usr/include/fdk-aac/genericStds.h
/usr/include/fdk-aac/machine_type.h
/usr/include/fdk-aac/syslib_channelMapDescr.h
/usr/lib64/cmake/fdk-aac/fdk-aac-config-version.cmake
/usr/lib64/cmake/fdk-aac/fdk-aac-config.cmake
/usr/lib64/cmake/fdk-aac/fdk-aac-targets-relwithdebinfo.cmake
/usr/lib64/cmake/fdk-aac/fdk-aac-targets.cmake
/usr/lib64/libfdk-aac.so
/usr/lib64/pkgconfig/fdk-aac.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfdk-aac.so.2
/usr/lib64/libfdk-aac.so.2.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fdk-aac/fbf78018934c1dee3df441ee708d17167b956d22