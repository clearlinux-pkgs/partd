#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : partd
Version  : 0.3.8
Release  : 2
URL      : https://files.pythonhosted.org/packages/e7/0c/b257648852230acf169c60283e59475727b156ee1a0a3a6b5527af745f15/partd-0.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/0c/b257648852230acf169c60283e59475727b156ee1a0a3a6b5527af745f15/partd-0.3.8.tar.gz
Summary  : Appendable key-value storage
Group    : Development/Tools
License  : BSD-3-Clause
Requires: partd-python3
Requires: partd-license
Requires: partd-python
Requires: locket
Requires: numpy
Requires: pandas
Requires: pyzmq
Requires: toolz
BuildRequires : buildreq-distutils3

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

%description python3
python3 components for the partd package.


%prep
%setup -q -n partd-0.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538790300
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/partd
cp LICENSE.txt %{buildroot}/usr/share/doc/partd/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/partd/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
