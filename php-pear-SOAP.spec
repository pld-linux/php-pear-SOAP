%include	/usr/lib/rpm/macros.php
%define		_class		SOAP
%define		_pearname	%{_class}
%define		_status		beta
Summary:	%{_pearname} - Client/Server for PHP
Summary(pl):	%{_pearname} - klient/serwer dla PHP
Name:		php-pear-%{_pearname}
Version:	0.9.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b016e4cb3654bf97ac7fef4ea98abdfd
URL:		http://pear.php.net/package/SOAP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-bcmath
Requires:	php-common >= 3:4.1
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(Mail.*)' 'pear(Mail/Mime.*)' 'pear(Net/DIME.*)'

%description
Implementation of SOAP protocol and services.

In PEAR status of this package is; %{_status}.

%description -l pl
Implementacja protoko³u SOAP i jego serwisów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/example
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/tools
%dir %{php_pear_dir}/%{_class}/Transport
%dir %{php_pear_dir}/%{_class}/Server
%dir %{php_pear_dir}/%{_class}/Type
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/tools/*.php
%{php_pear_dir}/%{_class}/Transport/*.php
%{php_pear_dir}/%{_class}/Server/*.php
%{php_pear_dir}/%{_class}/Type/*.php
