Summary:	MailSync
Name:		mailsync
Version:	5.1.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
Patch0:		%{name}-assert.patch
URL:		http://mailsync.sourceforge.net/
BuildRequires:	imap-devel
#BuildRequires:	krb5-devel
#BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mailsync is a way of synchronizing a collection of mailboxes. The algorithm is
a 3-way diff. Two mailboxes are simultaneously compared to a record of the
state of both mailboxes at last sync. New messages and message deletions are
propagated between the two mailboxes. If you're familiar with CVS, it's the
same principle, except there's no opportunity for conflicts.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-openssl

%{__make} %{?parallelmkflags}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	-C src \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/mailsync.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO doc/ABSTRACT doc/examples/mailsync
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
