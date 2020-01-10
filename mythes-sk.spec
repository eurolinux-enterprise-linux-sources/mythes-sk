Name: mythes-sk
Summary: Slovak thesaurus
%define upstreamid 20130130
Version: 0.%{upstreamid}
Release: 2%{?dist}
Source: http://www.sk-spell.sk.cx/thesaurus/download/OOo-Thesaurus2-sk_SK.zip
Group: Applications/Text
URL: http://www.sk-spell.sk.cx/thesaurus/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: MIT
BuildArch: noarch
Requires: mythes

%description
Slovak thesaurus.

%prep
%setup -q -c

%build
for i in README_th_sk_SK_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sk_SK_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_sk_SK_v2.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20130130-2
- Mass rebuild 2013-12-27

* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20130130-1
- Resolves: rhbz#905991 latest version

* Fri Nov 02 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120911-2
- clarify license

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120911-1
- latest version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120612-1
- latest version

* Fri Apr 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120412-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20111016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20111016-1
- latest version

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110807-1
- latest version

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110608-1
- latest version

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110316-1
- latest version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101220-1
- latest version

* Mon Oct 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101010-1
- latest version

* Wed Sep 08 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100907-1
- latest version

* Mon Aug 09 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100807-1
- latest version

* Mon Jul 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100704-1
- latest version

* Sat Jun 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100604-1
- latest version

* Wed May 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100504-1
- latest version

* Mon Apr 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100404-1
- latest version

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100304-2
- mythes now owns /usr/share/mythes

* Fri Mar 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100304-1
- latest version

* Fri Feb 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100204-1
- latest version

* Tue Jan 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100104-1
- latest version

* Tue Nov 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091031-1
- latest version

* Tue Sep 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090907-1
- latest version

* Sat Aug 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090807-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090707-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090707-2
- tidy spec

* Wed Jul 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090707-1
- latest version

* Mon Jun 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090607-1
- latest version

* Thu Apr 02 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090402-1
- latest version

* Tue Mar 03 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090302-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090202-1
- latest version

* Mon Jan 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090102-1
- latest version

* Thu Nov 27 2008 Caolán McNamara <caolanm@redhat.com> - 0.20081121-1
- latest version

* Thu Oct 16 2008 Caolán McNamara <caolanm@redhat.com> - 0.20081010-1
- latest version

* Wed Sep 10 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080905-1
- latest version

* Wed Nov 28 2007 Caolán McNamara <caolanm@redhat.com> - 0.20050503-1
- initial version
