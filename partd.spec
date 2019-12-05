#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : partd
Version  : 1.1.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/ad/94/1cdbd9c7196656dc7b40139a6c26650af111bb4095442b0be06e5636a536/partd-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/94/1cdbd9c7196656dc7b40139a6c26650af111bb4095442b0be06e5636a536/partd-1.1.0.tar.gz
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
PartD
=====
|Build Status| |Version Status|
Key-value byte store with appendable values

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

%description python3
python3 components for the partd package.


%prep
%setup -q -n partd-1.1.0
cd %{_builddir}/partd-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574459486
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/partd
cp %{_builddir}/partd-1.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/partd/395d3fcb94348847e3b7afbfbdae2adeb0d6ec00
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
