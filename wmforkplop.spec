Summary:	Kernel processes monitoring dock app
Summary(pl):	Aplet monitoruj±cy procesy j±dra
Name:		wmforkplop
Version:	0.9.1
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://hules.free.fr/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	74d25af52db37c613aa935c33c49c272
Source1:	%{name}.desktop
URL:		http://hules.free.fr/wmforkplop/
BuildRequires:	XFree86-devel
BuildRequires:	imlib2-devel
BuildRequires:	libgtop-devel >= 1:2.10.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmforkplop is a blend of wmhdplop and wmtop. It monitors the forking
activity of the kernel and displays a list of the most cpu-consuming
processes.

%description -l pl
wmforkplop jest po³±czeniem wmhdplopa i wmtopa monitoruj±cym tworzenie
przez j±dro nowych procesów i wy¶wietlaj±cym te najbardziej
obci±¿aj±ce procesor.

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
