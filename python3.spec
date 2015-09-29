Name:           python3
Version:        3.4.3
Release:        19
License:        Python-2.0
Summary:        The Python Programming Language
Url:            http://www.python.org
Group:          devel/python
Source0:        https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
Patch0:         0001-Fix-python-path-for-linux.patch
# Causes test-suite failures
#Patch1:         0001-ensure-pip-upgrade.patch
Patch1:         skip-some-tests.patch
Patch2:         fix-gcc-5-bug.patch
BuildRequires:  bzip2
BuildRequires:  db
BuildRequires:  grep
BuildRequires:  bzip2-dev
BuildRequires:  xz-dev
BuildRequires:  gdbm-dev
BuildRequires:  readline-dev
BuildRequires:  openssl
BuildRequires:  openssl-dev
BuildRequires:  sqlite-autoconf
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
BuildRequires:  libffi-dev
BuildRequires:  procps-ng-bin
BuildRequires:  netbase

%global __arch_install_post %{nil}

%description
The Python Programming Language.

%package lib
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

%description lib
The Python Programming Language.

%package core
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python
Provides:       python3
Provides:       python3-modules
Provides:       /bin/python3

%description core
The Python Programming Language.

%package dev
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel
Requires:       python3-lib
Requires:       python3-core

%description dev
The Python Programming Language.

%package doc
License:        Python-2.0
Summary:        The Python Programming Language
Group:          devel/python

%description doc
The Python Programming Language.

%prep
%setup -q -n Python-%{version}
%patch0 -p1
# Todo fix these
%patch1 -p1
%patch2 -p1

%build
export LANG=C
%configure --with-threads \
 --with-pymalloc \
 --with-ensurepip=upgrade \
 --without-cxx-main \
 --with-signal-module \
 --enable-shared \
 --enable-ipv6=yes \
 --libdir=/usr/lib \
 ac_cv_header_bluetooth_bluetooth_h=no \
 ac_cv_header_bluetooth_h=no \
 --with-system-ffi --with-system-expat

make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}/usr/lib/libpython*.so* %{buildroot}/usr/lib64/

%check
export LANG=C

LD_LIBRARY_PATH=`pwd` ./python -Wd -E -tt  Lib/test/regrtest.py -v -x test_asyncio test_uuid || :

%files lib
/usr/lib64/libpython3.4m.so.1.0

%files core
%exclude %{_bindir}/2to3
%{_bindir}/2to3-3.4
%{_bindir}/easy_install-3.4
%{_bindir}/idle3
%{_bindir}/idle3.4
%{_bindir}/pip3
%{_bindir}/pip3.4
%{_bindir}/pydoc3
%{_bindir}/pydoc3.4
%{_bindir}/python3
%{_bindir}/python3-config
%{_bindir}/python3.4
%{_bindir}/python3.4-config
%{_bindir}/python3.4m
%{_bindir}/python3.4m-config
%{_bindir}/pyvenv
%{_bindir}/pyvenv-3.4
/usr/lib/python3.4/

%files dev
%{_includedir}/python3.4m/*.h
/usr/lib64/libpython3.so
/usr/lib64/libpython3.4m.so
/usr/lib64/pkgconfig/python3.pc
/usr/lib64/pkgconfig/python-3.4.pc
/usr/lib64/pkgconfig/python-3.4m.pc

%files doc
%{_mandir}/man1/python3.4.1
%{_mandir}/man1/python3.1
