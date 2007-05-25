#
Summary:	Tool to read windows address book filesd
Name:		libwab
Version:	060901
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://lilith.tec-man.com/libwab/files/%{name}-060901.tar.gz
# Source0-md5:	82c333cb5f737a100c9a431d920dbd5f
URL:		http://lilith.tec-man.com/libwab/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwab is a little command line utility that you can use to export
your addresses from a Windows Address Book (used in Microsoft Outlook
Express). Simply compile and run it on a .wab file and it should dump
the file in ldif format (a nice ascii format used in ldap).

Used in heuristic mode libwab can often recover deleted contacts and
contacts from damaged files.

%prep
%setup -q

%build
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
%doc ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/wabread
