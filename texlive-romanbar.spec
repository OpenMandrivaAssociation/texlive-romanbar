%global tl_name romanbar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0g
Release:	%{tl_revision}.1
Summary:	Write roman number with bars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/romanbar
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
'Bars', in the present context, are lines above and below text that abut
with the text. Barred roman numerals are sometimes found in
publications. The package provides a function that prints barred roman
numerals (converting arabic numerals if necessary). The package also
provides a predicate \ifnumeric.

