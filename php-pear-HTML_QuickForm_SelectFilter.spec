%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_SelectFilter

Summary:	%{_pearname} - dynamic filters on the client side for select elements
Summary(pl.UTF-8):   %{_pearname} - dynamiczne filtry po stronie klienta dla pól wyboru
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define		_rc	RC1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	06860491c616e3f418d1b033145af446
URL:		http://pear.php.net/package/HTML_QuickForm_SelectFilter/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_QuickForm_SelectFilter package adds an element to the
PEAR::HTML_QuickForm package that is used to define dynamic filters on
the client side for select elements.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::HTML_QuickForm_SelectFilter dodaje do klasy
PEAR::HTML_QuickForm element, który może być użyty do zdefiniowania
działających po stronie klienta dynamicznych filtrów pól wyboru.

Ta klasa ma w PEAR status: %{_status}.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
