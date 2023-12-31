%global tessdata_version 4.0.0

Name:          tesseract
Version:       4.1.1
Release:       2%{?dist}
Summary:       Raw OCR Engine

License:       ASL 2.0
URL:           https://github.com/tesseract-ocr/%{name}
Source0:       https://github.com/tesseract-ocr/tesseract/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       https://github.com/tesseract-ocr/tessdata/archive/%{tessdata_version}/tessdata-%{tessdata_version}.tar.gz

# Tweak location of tessdata folder
Patch0:        tesseract_datadir.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libtiff-devel
BuildRequires: leptonica-devel
BuildRequires: cairo-devel
BuildRequires: libicu-devel
BuildRequires: pango-devel
BuildRequires: automake libtool
# Required for building manpages
BuildRequires: asciidoc libxslt


%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.


%package osd
Summary:       Orientation & Script Detection Data for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description osd
Orientation & Script Detection Data for %{name}

# define lang_subpkg macro
# m: 3 letter macrolanguage code
# l: langcode used in Provides and Supplements tags
# n: language name
# -m and -n is needed for subpackages, -l is optional
#
%define lang_subpkg(l:m:n:) \
%define macrolang %{-m:%{-m*}}%{!-m:%{error:3 letter Language code not defined}} \
%define langcode %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package langpack-%{macrolang}\
Summary:       %{langname} language data for %{name}\
BuildArch:     noarch\
Requires:      %{name} = %{version}-%{release}\
%{-l:Provides:      %{name}-langpack-%{langcode} = %{version}-%{release}\
Supplements:   (%{name} = %{version}-%{release} and langpacks-%{langcode})}\
\
%description langpack-%{macrolang}\
%{langname} language data for %{name}.\
\
%files langpack-%{macrolang}\
%{_datadir}/%{name}/tessdata/%{macrolang}.*

# define script_subpkg macro
# s: script name
# n: package name
#
%define script_subpkg(s:n:) \
%define scriptname %{-s:%{-s*}}%{!-s:%{error:Script name defined}} \
%define filename %{-n:%{-n*}}%{!-n:%{error:Package name not defined}} \
%define pkgname %(echo %filename | tr '[:upper:]' '[:lower:]') \
\
%package -n script-%{pkgname}\
Summary:       %{scriptname} script data for %{name}\
BuildArch:     noarch\
Requires:      %{name} = %{version}-%{release}\
\
%description -n script-%{pkgname}\
This package contains the fast integer version of the %{scriptname} script \
trained models for the Tesseract Open Source OCR Engine.\
\
%files -n script-%{pkgname}\
%dir %{_datadir}/tesseract/tessdata/script/\
%{_datadir}/tesseract/tessdata/script/%{filename}.*

