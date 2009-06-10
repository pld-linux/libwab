Summary:	Tool to read Windows address book files
Summary(pl.UTF-8):	Narzędzie do odczytu plików książek adresowych Windows
Name:		libwab
Version:	061227
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
Express). Simply run it on a .wab file and it should dump the file in
LDIF format (a nice ASCII format used in LDAP).

Used in heuristic mode libwab can often recover deleted contacts and
contacts from damaged files.

%description -l pl.UTF-8
libwab to małe narzędzie linii poleceń, które można wykorzystać do
eksportu adresów z książki adresowej Windows (używanej przez program
Microsoft Outlook Express).  Wystarczy uruchomić je na pliku .wab, a
powinno utworzyć plik zrzutu w formacie LDIF (przyjemnym formacie
ASCII używanym w LDAP).

Użyte w trybie heurystycznym zwykle potrafi odzyskać usunięte kontakty
oraz kontakty z uszkodzonych plików.

%prep
%setup -q -n %{name}-060901

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
