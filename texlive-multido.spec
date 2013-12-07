# revision 18302
# category Package
# catalog-ctan /macros/generic/multido
# catalog-date 2010-05-15 11:36:20 +0200
# catalog-license lppl
# catalog-version 1.42
Name:		texlive-multido
Version:	1.42
Release:	5
Summary:	A loop facility for Generic TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/multido
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multido.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multido.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multido.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.42-2
+ Revision: 754201
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.42-1
+ Revision: 719085
- texlive-multido
- texlive-multido
- texlive-multido
- texlive-multido

