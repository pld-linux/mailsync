Summary:	MailSync - synchronizing a collection of mailboxes
Summary(pl):	MailSync - synchronizacja zbioru skrzynek pocztowych
Name:		mailsync
Version:	5.1.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	11c099a94143b11b35ed3a0a9593e33a
Patch0:		%{name}-assert.patch
URL:		http://mailsync.sourceforge.net/
BuildRequires:	imap-devel
#BuildRequires:	krb5-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
#BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mailsync is a way of synchronizing a collection of mailboxes. The
algorithm is a 3-way diff. Two mailboxes are simultaneously compared
to a record of the state of both mailboxes at last sync. New messages
and message deletions are propagated between the two mailboxes. If
you're familiar with CVS, it's the same principle, except there's no
opportunity for conflicts.

%description -l pl
Mailsync to spos�b synchronizacji zbioru skrzynek pocztowych. Algorytm
to tr�jstronny diff. Dwie skrzynki s� jednocze�nie por�wnywane z
rekordem stanu dw�ch skrzynek po ostatniej synchronizacji. Nowe
wiadomo�ci i usuni�cia wiadomo�ci s� propagowane mi�dzy dwiema
skrzynkami. Dzia�a to na tej samej zasadzie co CVS, z wyj�tkiem tego,
�e nie wyst�puj� konflikty.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-openssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/mailsync.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO doc/ABSTRACT doc/examples/mailsync
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*