# see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# and https://en.wikipedia.org/wiki/ISO_639_macrolanguage
%lang_subpkg -m afr -l af -n Afrikaans
%lang_subpkg -m amh -l an -n Amharic
%lang_subpkg -m ara -l ar -n Arabic
%lang_subpkg -m asm -l as -n Assamese
%lang_subpkg -m aze -l az -n Azerbaijani
%lang_subpkg -m aze_cyrl -n %{quote:Azerbaijani (Cyrilic)}
%lang_subpkg -m bel -l bel -n Belarusian
%lang_subpkg -m ben -l bn -n Bengali
%lang_subpkg -m bod -l bo -n %{quote:Tibetan (Standard)}
%lang_subpkg -m bos -l bs -n Bosnian
%lang_subpkg -m bre -l br -n Breton
%lang_subpkg -m bul -l bg -n Bulgarian
%lang_subpkg -m cat -l ca -n Catalan
%lang_subpkg -m ceb -n Cebuano
%lang_subpkg -m ces -l cs -n Czech
%lang_subpkg -m chi_sim -l zh_CN -n %{quote:Chinese (Simplified)}
%lang_subpkg -m chi_sim_vert -l zh_CN -n %{quote:Chinese (Simplified, Vertical)}
%lang_subpkg -m chi_tra -l zh_TW -n %{quote:Chinese (Traditional)}
%lang_subpkg -m chi_tra_vert -l zh_TW -n %{quote:Chinese (Traditional, Vertical)}
%lang_subpkg -m chr -n Cherokee
%lang_subpkg -m cos -l co -n Corsican
%lang_subpkg -m cym -l cy -n Welsh
%lang_subpkg -m dan -l da -n Danish
%lang_subpkg -m dan_frak -n %{quote:Danish (Fraktur)}
%lang_subpkg -m deu -l de -n German
%lang_subpkg -m deu_frak -n %{quote:German (Fraktur)}
%lang_subpkg -m div -l dv -n %{quote:Dhivehi; Maldivian}
%lang_subpkg -m dzo -n Dzongkha
%lang_subpkg -m ell -l el -n Greek
%lang_subpkg -m enm -n %{quote:Middle English (1100-1500)}
%lang_subpkg -m epo -l eo -n Esperanto
%lang_subpkg -m equ -n %{quote:Math / equation}
%lang_subpkg -m est -l et -n Estonian
%lang_subpkg -m eus -l eu -n Basque
%lang_subpkg -m fao -l fo -n Faroese
%lang_subpkg -m fas -l fa -n %{quote:Persian (Farsi)}
%lang_subpkg -m fil -n %{quote:Filipino; Pilipino}
%lang_subpkg -m fin -l fi -n Finnish
%lang_subpkg -m fra -l fr -n French
%lang_subpkg -m frk -n Fraktur
%lang_subpkg -m frm -n %{quote:Middle French (ca. 1400-1600)}
%lang_subpkg -m fry -l fy -n %{quote:Western Frisian}
%lang_subpkg -m gla -l gd -n %{quote:Gaelic; Scottish Gaelic}
%lang_subpkg -m gle -l ga -n Irish
%lang_subpkg -m glg -l gl -n Galician
%lang_subpkg -m grc -n %{quote:Ancient Greek}
%lang_subpkg -m guj -l gu -n Gujarati
%lang_subpkg -m hat -l ht -n Haitian
%lang_subpkg -m heb -l he -n Hebrew
%lang_subpkg -m hin -l hi -n Hindi
%lang_subpkg -m hrv -l hr -n Croatian
%lang_subpkg -m hun -l hu -n Hungarian
%lang_subpkg -m hye -l hy -n Armenian
%lang_subpkg -m iku -l iu -n Inuktitut
%lang_subpkg -m ind -l id -n Indonesian
%lang_subpkg -m isl -l is -n Icelandic
%lang_subpkg -m ita -l it -n Italian
%lang_subpkg -m ita_old -n %{quote:Italian (Old)}
%lang_subpkg -m jav -l jav -n Javanese
%lang_subpkg -m jpn -l ja -n Japanese
%lang_subpkg -m jpn_vert -l ja -n %{quote:Japanese (Vertical)}
%lang_subpkg -m kan -l kn -n Kannada
%lang_subpkg -m kat -l ka -n Georgian
%lang_subpkg -m kat_old -n %{quote:Georgian (Old)}
%lang_subpkg -m kaz -l kk -n Kazakh
%lang_subpkg -m khm -l km -n Khmer
%lang_subpkg -m kir -l ky -n Kyrgyz
%lang_subpkg -m kor -l ko -n Korean
%lang_subpkg -m kor_vert -l ko -n %{quote:Korean (Vertical)}
%lang_subpkg -m kur -l ku -n Kurdish
%lang_subpkg -m kur_ara -l ku -n %{quote:Kurdish (Arabic)}
%lang_subpkg -m lao -l lo -n Lao
%lang_subpkg -m lat -l lat -n Latin
%lang_subpkg -m lav -l lv -n Latvian
%lang_subpkg -m lit -l lt -n Lithuanian
%lang_subpkg -m ltz -l lb -n Luxembourgish
%lang_subpkg -m mal -l ml -n Malayalam
%lang_subpkg -m mar -l mr -n Marathi
%lang_subpkg -m mkd -l mk -n Macedonian
%lang_subpkg -m mlt -l mt -n Maltese
%lang_subpkg -m mon -l mn -n Mongolian
%lang_subpkg -m mri -l mi -n Maori
%lang_subpkg -m msa -l ms -n Malay
%lang_subpkg -m mya -l my -n Burmese
%lang_subpkg -m nep -l ne -n Nepali
%lang_subpkg -m nld -l nl -n Dutch
%lang_subpkg -m nor -l no -n Norwegian
%lang_subpkg -m oci -l oc -n Occitan
%lang_subpkg -m ori -l or -n Oriya
%lang_subpkg -m pan -l pa -n Panjabi
%lang_subpkg -m pol -l pl -n Polish
%lang_subpkg -m por -l pt -n Portuguese
%lang_subpkg -m pus -l ps -n Pashto
%lang_subpkg -m que -l qu -n Quechuan
%lang_subpkg -m ron -l ro -n Romanian
%lang_subpkg -m rus -l ru -n Russian
%lang_subpkg -m san -l sa -n Sanskrit
%lang_subpkg -m sin -l si -n Sinhala
%lang_subpkg -m slk -l sk -n Slovakian
%lang_subpkg -m slk_frak -n %{quote:Slovakian (Fraktur)}
%lang_subpkg -m slv -l sl -n Slovenian
%lang_subpkg -m snd -l sd -n Sindhi
%lang_subpkg -m spa -l es -n Spanish
%lang_subpkg -m spa_old -n %{quote:Spanish (Old)}
%lang_subpkg -m sqi -l sq -n Albanian
%lang_subpkg -m srp -l sr -n Serbian
%lang_subpkg -m srp_latn -n %{quote:Serbian (Latin)}
%lang_subpkg -m sun -l su -n Sundanese
%lang_subpkg -m swa -l sw -n Swahili
%lang_subpkg -m swe -l sv -n Swedish
%lang_subpkg -m syr -l ar_SY -n Syriac
%lang_subpkg -m tam -l ta -n Tamil
%lang_subpkg -m tat -l tt -n Tatar
%lang_subpkg -m tel -l te -n Telugu
%lang_subpkg -m tgk -l tg -n Tajik
%lang_subpkg -m tgl -l tl -n Tagalog
%lang_subpkg -m tha -l th -n Thai
%lang_subpkg -m tir -l ti -n Tigrinya
%lang_subpkg -m ton -l to -n Tongan
%lang_subpkg -m tur -l tr -n Turkish
%lang_subpkg -m uig -l ug -n Uyghur
%lang_subpkg -m ukr -l uk -n Ukrainian
%lang_subpkg -m urd -l ur -n Urdu
%lang_subpkg -m uzb -l uz -n Uzbek
%lang_subpkg -m uzb_cyrl -n %{quote:Uzbek (Cyrillic)}
%lang_subpkg -m vie -l vi -n Vietnamese
%lang_subpkg -m yid -l yi -n Yiddish
%lang_subpkg -m yor -l yo -n Yoruba

