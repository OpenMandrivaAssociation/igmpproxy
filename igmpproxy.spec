Name: igmpproxy
Version: 0.1
Release: 2
License: GPL
Group: System/Servers
Summary: Simple mulitcast router for Linux that only uses the IGMP protocol

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
%makeinstall
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}/usr/src
install -D -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%clean

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS
%{_sbindir}/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
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

