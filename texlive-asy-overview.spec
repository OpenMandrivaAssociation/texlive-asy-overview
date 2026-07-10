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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Asymptote is a programming language for creating mathematical graphics.
This document gives you a quick overview, illustrating with a few
familiar Calculus examples. Readers can work through it in a couple of
hours to get a feel for the system's strengths, and if they are
interested then go on to a full tutorial or the official reference.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/asy
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/asy_sty
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/appendix
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter1
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/cover
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/preface
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter1/asy
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2/asy
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3/asy
%dir %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4/asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/README
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/asy/jh.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/asy_overview.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/asy_sty/asy_tut.sty
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/asy_sty/colors.sty
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/Makefile
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/appendix/appendix.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/asy_tut.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter1/asy/unit_circle.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter1/asy/unit_circle_after.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter1/chapter1.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter1/main.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2/asy/cos.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2/asy/exponential.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2/asy/plot.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2/asy/plot_after.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter2/chapter2.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3/asy/integral.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3/asy/zoom.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3/asy/zoom_iterate.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3/asy/zoom_times.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter3/chapter3.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4/asy/planes.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4/asy/vectors.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4/asy/washer.asy
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4/chapter4.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/chapter4/main_3d.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/cover/cover.tex
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/cover/pp.jpg
%doc %{_datadir}/texmf-dist/doc/latex/asy-overview/src/preface/preface.tex