%script_subpkg -n Arabic -s Arabic
%script_subpkg -n Armenian -s Armenian
%script_subpkg -n Bengali -s Bengali
%script_subpkg -n Canadian_Aboriginal -s %{quote:Canadian (Aboriginal)}
%script_subpkg -n Cherokee -s Cherokee
%script_subpkg -n Cyrillic -s Cyrillic
%script_subpkg -n Devanagari -s Devanagari
%script_subpkg -n Ethiopic -s Ethiopic
%script_subpkg -n Fraktur -s Fraktur
%script_subpkg -n Georgian -s Georgian
%script_subpkg -n Greek -s Greek
%script_subpkg -n Gujarati -s Gujarati
%script_subpkg -n Gurmukhi -s Gurmukhi
%script_subpkg -n HanS -s %{quote:Han (Simplified)}
%script_subpkg -n HanS_vert -s %{quote:Han (Simplified, Vertical)}
%script_subpkg -n HanT -s %{quote:Han (Traditional)}
%script_subpkg -n HanT_vert -s %{quote:Han (Traditional, Vertical)}
%script_subpkg -n Hangul -s Hangul
%script_subpkg -n Hangul_vert -s %{quote:Hangul (Vertical)}
%script_subpkg -n Hebrew -s Hebrew
%script_subpkg -n Japanese -s Japanese
%script_subpkg -n Japanese_vert -s %{quote:Japanese (Vertical)}
%script_subpkg -n Kannada -s Kannada
%script_subpkg -n Khmer -s Khmer
%script_subpkg -n Lao -s Lao
%script_subpkg -n Latin -s Latin
%script_subpkg -n Malayalam -s Malayalam
%script_subpkg -n Myanmar -s Myanmar
%script_subpkg -n Oriya -s Oriya
%script_subpkg -n Sinhala -s Sinhala
%script_subpkg -n Syriac -s Syriac
%script_subpkg -n Tamil -s Tamil
%script_subpkg -n Telugu -s Telugu
%script_subpkg -n Thaana -s Thaana
%script_subpkg -n Thai -s Thai
%script_subpkg -n Tibetan -s Tibetan
%script_subpkg -n Vietnamese -s Vietnamese


%prep
%setup -q -n %{name}-%{version} -a1
%patch0 -p1


%build
autoreconf -ifv
%configure --disable-static

%make_build
%make_build training


%install
%make_install
%make_install training-install

find %{buildroot}%{_libdir} -type f -name '*.la' -delete

