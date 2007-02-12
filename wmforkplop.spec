Summary:	Kernel processes monitoring dock app
Summary(pl.UTF-8):   Aplet monitorujący procesy jądra
Name:		wmforkplop
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://hules.free.fr/wmforkplop/%{name}-%{version}.tar.gz
# Source0-md5:	70d5ab10614f773674f6c957ddeb1afd
Source1:	%{name}.desktop
URL:		http://hules.free.fr/wmforkplop/
BuildRequires:	XFree86-devel
BuildRequires:	imlib2-devel
BuildRequires:	libgtop-devel >= 1:2.14.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmforkplop is a blend of wmhdplop and wmtop. It monitors the forking
activity of the kernel and displays a list of the most cpu-consuming
processes.

%description -l pl.UTF-8
wmforkplop jest połączeniem wmhdplopa i wmtopa monitorującym tworzenie
przez jądro nowych procesów i wyświetlającym te najbardziej
obciążające procesor.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/docklets/*
