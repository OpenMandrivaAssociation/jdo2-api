%{?_javapackages_macros:%_javapackages_macros}

Name:          jdo2-api
Version:       2.2
Release:       6.3
Summary:       Implementation of JSR 243: Java Data Objects 2.0
Group:		Development/Java
License:       ASL 2.0
Url:           http://db.apache.org/jdo/
Source0:       http://svn.apache.org/repos/asf/db/jdo/releases/2.2/dist/db/jdo/2.2/jdo2-api-2.2-src.tar.gz
Source1:       jdo2-api-2.2-build.xml
# changed javax.transaction transaction-api 1.1 with geronimo-jta_1.1_spec
# fix pom version
Source2:       http://repo1.maven.org/maven2/javax/jdo/jdo2-api/2.2/jdo2-api-2.2.pom

Patch0:        jdo2-api-2.2-pom.patch
BuildRequires: jpackage-utils
BuildRequires: java-devel

BuildRequires: ant
BuildRequires: geronimo-jpa
BuildRequires: geronimo-jta
BuildRequires: junit

Requires:      ant
Requires:      geronimo-jpa
Requires:      geronimo-jta
Requires:      junit

Requires:      jpackage-utils
Requires:      java
BuildArch:     noarch

%description
The Java Data Objects 2 (JDO) API is a standard interface-based 
Java model abstraction of persistence, developed as Java Specification 
Request 243 under the auspices of the Java Community Process.

%package javadoc

Summary:       API documentation for %{name}
Requires:      jpackage-utils

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
cd %{name}-%{version}
cp -p %{SOURCE1} build.xml
cp -p %{SOURCE2} pom.xml
%patch0 -p0

%build
cd %{name}-%{version}
%ant jar javadoc

%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_javadir}
install -pm 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr  dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%files -f %{name}-%{version}/.mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt
