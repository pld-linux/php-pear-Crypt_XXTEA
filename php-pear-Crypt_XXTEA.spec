%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	XXTEA
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an implementation of XXTEA encryption algorithm
Summary(pl):	%{_pearname} - implemtancja algorytmu szyfruj±cego XXTEA
Name:		php-pear-%{_pearname}
Version:	0.8.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1791047c8a2a5455c0c9e278e11edf0f
URL:		http://pear.php.net/package/Crypt_XXTEA/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XXTEA is a secure and fast encryption algorithm. It's suitable for web
development. This package allows you to encrypt or decrypt a string
using the algorithm.

In PEAR status of this package is: %{_status}.

%description -l pl
XXTEA to bezpieczny i szybki algorytm szyfruj±cy, wygodny w u¿yciu
przy projektowaniu stron internetowych. Pakiet ten pozwala na
szyfrowanie oraz deszyfrowanie ³añcuchów znaków przy u¿yciu tego
algorytmu.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