cp -av tessdata-%{tessdata_version}/* %{buildroot}%{_datadir}/%{name}/tessdata


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/ambiguous_words
%{_bindir}/classifier_tester
%{_bindir}/combine_lang_model
%{_bindir}/combine_tessdata
%{_bindir}/dawg2wordlist
%{_bindir}/language-specific.sh
%{_bindir}/lstmeval
%{_bindir}/merge_unicharsets
%{_bindir}/set_unicharset_properties
%{_bindir}/shapeclustering
%{_bindir}/tesstrain.sh
%{_bindir}/tesstrain_utils.sh
%{_bindir}/*training
%{_bindir}/%{name}
%{_bindir}/text2image
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tessdata
%{_datadir}/%{name}/tessdata/configs/
%{_datadir}/%{name}/tessdata/tessconfigs/
%{_datadir}/%{name}/tessdata/COPYING
%{_datadir}/%{name}/tessdata/README.md
%{_datadir}/%{name}/tessdata/eng.*
%{_datadir}/%{name}/tessdata/pdf.ttf
%{_libdir}/lib%{name}*.so.4*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%files osd
%{_datadir}/%{name}/tessdata/osd.traineddata


%changelog
* Fri Aug 06 2021 Jiri Kucera <jkucera@redhat.com> - 4.1.1-2
- Fix subpackages deps
  Related: #1826085

* Thu Aug 05 2021 Jiri Kucera <jkucera@redhat.com> - 4.1.1-1
- Rebase to 4.1.1
  Related: #1826085

* Thu Jul 01 2021 Jiri Kucera <jkucera@redhat.com> - 3.05.01-7
- Rebuild
  Resolves: #1826085

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.coM> - 3.05.01-6
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.05.01-4
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 3.05.01-1
- Update to 3.05.01

* Tue Feb 21 2017 Sandro Mani <manisandro@gmail.com> - 3.05.00-1
- Update to 3.05.00

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 3.04.01-3
- Rebuild (to fix behaviour on big-endian arches after leptonica endianness fix)

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.04.01-2
- rebuild for ICU 57.1

* Fri Feb 19 2016 Sandro Mani <manisandro@gmail.com> - 3.04.01-1
- Update to 3.04.01

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.04.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 3.04.00-5
- Rebuild (leptonica)

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 3.04.00-4
- Rebuild (leptonica)

* Mon Jan 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.04.00-3
- Added virtual provides to follow langpacks naming guidelines
- Added Supplements tag for new way of langpacks installation

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 3.04.00-2
- rebuild for ICU 56.1

* Sat Sep 12 2015 Sandro Mani <manisandro@gmail.com> - 3.04.00-1
- Update to 3.04.00

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.03-0.5.rc1
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 3.03-0.4.rc1
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 3.03-0.3.rc1
- rebuild for ICU 53.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Sandro Mani <manisandro@gmail.com> - 3.03-0.1.rc1
- Update to v3.03-rc1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Karol Trzcionka <karlik at fedoraproject.org> - 3.02.02-3
- Fix rhbz#1037350 (-Werror=format-security)
- Add OSD data
- Remove BuildRoot tag

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Karol Trzcionka <karlik at fedoraproject.org> - 3.02.02-1
- Update to v3.02.02
- Apply pkgconfig patch rhbz#904806

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Karol Trzcionka <karlik at fedoraproject.org> - 3.01-1
- Update to v3.01
- Add manual pages
- Add BRs leptonica, automake

* Tue Jul 31 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.00-6
- Fix FTBFS with g++ 4.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Karol Trzcionka <karlikt at gmail.com> - 3.00-1
- Update to v3.00
- Remove static libs and add dynamic

* Wed Oct 21 2009 Karol Trzcionka <karlikt at gmail.com> - 2.04-1
- Update to v2.04
- Add static libraries to -devel subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 2.03-3
- include stdio.h for snprintf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May 04 2008 Karol Trzcionka <karlikt at gmail.com> - 2.03-1
- Update to v2.03
* Sat Feb 09 2008 Karol Trzcionka <karlikt at gmail.com> - 2.01-2
- Rebuild for gcc43
* Fri Sep 07 2007 Karol Trzcionka <karlikt at gmail.com> - 2.01-1
- Upgrade to v2.01
* Tue Aug 21 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-1
- Upgrade to v2.00
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.04-1
- Change url and source
- Update to v1.04
- Make patch bases on upstream's v1.04b
- Change compilefix patch
- Adding -devel subpackage
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-2
- Including patch bases on cvs
* Tue Feb 13 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-1
- Update to v1.03
* Sat Jan 27 2007 Karol Trzcionka <karlikt at gmail.com> - 1.02-3
- Update BRs
- Fix x86_64 compile
* Sat Dec 30 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-2
- Fixed rpmlint warning in SRPM
* Fri Dec 29 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-1
- Initial Release
