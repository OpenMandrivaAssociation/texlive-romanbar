# revision 25005
# category Package
# catalog-ctan /macros/latex/contrib/romanbar
# catalog-date 2012-01-02 20:05:40 +0100
# catalog-license lppl1.3
# catalog-version 1.0f
Name:		texlive-romanbar
Version:	1.0f
Release:	3
Summary:	Write roman number with "bars"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/romanbar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
'Bars', in the present context, are lines above and below text
that abut with the text. Barred roman numerals are sometimes
found in publications. The package provides a function that
prints barred roman numerals (converting arabic numerals if
necessary). The package also provides a predicate \ifnumeric.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/romanbar/romanbar.sty
%doc %{_texmfdistdir}/doc/latex/romanbar/README
%doc %{_texmfdistdir}/doc/latex/romanbar/romanbar-example.pdf
%doc %{_texmfdistdir}/doc/latex/romanbar/romanbar-example.tex
%doc %{_texmfdistdir}/doc/latex/romanbar/romanbar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/romanbar/romanbar.drv
%doc %{_texmfdistdir}/source/latex/romanbar/romanbar.dtx
%doc %{_texmfdistdir}/source/latex/romanbar/romanbar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
