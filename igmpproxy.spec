Name: igmpproxy
Version: 0.1
Release: %mkrel 1
License: GPL
Group: Applications/Internet
Summary: IGMPproxy is a simple mulitcast router for Linux that only uses the IGMP protocol
BuildRoot: %{_tmppath}/%{name}-%{version}

Source0: http://sourceforge.net/projects/igmpproxy/igmpproxy-%{version}.tar.gz
Source1: igmpproxy.init

BuildRequires: gcc

%description
igmpproxy is a simple multicast router for Linux that only uses the IGMP protocol.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}/usr/src
install -D -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_sbindir}/%{name}
%{_mandir}/*
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
