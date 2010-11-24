%global upstream_name keyring

%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

Name:           python-keyring
Version:        0.4
Release:        1%{?dist}
Summary:        Python library to access the system keyring service

Source0:        http://pypi.python.org/packages/source/k/keyring/%{upstream_name}-%{version}.tar.gz
License:        Python
Group:          Development/Libraries
URL:            http://pypi.python.org/pypi/keyring

# Actually the main package is noarch but -gnome and -kwallet contain
# architecture-specific code. Currently it's impossible to have a noarch main
# package with arch-specific subpackages. Therefore we can't use 'noarch' here.
BuildRequires:  python-devel

# Gnome-Keyring
BuildRequires:  dbus-devel glib2-devel gnome-keyring-devel

# KWallet
BuildRequires:  kdelibs4-devel


%description
The Python keyring lib provides a easy way to access the system keyring 
service from python. It can be used in any application that needs safe 
password storage.

This package only provides file-based pseudo-keyrings. To interface with 
gnome-keyring or KWallet, please install one of python-keyring-gnome or 
python-keyring-kwallet.


%package        gnome
Summary:        Use gnome-keyring as backend for python-keyring
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       dbus gnome-keyring

%description    gnome
Integrate python-keyring with gnome-keyring so passwords can be read from/
stored in the gnome-keyring database.


%package        kwallet
Summary:        Use KWallet as backend for python-keyring
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    kwallet
Integrate python-keyring with KWallet so passwords can be read 
from/stored in the KWallet database.


%prep
%setup -q -n %{upstream_name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-L %{_libdir}/kde4/devel" %{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
#%{__rm} -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%doc README.txt demo
%{python_sitearch}/%{upstream_name}
%{python_sitearch}/%{upstream_name}-*.egg-info

%files gnome
%defattr(-,root,root,-) 
%{python_sitearch}/gnome_keyring.so

%files kwallet
%defattr(-,root,root,-) 
%{python_sitearch}/kde_kwallet.so


%changelog
* Mon Nov 01 2010 rtnpro <rtnpro@gmail.com> 0.4-1
- Updated rpm to python-keyring version 0.4

* Sat Oct 30 2010 rtnpro <rtnpro@gmail.com> 0.2-4
- Filtered gnome_keyring.so from the provides list, removed kdelibs-devel

* Sat Oct 02 2010 rtnpro <rtnpro@gmail.com> 0.2-3
- Updated dependencies to kdelibs4-devel, some cleanup

* Tue Aug 24 2010 rtnpro <rtnpro@gmail.com> 0.2-2
- Some updates according to bugzilla reviews

* Sat Jun 26 2010 rtnpro <rtnpro@gmail.com> 0.2-1.3
- Some cleanup

* Sat Jun 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.2
- add KWallet subpackage

* Mon Jun 21 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.1
- add build dependencies
- create subpackage for gnome, disable KWallet for now
- look for files in arch-dependend site-packages

* Tue May 25 2010 rtnpro <rtnpro@gmail.com> 0.2-1
- Incorporated some changes with reference to http://vcrhonek.fedorapeople.org/python-keyring/python-keyring.spec
- Fixed some rpmlint errors

* Wed May 19 2010 rtnpro <rtnpro@gmail.com> 0.2
- Initial RPM package


