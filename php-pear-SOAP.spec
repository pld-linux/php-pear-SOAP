%include	/usr/lib/rpm/macros.php
%define		_class		SOAP
%define		_pearname	%{_class}
%define		_status		beta
%define		_rc		RC3

Summary:	%{_pearname} - Client/Server for PHP
Summary(pl):	%{_pearname} - klient/serwer dla PHP
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	0.%{_rc}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	1181071986f31a89ecc5a4aa5fd8c9c4
URL:		http://pear.php.net/package/SOAP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-bcmath
Requires:	php-pcre
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of SOAP protocol and services.

This class has in PEAR status; %{_status}.

%description -l pl
Implementacja protoko³u SOAP i jego serwisów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{tools,Transport,Server,Type}

install %{_pearname}-%{version}%{_rc}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}%{_rc}/tools/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/tools
install %{_pearname}-%{version}%{_rc}/Transport/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Transport
install %{_pearname}-%{version}%{_rc}/Server/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Server
install %{_pearname}-%{version}%{_rc}/Type/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Type

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_rc}/example
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
