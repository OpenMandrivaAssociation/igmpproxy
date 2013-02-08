Name: igmpproxy
Version: 0.1
Release: 2
License: GPL
Group: System/Servers
Summary: IGMPproxy is a simple mulitcast router for Linux that only uses the IGMP protocol

Source0: http://sourceforge.net/projects/igmpproxy/igmpproxy-%{version}.tar.gz
Source1: igmpproxy.init

BuildRequires: gcc

%description
igmpproxy is a simple multicast router for Linux that only uses the IGMP
protocol.

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


%changelog
* Wed Nov 24 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.1-1mdv2011.0
+ Revision: 600889
- Fixed group to comply with the policy.
- Cleaned up spec.

  + zamir <zamir@mandriva.org>
    - first build
    - Created package structure for igmpproxy.

