Summary: daVinci is a universal, generic visualization system for automatic generation of high-quality drawings of directed graphs.
Name: daVinci
Version: 2.1
Release: 1


URL: http://www.tzi.de/~davinci/daVinci_get_daVinci.html
Copyright: daVinci is licensed free of charge for non-profit or internal use.
Group: X11/Applications/Graphics


Source0: daVinci_V2.1_Linux_RedHat5.tar.gz
Source1: daVinci.csh
Source2: daVinci.sh
Source3: daVinci.wmconfig
ExclusiveArch: i386
BuildRoot:	/tmp/%{name}-%{version}-root
Packager: Andrea Borgia <borgia@cs.unibo.it>


%description
daVinci is a universal, generic visualization system for automatic generation
of high-quality drawings of directed graphs. Graphs are frequently used in
computer applications as a general data structure to represent objects and
relationships between them. They are used to implement hierarchies,
dependency structures, networks, configurations, dataflows, and so on. In
despite of this manifold demand, techniques to visualize such graphs are not
common in today's computer applications. So frequently a user has to deal
with uncomfortable textual interfaces or poor ad-hoc drawings of graphs,
because high-quality graph layout is difficult to implement and reusable
tools for graph visualization are often hard to find. 

%description -l pl
daVinci jest uniwersalnym, ogólnym systemem wizualizacji s³u¿±cym do 
automatycznego tworzenia wysokiej jako¶ci rysunków grafów skierowanych.
W aplikacjach komputerowych czêsto u¿ywa siê grafów jako ogólnej struktury 
danych, reprezentuj±cej obiekty oraz zwi±zki miêdzy nimi. Uzywa siê ich
do implementacji hierarchii, struktur zalezno¶ci, sieci, konfiguracji,
przep³ywu danych itd. Mimo wielorakiego zapotzrebowania, w dzisiejszych
aplikacjach wci±¿ brakuje technik s³u¿±cych wizualizacji takich grafów. 
Czêsto wiêc u¿ytkownik musi pos³ugiwaæ siê niewygodnymi interfejsami 
tekstowymi lub prowizorycznymi rysunkami grafów, poniewa¿ trudno
zaimplemetowaæ wysokiej jako¶ci uk³ad grafów i trudno znale¼æ narzêdzia 
do wizualizacji grafów nadaj±cych siê do wielokrotnego wykorzystania.

%prep
%setup -n daVinci_V2.1


%install
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/daVinci_V2.1
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cp -r * $RPM_BUILD_ROOT/usr/local/daVinci_V2.1
cp $RPM_SOURCE_DIR/daVinci.sh $RPM_BUILD_ROOT/etc/profile.d/daVinci.sh
cp $RPM_SOURCE_DIR/daVinci.csh $RPM_BUILD_ROOT/etc/profile.d/daVinci.csh
cp $RPM_SOURCE_DIR/daVinci.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/daVinci
cd $RPM_BUILD_ROOT/usr/X11R6/bin
ln -s ../../local/daVinci_V2.1/daVinci


%clean
rm -rf * $RPM_BUILD_ROOT


%files
%attr(-,root,root) /usr/X11R6/bin/daVinci
%attr(-,root,root) /usr/local/daVinci_V2.1
%attr(-,root,root) /etc/X11/wmconfig/daVinci
%attr(-,root,root) /etc/profile.d/daVinci.sh
%attr(-,root,root) /etc/profile.d/daVinci.csh
