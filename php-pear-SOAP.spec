%define		pearname	SOAP
%define		status		beta
Summary:	%{pearname} - Client/Server for PHP
Summary(pl.UTF-8):	%{pearname} - klient/serwer dla PHP
Name:		php-pear-%{pearname}
Version:	0.14.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	f559b8602147d6abbb28e11b4484844a
URL:		http://pear.php.net/package/SOAP/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(bcmath)
Requires:	php(core) >= 4.1
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR-core
Suggests:	php-pear-Mail
Suggests:	php-pear-Mail_Mime
Suggests:	php-pear-Net_DIME
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Mail.* Mail/Mime.* Net/DIME.*

%description
Implementation of SOAP protocol and services.

In PEAR status of this package is; %{status}.

%description -l pl.UTF-8
Implementacja protokołu SOAP i jego serwisów.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/tools .
mv docs/%{pearname}/example examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log 
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/SOAP
%dir %{php_pear_dir}/SOAP/Transport
%dir %{php_pear_dir}/SOAP/Server
%dir %{php_pear_dir}/SOAP/Server/TCP
%dir %{php_pear_dir}/SOAP/Type
%{php_pear_dir}/SOAP/*.php
%{php_pear_dir}/SOAP/Transport/*.php
%{php_pear_dir}/SOAP/Server/*.php
%{php_pear_dir}/SOAP/Server/TCP/Handler.php
%{php_pear_dir}/SOAP/Type/*.php
%{_examplesdir}/%{name}-%{version}
