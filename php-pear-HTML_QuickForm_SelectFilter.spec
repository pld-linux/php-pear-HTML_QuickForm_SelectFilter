%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_SelectFilter

Summary:	%{_pearname} - dynamic filters on the client side for select elements
Summary(pl):	%{_pearname} - dynamiczne filtry po stronie klienta dla pól wyboru
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define		_pre	RC1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_pre}.tgz
# Source0-md5:	06860491c616e3f418d1b033145af446
URL:		http://pear.php.net/package/HTML_QuickForm_SelectFilter/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_QuickForm_SelectFilter package adds an element to the
PEAR::HTML_QuickForm package that is used to define dynamic filters on
the client side for select elements.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::HTML_QuickForm_SelectFilter dodaje do klasy
PEAR::HTML_QuickForm element, który mo¿e byæ u¿yty do zdefiniowania
dzia³aj±cych po stronie klienta dynamicznych filtrów pól wyboru.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}%{_pre}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
