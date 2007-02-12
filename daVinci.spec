Summary:	daVinci is a universal, generic visualization system
Summary(pl.UTF-8):	Uniwersalny, ogólny system wizualizacji
Name:		daVinci
Version:	2.1
Release:	2
License:	free of charge for non-profit or internal use
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.tzi.de/tzi/biss/daVinci/%{name}_V%{version}_Linux_RedHat5.tar.gz
# Source0-md5:	526fd8b372179612cb1d4eb33aa435aa
#Source1:	%{name}.desktop
URL:		http://www.tzi.de/~davinci/daVinci_get_daVinci.html
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		pkghome		%{_libdir}/daVinci_V2.1

%description
daVinci is a universal, generic visualization system for automatic
generation of high-quality drawings of directed graphs. Graphs are
frequently used in computer applications as a general data structure
to represent objects and relationships between them. They are used to
implement hierarchies, dependency structures, networks,
configurations, dataflows, and so on. In despite of this manifold
demand, techniques to visualize such graphs are not common in today's
computer applications. So frequently a user has to deal with
uncomfortable textual interfaces or poor ad-hoc drawings of graphs,
because high-quality graph layout is difficult to implement and
reusable tools for graph visualization are often hard to find.

%description -l pl.UTF-8
daVinci jest uniwersalnym, ogólnym systemem wizualizacji służącym do
automatycznego tworzenia wysokiej jakości rysunków grafów skierowanych. 
W aplikacjach komputerowych często używa się grafów jako ogólnej struktury 
danych, reprezentującej obiekty oraz związki między nimi. Używa się ich do 
implementacji hierarchii, struktur zależności, sieci, konfiguracji, 
przepływu danych itd. Mimo wielorakiego zapotrzebowania, w dzisiejszych 
aplikacjach wciąż brakuje technik służących wizualizacji takich grafów. 
Często więc użytkownik musi posługiwać się niewygodnymi interfejsami 
tekstowymi lub prowizorycznymi rysunkami grafów, ponieważ trudno 
zaimplementować wysokiej jakości układ grafów i trudno znaleźć narzędzia 
do wizualizacji grafów nadających się do wielokrotnego wykorzystania.

%prep
%setup -q -n daVinci_V2.1
chmod -R a+w *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Graphics,/etc/profile.d,%{pkghome}}
cp -r * $RPM_BUILD_ROOT%{pkghome}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf %{pkghome}/daVinci .

cat > $RPM_BUILD_ROOT/etc/profile.d/%{name}.csh <<EOF
setenv DAVINCIHOME %{pkghome}
EOF

cat >$RPM_BUILD_ROOT/etc/profile.d/daVinci.sh <<EOF2
export DAVINCIHOME=%{pkghome}
EOF2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/daVinci
%dir %{pkghome}
%{pkghome}/[B-R]*
%attr(755,root,root) %{pkghome}/daVinci
%{pkghome}/api
%docdir %{pkghome}/docs
%{pkghome}/docs
%{pkghome}/example_graphs
%dir %{pkghome}/grapheditor
%{pkghome}/grapheditor/README
%attr(755,root,root) %{pkghome}/grapheditor/grapheditor
%{pkghome}/icons
%{pkghome}/lib
%dir %{pkghome}/tools
%{pkghome}/tools/README
%attr(755,root,root) %{pkghome}/tools/*term
#%%{_applnkdir}/Graphics/daVinci.desktop
%attr(755,root,root) /etc/profile.d/daVinci.sh
%attr(755,root,root) /etc/profile.d/daVinci.csh
