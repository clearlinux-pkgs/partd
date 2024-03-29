#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : partd
Version  : 1.2.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/9c/b4/3674cd02e2b198a50cea6b73c899ee3176004d28f52556093aefadf69b8a/partd-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/b4/3674cd02e2b198a50cea6b73c899ee3176004d28f52556093aefadf69b8a/partd-1.2.0.tar.gz
Summary  : Appendable key-value storage
Group    : Development/Tools
License  : BSD-3-Clause
Requires: partd-license = %{version}-%{release}
Requires: partd-python = %{version}-%{release}
Requires: partd-python3 = %{version}-%{release}
Requires: locket
Requires: numpy
Requires: pandas
Requires: pyzmq
Requires: toolz
BuildRequires : buildreq-distutils3
BuildRequires : locket
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : pyzmq
BuildRequires : toolz

%description
=====
        
        |Build Status| |Version Status|
        
        Key-value byte store with appendable values
        
            Partd stores key-value pairs.
            Values are raw bytes.
            We append on old values.
        
        Partd excels at shuffling operations.
        
        Operations
        ----------
        
        PartD has two main operations, ``append`` and ``get``.
        
        
        Example
        -------

%package license
Summary: license components for the partd package.
Group: Default

%description license
license components for the partd package.


%package python
Summary: python components for the partd package.
Group: Default
Requires: partd-python3 = %{version}-%{release}

%description python
python components for the partd package.


%package python3
Summary: python3 components for the partd package.
Group: Default
Requires: python3-core
Provides: pypi(partd)
Requires: pypi(locket)
Requires: pypi(toolz)

%description python3
python3 components for the partd package.


%prep
%setup -q -n partd-1.2.0
cd %{_builddir}/partd-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618244344
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/partd
cp %{_builddir}/partd-1.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/partd/395d3fcb94348847e3b7afbfbdae2adeb0d6ec00
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/partd/395d3fcb94348847e3b7afbfbdae2adeb0d6ec00

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
