%global tl_name asy-overview
%global tl_revision 72484

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A brief overview of the Asymptote language for drawing mathematical graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/asy-overview
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asy-overview.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asy-overview.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Asymptote is a programming language for creating mathematical graphics.
This document gives you a quick overview, illustrating with a few
familiar Calculus examples. Readers can work through it in a couple of
hours to get a feel for the system's strengths, and if they are
interested then go on to a full tutorial or the official reference.

