Name:		texlive-multido
Version:	18302
Release:	2
Summary:	A loop facility for Generic TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/multido
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multido.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multido.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multido.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the \multido command, which was originally
designed for use with with PSTricks. Fixed-point arithmetic is
used when working on the loop variable, so that the package is
equally applicable in graphics applications like PSTricks as it
is with the more common integer loops.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/multido/multido.tex
%{_texmfdistdir}/tex/latex/multido/multido.sty
%doc %{_texmfdistdir}/doc/generic/multido/Changes
%doc %{_texmfdistdir}/doc/generic/multido/multido-doc.pdf
%doc %{_texmfdistdir}/doc/generic/multido/multido-doc.tex
%doc %{_texmfdistdir}/doc/generic/multido/multido.pdf
#- source
%doc %{_texmfdistdir}/source/generic/multido/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
