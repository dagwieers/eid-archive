Name: eid-archive-el
Version: 2016
Release: 1
Summary: GnuPG archive keys and configuration of the Belgian eID package archive

URL: http://eid.belgium.be/
Source0: http://eid.belgium.be/10a04d46.asc
Source1: http://eid.belgium.be/6773d225.asc
Source2: eid-archive-el.repo
License: GPL

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This package contains the Belgian eID repository GPG key as well as
configuration for yum.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

install -Dpm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-BEID-CONTINUOUS
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-BEID-RELEASE

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/eid-archive.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Thu Mar 24 2016 <wouter.verhelst@fedict.be> - 2016-1
- Add the files2 mirror as a separate repository, to remove a SPOF
* Fri Oct 23 2015 <wouter.verhelst@fedict.be> - 2015-3
- Add the candidate repository
* Wed Jun 10 2015 <wouter.verhelst@fedict.be> - 2015-2
- Remove %post scriptlet, it doesn't work; you can't install a GPG key while
  the RPM lock is held.
* Fri Jan 30 2015 <wouter.verhelst@fedict.be> - 2015-1
- Rebuild to remove eid-archive-el.repo artifact from rpmbuild directory,
  analoguously to the eid-archive-fedora one
* Wed Aug 20 2014 <wouter.verhelst@fedict.be> - 2014-4
- Update link to main archive as well, now. We'll leave the old layout
  functional for now, so that upgrades continue working.
* Fri Aug 1 2014 <wouter.verhelst@fedict.be> - 2014-3
- Update link to continuous archive, so that multiarch can actually
  work. Will need to do something similar for main archive, but that's
  for later.
* Thu Jul 17 2014 <wouter.verhelst@fedict.be> - 2014-2
- Install the GPG keys from the postinst script (with appropriate message).
- Output a message to notify the user that this package is only the first step.
* Thu Jun 12 2014 <wouter.verhelst@fedict.be> - 2014-1
- Create, with inspiration from the epel-release package
