Summary:	X.org cf files
Summary(pl.UTF-8):	Pliki cf z X.org
Name:		xorg-cf-files
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
# Source0-md5:	10546b5ddda3cdda7950bb56bf98e0ea
Patch0:		%{name}-lib64.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org cf files.

%description -l pl.UTF-8
Pliki cf z X.org.

%prep
%setup -q -n %{name}-%{version}
%if "%{_lib}" == "lib64"
%patch0 -p1
%endif

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_libdir}/X11/config
