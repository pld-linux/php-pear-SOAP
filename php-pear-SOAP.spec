%include	/usr/lib/rpm/macros.php
%define		_class		SOAP
%define		_pearname	%{_class}
Summary:	%{_class} - Client/Server for PHP
Summary(pl):	%{_class} - klient/serwer dla PHP
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-bcmath
Requires:	php-pcre
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of SOAP protocol and services.

%description -l pl
Implementacja protoko³u SOAP i jego serwisów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{tools,Transport,Server,Type}

install %{_pearname}-%{version}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/tools/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/tools
install %{_pearname}-%{version}/Transport/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Transport
install %{_pearname}-%{version}/Server/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Server
install %{_pearname}-%{version}/Type/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Type

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{example,interop,test}/*
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
