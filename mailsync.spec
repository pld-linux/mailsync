Summary:	MailSync - synchronizing a collection of mailboxes
Summary(pl):	MailSync - synchronizacja zbioru skrzynek pocztowych
Name:		mailsync
Version:	5.1.1
Release:	5
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	aa7f3983e38d66e00ab9231760751c75
Patch0:		%{name}-assert.patch
Patch1:		%{name}-imap2004_fix.patch
Patch2:		%{name}-amd64_fix.patch
URL:		http://mailsync.sourceforge.net/
BuildRequires:	imap-devel >= 2004
#BuildRequires:	krb5-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
#BuildRequires:	pam-devel
Requires:	imap-lib >= 2004
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mailsync is a way of synchronizing a collection of mailboxes. The
algorithm is a 3-way diff. Two mailboxes are simultaneously compared
to a record of the state of both mailboxes at last sync. New messages
and message deletions are propagated between the two mailboxes. If
you're familiar with CVS, it's the same principle, except there's no
opportunity for conflicts.

%description -l pl
Mailsync to sposób synchronizacji zbioru skrzynek pocztowych. Algorytm
to trójstronny diff. Dwie skrzynki s± jednocze¶nie porównywane z
rekordem stanu dwóch skrzynek po ostatniej synchronizacji. Nowe
wiadomo¶ci i usuniêcia wiadomo¶ci s± propagowane miêdzy dwiema
skrzynkami. Dzia³a to na tej samej zasadzie co CVS, z wyj±tkiem tego,
¿e nie wystêpuj± konflikty.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%ifarch amd64
%patch2 -p1
%endif

%build
./autogen.sh
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
