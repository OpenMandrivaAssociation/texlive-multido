# revision 18302
# category Package
# catalog-ctan /macros/generic/multido
# catalog-date 2010-05-15 11:36:20 +0200
# catalog-license lppl
# catalog-version 1.42
Name:		texlive-multido
Version:	1.42
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the \multido command, which was originally
designed for use with with PSTricks. Fixed-point arithmetic is
used when working on the loop variable, so that the package is
equally applicable in graphics applications like PSTricks as it
is with the more common integer loops.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
