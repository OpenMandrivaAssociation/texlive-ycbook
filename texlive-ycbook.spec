Name:		texlive-ycbook
Version:	46201
Release:	2
Summary:	A versatile book class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ycbook
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ycbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ycbook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is intended to be an interpretation of the mwbk
class which is a part of the mwcls package. The mwcls classes
are simple, yet powerful and customizable classes that allow
the end-user to customize the layout of headers, headings etc.
They also have the benefit of being more economic in space than
the most common LaTeX classes, while keeping a clear appearance
and a smooth flow.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ycbook
%doc %{_texmfdistdir}/doc/latex/ycbook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
