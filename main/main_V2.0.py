# Copyright (c) 2024-2025 Maxxj
# Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
#
# This script is free for non-commercial use.
# For commercial use, please contact xxjlyh3332@gmail.com.

import gradio as gr

def zzzzzz(isotherlan, author, maintitle, othertitle, type, otherauthor, version, location, publisher, publishtime, page):
    try:
        citation = []
        if not author or not maintitle or not type or not publishtime:
            print(5/0)
        citation.append(author + ". " + maintitle)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[" + type[:1] + "]. ")
        if otherauthor:
            citation.append(otherauthor + ". ")
        if version:
            citation.append(version + ". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime)
        if page:
            citation.append(":" + page)
        citation.append(".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段",duration=5)

def zzzzhbhyl(isotherlan,author, maintitle, othertitle, type, otherauthor, version, location, publisher,
              publishtime):
    try:
        citation = []
        if not author or not maintitle or not type or not publishtime:
            print(5/0)
        citation.append(author + ". " + maintitle)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[" + type[:1] + "]. ")
        if otherauthor:
            citation.append(otherauthor + ". ")
        if version:
            citation.append(version + ". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime+".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def zzzzdzzy(isotherlan,author, maintitle, othertitle, type, otherauthor, version, location, publisher, publishtime, page, date, url, doi):
    try:
        citation = []
        if not author or not maintitle or not type or not publishtime or not page or not date or not url:
            print(5/0)
        citation.append(author + ". " + maintitle)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[" + type[:1]+"/OL]. ")
        if otherauthor:
            citation.append(otherauthor + ". ")
        if version:
            citation.append(version + ". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime+":"+page+"[" + str(date)[:10] + "]. "+url + ".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def zzzzdzzyhbhyl(isotherlan,author, maintitle, othertitle, type, otherauthor, version, location, publisher,
              publishtime, date, url, doi):
    try:
        citation = []
        if not author or not maintitle or not type or not publishtime or not date or not url:
            print(5/0)
        citation.append(author + ". " + maintitle)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[" + type[:1] + "]. ")
        if otherauthor:
            citation.append(otherauthor + ". ")
        if version:
            citation.append(version + ". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime+"[" + str(date)[:10] + "]. "+url+".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def zzzzxcwxzzxcwx(isotherlan,author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version, location, publisher, publishtime, page):
    try:
        citation = []
        if not author or not title or not type or not bigauthor or not bigtitle or not publishtime or not page:
            print(5/0)
        citation.append(author + ". " + title + "[" + type[:1]+"]. ")
        if otherauthor:
            citation.append(otherauthor)
        citation.append("//" + bigauthor + ". " + bigtitle)
        if otherbigtitle:
            citation.append(":" + otherbigtitle)
        citation.append(". ")
        if version:
            citation.append(version + ". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime + ":" + page+".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def zzzzxcwxddzyxcwx(isotherlan,author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version, location, publisher, publishtime, page, date, url, doi):
    try:
        citation = []
        if not author or not title or not type or not bigauthor or not bigtitle or not publishtime or not page or not date or not url:
            print(5/0)
        citation.append(author + ". " + title + "[" + type[:1]+"/OL]. ")
        if otherauthor:
            citation.append(otherauthor)
        citation.append("//" + bigauthor + ". " + bigtitle)
        if otherbigtitle:
            citation.append(":" + otherbigtitle)
        citation.append(". ")
        if version:
            citation.append(version + ". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime + ":" + page + "[" + str(date)[:10] + "]. "+url + ".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def lxcbwlxcbwlxcbwqk(isotherlan,author, title, othertitle, year, juan, qi, year2, juan2, qi2, location, publisher, publishtime):
    try:
        citation = []
        if not author or not title or not year or not publishtime:
            print(5/0)
        citation.append(author + ". " + title)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[J]. "+year)
        if juan:
            citation.append("," + juan)
        if qi:
            citation.append("(" + qi + ")")
        citation.append("-")
        if year2:
            citation.append(year2)
        if juan2:
            citation.append("," + juan2)
        if qi2:
            citation.append("(" + qi2 + ")")
        citation.append(". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime+".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def lxcbwlxcbwdzzylxcbwqk(isotherlan,author, title, othertitle, year, juan, qi, year2, juan2, qi2, location, publisher, publishtime, date,url,doi):
    try:
        citation = []
        if not author or not title or not year or not publishtime or not date or not url:
            print(5/0)
        citation.append(author + ". " + title)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[J/OL]. "+year)
        if juan:
            citation.append("," + juan)
        if qi:
            citation.append("(" + qi + ")")
        citation.append("-")
        if year2:
            citation.append(year2)
        if juan2:
            citation.append("," + juan2)
        if qi2:
            citation.append("(" + qi2 + ")")
        citation.append(". ")
        if not location:
            if isotherlan:
                citation.append("[S.l.]")
            elif not isotherlan:
                citation.append("[出版地不详]:")
        else:
            citation.append(location + ":")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(publishtime + "[" + str(date)[:10] + "]. "+url + ".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def lxcbwlxcbwxcwxlxcbwxcwxqk(author, title, rapidtitle, otherrapidtitle, year, juan, qi, page):
    try:
        citation = []
        if not author or not title or not rapidtitle or not year or not juan or not qi or not page:
            print(5/0)
        citation.append(author + ". " + title + "[J]. "+ rapidtitle)
        if otherrapidtitle:
            citation.append(":" + otherrapidtitle)
        citation.append("," + year+"," + juan+"(" + qi + "):"+page + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)
def lxcbwlxcbwxcwxlxcbwxcwxbz(isotherlan,author, title, publisher, publishdate, banci):
    try:
        citation = []
        if not author or not title or not publishdate or not banci:
            print(5/0)
        citation.append(author + ". " + title + "[N]. ")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(str(publishdate)[:10] + "("+ banci + ").")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def lxcbwlxcbwxcwxdzzylxcbwxcwxqk(author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, date,url,doi):
    try:
        citation = []
        if not author or not title or not rapidtitle or not year or not juan or not qi or not page or not date or not url:
            print(5/0)
        citation.append(author + ". " + title + "[J/OL]. "+ rapidtitle)
        if otherrapidtitle:
            citation.append(":" + otherrapidtitle)
        citation.append("," + year+"," + juan+"(" + qi + "):"+page + "[" + str(date)[:10] + "]. "+url+".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def lxcbwlxcbwxcwxdzzylxcbwxcwxbz(isotherlan,author, title, publisher, publishdate, banci, date, url,doi):
    try:
        citation = []
        if not author or not title or not publishdate or not banci or not date or not url:
            print(5/0)
        citation.append(author + ". " + title + "[N]. ")
        if not publisher:
            if isotherlan:
                citation.append("[s.n.],")
            elif not isotherlan:
                citation.append("[出版者不详],")
        else:
            citation.append(publisher + ",")
        citation.append(str(publishdate)[:10] + "("+ banci + ")["+str(date)[:10]+"]. "+url+".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def zlwxzlwx(author, title, num, publictime):
    try:
        citation = []
        if not author or not title or not num or not publictime:
            print(5/0)
        citation.append(author + ". " + title + ":" + num + "[P]. " + str(publictime)[:10] + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def zlwxdzzyzlwx(author, title, num, publictime, date, url, doi):
    try:
        citation = []
        if not author or not title or not num or not publictime or not date or not url:
            print(5/0)
        citation.append(author + ". " + title + ":" + num + "[P/OL]. "+ str(publictime)[:10] + "[" + str(date)[:10] + "]. "+url+".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def dzgg(author, maintitle, othertitle, changetime, date, url, doi):
    try:
        citation = []
        if not author or not maintitle or not date or not url:
            print(5/0)
        citation.append(author + ". " + maintitle)
        if othertitle:
            citation.append(":" + othertitle)
        citation.append("[EB/OL]. ")
        if changetime:
            citation.append("(" + str(changetime)[:10] + ")")
        citation.append("[" + str(date)[:10] + "]. "+url + ".")
        if doi:
            citation.append(" DOI:" + doi + ".")
        gr.Info(message="参考文献生成完毕", duration=3)
        return ''.join(citation)
    except Exception:
        raise gr.Error(message="请填写所有除“可选”外的字段", duration=5)

def clear_all_5():
    return [""] *5

def clear_all_7():
    return [""] *7

def clear_all_8():
    return [""] *8

def clear_all_9():
    return [""] *9

def clear_all_10():
    return [""] * 10

def clear_all_11():
    return [""] * 11

def clear_all_12():
    return [""] * 12

def clear_all_14():
    return [""] * 14

def clear_all_15():
    return [""] * 15

def clear_all_17():
    return [""] * 17

theme = gr.themes.Ocean(
    primary_hue="amber",
    secondary_hue="cyan",
    neutral_hue="gray",
    text_size="sm",
)

copyright_html = """
<div style="text-align: center; padding-top: 0px; margin-top: 0px;">
    <p style="font-size: 1em; color: grey; margin-top: 0; margin-bottom: 0;">
        Copyright © 2024-2025 Maxxj. All rights reserved
        (licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer" style="color: grey; text-decoration: underline;">CC BY-NC-SA 4.0</a>).
        Exact legal code is in the sidebar.
    </p>
</div>
"""

ccbyncsa="""
Attribution-NonCommercial-ShareAlike 4.0 International

===============================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees

===============================================================

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
Public License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International Public License
("Public License"). To the extent this Public License may be
interpreted as a contract, You are granted the Licensed Rights in
consideration of Your acceptance of these terms and conditions, and the
Licensor grants You such rights in consideration of benefits the
Licensor receives from making the Licensed Material available under
these terms and conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. BY-NC-SA Compatible License means a license listed at
     creativecommons.org/compatiblelicenses, approved by Creative
     Commons as essentially the equivalent of this Public License.

  d. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  e. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  f. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  g. License Elements means the license attributes listed in the name
     of a Creative Commons Public License. The License Elements of this
     Public License are Attribution, NonCommercial, and ShareAlike.

  h. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  i. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  j. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  k. NonCommercial means not primarily intended for or directed towards
     commercial advantage or monetary compensation. For purposes of
     this Public License, the exchange of the Licensed Material for
     other material subject to Copyright and Similar Rights by digital
     file-sharing or similar means is NonCommercial provided there is
     no payment of monetary compensation in connection with the
     exchange.

  l. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  m. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  n. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part, for NonCommercial purposes only; and

            b. produce, reproduce, and Share Adapted Material for
               NonCommercial purposes only.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. Additional offer from the Licensor -- Adapted Material.
               Every recipient of Adapted Material from You
               automatically receives an offer from the Licensor to
               exercise the Licensed Rights in the Adapted Material
               under the conditions of the Adapter's License You apply.

            c. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties, including when
          the Licensed Material is used other than for NonCommercial
          purposes.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.
       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

  b. ShareAlike.

     In addition to the conditions in Section 3(a), if You Share
     Adapted Material You produce, the following conditions also apply.

       1. The Adapter's License You apply must be a Creative Commons
          license with the same License Elements, this version or
          later, or a BY-NC-SA Compatible License.

       2. You must include the text of, or the URI or hyperlink to, the
          Adapter's License You apply. You may satisfy this condition
          in any reasonable manner based on the medium, means, and
          context in which You Share Adapted Material.

       3. You may not offer or impose any additional or different terms
          or conditions on, or apply any Effective Technological
          Measures to, Adapted Material that restrict exercise of the
          rights granted under the Adapter's License You apply.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database for NonCommercial purposes
     only;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material,
     including for purposes of Section 3(b); and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE.md OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.

===============================================================

Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.

Creative Commons may be contacted at creativecommons.org.
"""

with gr.Blocks(title="GB/T 7714-2015参考文献生成器",fill_width=True,theme=theme) as demo:
    gr.Markdown('''
# GB/T 7714-2015参考文献生成器V2.0
### Created by Maxxj
使用本软件即视为同意采用CC BY-NC-SA 4.0许可证，详细条文请参照左侧侧边栏；本生成器生成结果仅供参考。
    ''')
    with gr.Sidebar(open=False, width=560):
        gr.Markdown("## GB/T 7714-2015 信息与文献参考文献著录规则")
        gr.Gallery(value=[
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-01.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-03.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-04.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-05.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-07.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-08.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-09.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-10.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-11.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-12.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-13.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-14.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-15.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-16.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-17.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-18.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-19.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-20.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-21.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-22.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-23.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-24.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-25.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-26.png",
            "./pic/61216c61-72b6-46b7-b11b-185bb28b2ada-27.png"],columns=1, object_fit="contain")
        gr.Markdown(value="## CC BY-NC-SA 4.0协议")
        gr.Markdown(value=ccbyncsa)
    with gr.Tab("专著"):
        with gr.Tab("专著"):
            with gr.Tab("专著"):
                with gr.Tab("普通图书及学位论文"):
                    isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                    author = gr.Textbox(label="主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
                    othertitle = gr.Textbox(label="其它题名信息（可选）",
                                            info="其它题名信息包括副题名，说明题名文字，多卷书的分卷书名、卷次、册次、标准号等。")
                    type = gr.Radio(["M（普通图书）", "D（学位论文）"], label="文献类型标识")
                    otherauthor = gr.Textbox(label="其它责任者（可选）", info="这里通常是译者，超过三个时写上“,译”即可，例如“印森林,吴胜和,李俊飞,译”；其它责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    version = gr.Textbox(label="版本项（可选）",
                                         info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代；外文参考文献版次用序数词的缩写形式表示，例如“Fifth edition”变成“5th ed.”。")
                    location = gr.Textbox(label="出版地（可选）",
                                          info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                    publisher = gr.Textbox(label="出版者（可选）",
                                           info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                    publishtime = gr.Textbox(label="出版年",
                                             info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
                    page = gr.Textbox(label="引文页码（可选）", info="例：10-11；引自序言或扉页题词的页码，可按实际情况著录")
                    button = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button.click(zzzzzz, inputs=[isotherlan, author, maintitle, othertitle, type, otherauthor, version, location, publisher,
                                             publishtime, page], outputs=[cita])
                    clearbutton.click(clear_all_12, inputs=[],
                                      outputs=[isotherlan, author, maintitle, othertitle, type, otherauthor, version, location,
                                               publisher, publishtime, page, cita])
                with gr.Tab("汇编及会议录"):
                    isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                    author = gr.Textbox(label="主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
                    othertitle = gr.Textbox(label="其它题名信息（可选）",
                                            info="其它题名信息包括副题名，说明题名文字，多卷书的分卷书名、卷次、册次、标准号等。")
                    type = gr.Radio(["C（会议录）", "G（汇编）"], label="文献类型标识")
                    otherauthor = gr.Textbox(label="其它责任者（可选）", info="这里通常是译者，超过三个时写上“,译”即可，例如“印森林,吴胜和,李俊飞,译”；其它责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    version = gr.Textbox(label="版本项（可选）",
                                         info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代；外文参考文献版次用序数词的缩写形式表示，例如“Fifth edition”变成“5th ed.”。")
                    location = gr.Textbox(label="出版地（可选）",
                                          info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                    publisher = gr.Textbox(label="出版者（可选）",
                                           info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                    publishtime = gr.Textbox(label="出版年",
                                             info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
                    button = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button.click(zzzzhbhyl,
                                 inputs=[isotherlan,author, maintitle, othertitle, type, otherauthor, version, location, publisher,
                                         publishtime], outputs=[cita])
                    clearbutton.click(clear_all_11, inputs=[],
                                      outputs=[isotherlan,author, maintitle, othertitle, type, otherauthor, version, location,
                                               publisher, publishtime, cita])
            with gr.Tab("电子资源专著"):
                with gr.Tab("普通图书及学位论文"):
                    isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                    author = gr.Textbox(label="主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
                    othertitle = gr.Textbox(label="其它题名信息（可选）",
                                            info="其它题名信息包括副题名，说明题名文字，多卷书的分卷书名、卷次、册次、标准号等。")
                    type = gr.Radio(["M（普通图书）", "D（学位论文）"], label="文献类型标识")
                    otherauthor = gr.Textbox(label="其它责任者（可选）", info="这里通常是译者，超过三个时写上“,译”即可，例如“印森林,吴胜和,李俊飞,译”；其它责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    version = gr.Textbox(label="版本项（可选）",
                                         info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代；外文参考文献版次用序数词的缩写形式表示，例如“Fifth edition”变成“5th ed.”。")
                    location = gr.Textbox(label="出版地（可选）",
                                          info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                    publisher = gr.Textbox(label="出版者（可选）",
                                           info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                    publishtime = gr.Textbox(label="出版年",
                                             info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
                    page = gr.Textbox(label="引文页码", info="例：10-11；引自序言或扉页题词的页码，可按实际情况著录")
                    date = gr.DateTime(label="引用日期", include_time=False, type="datetime",
                                       value="在右边输入，别再这里输，会报错➞")
                    url = gr.Textbox(label="获取和访问路径",info="即链接")
                    doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
                    button = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button.click(zzzzdzzy, inputs=[isotherlan,author, maintitle, othertitle, type, otherauthor, version, location, publisher,
                                             publishtime, page, date, url, doi], outputs=[cita])
                    clearbutton.click(clear_all_15, inputs=[],
                                      outputs=[isotherlan,author, maintitle, othertitle, type, otherauthor, version, location,
                                               publisher, publishtime, page, date, url, doi, cita])
                with gr.Tab("汇编及会议录"):
                    isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                    author = gr.Textbox(label="主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
                    othertitle = gr.Textbox(label="其它题名信息（可选）",
                                            info="其它题名信息包括副题名，说明题名文字，多卷书的分卷书名、卷次、册次、标准号等。")
                    type = gr.Radio(["C（会议录）", "G（汇编）"], label="文献类型标识")
                    otherauthor = gr.Textbox(label="其它责任者（可选）", info="这里通常是译者，超过三个时写上“,译”即可，例如“印森林,吴胜和,李俊飞,译”；其它责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    version = gr.Textbox(label="版本项（可选）",
                                         info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代；外文参考文献版次用序数词的缩写形式表示，例如“Fifth edition”变成“5th ed.”。")
                    location = gr.Textbox(label="出版地（可选）",
                                          info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                    publisher = gr.Textbox(label="出版者（可选）",
                                           info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                    publishtime = gr.Textbox(label="出版年",
                                             info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
                    date = gr.DateTime(label="引用日期", include_time=False, type="datetime",
                                       value="在右边输入，别再这里输，会报错➞")
                    url= gr.Textbox(label="获取和访问路径",info="即链接")
                    doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
                    button = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button.click(zzzzdzzyhbhyl,
                                 inputs=[isotherlan,author, maintitle, othertitle, type, otherauthor, version, location, publisher,
                                         publishtime,date,url,doi], outputs=[cita])
                    clearbutton.click(clear_all_14, inputs=[],
                                      outputs=[isotherlan,author, maintitle, othertitle, type, otherauthor, version, location,
                                               publisher, publishtime, date,url, doi, cita])
        with gr.Tab("专著析出文献"):
            with gr.Tab("专著析出文献"):
                isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                author = gr.Textbox(label="析出文献主要责任者",
                                    info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
                type = gr.Radio(["M（普通图书）", "C（会议录）", "G（汇编）"], label="文献类型标识")
                otherauthor = gr.Textbox(label="析出文献其它责任者（可选）",info="析出文献其它责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                bigauthor = gr.Textbox(label="专著主要责任者",
                                       info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                bigtitle = gr.Textbox(label="专著题名", info="多个题名之间用“;”间隔，至多三个")
                otherbigtitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
                version = gr.Textbox(label="版本项（可选）",
                                     info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代；外文参考文献版次用序数词的缩写形式表示，例如“Fifth edition”变成“5th ed.”。")
                location = gr.Textbox(label="出版地（可选）",
                                      info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                publisher = gr.Textbox(label="出版者（可选）",
                                       info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                publishtime = gr.Textbox(label="出版年",
                                         info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
                page = gr.Textbox(label="析出文献的页码", info="例：10-11")
                button2 = gr.Button("提交", variant='primary')
                clearbutton2 = gr.Button("清除")
                cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                button2.click(zzzzxcwxzzxcwx,
                              inputs=[isotherlan,author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version,
                                      location, publisher, publishtime, page], outputs=cita)
                clearbutton2.click(clear_all_14, inputs=[],
                                   outputs=[isotherlan,author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle,
                                            version, location, publisher, publishtime, page, cita])
            with gr.Tab("电子资源专著析出文献"):
                isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                author = gr.Textbox(label="析出文献主要责任者",
                                    info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
                type = gr.Radio(["M（普通图书）", "C（会议录）", "G（汇编）"], label="文献类型标识")
                otherauthor = gr.Textbox(label="析出文献其它责任者（可选）",info="析出文献其它责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                bigauthor = gr.Textbox(label="专著主要责任者",
                                       info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                bigtitle = gr.Textbox(label="专著题名", info="多个题名之间用“;”间隔，至多三个")
                otherbigtitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
                version = gr.Textbox(label="版本项（可选）",
                                     info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代；外文参考文献版次用序数词的缩写形式表示，例如“Fifth edition”变成“5th ed.”。")
                location = gr.Textbox(label="出版地（可选）",
                                      info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                publisher = gr.Textbox(label="出版者（可选）",
                                       info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                publishtime = gr.Textbox(label="出版年",
                                         info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
                page = gr.Textbox(label="析出文献的页码", info="例：10-11")
                date = gr.DateTime(label="引用日期", include_time=False, type="datetime",
                                   value="在右边输入，别再这里输，会报错➞")
                url = gr.Textbox(label="获取和访问路径",info="即链接")
                doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
                button2 = gr.Button("提交", variant='primary')
                clearbutton2 = gr.Button("清除")
                cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                button2.click(zzzzxcwxddzyxcwx,
                              inputs=[isotherlan,author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version,
                                      location, publisher, publishtime, page, date, url, doi], outputs=cita)
                clearbutton2.click(clear_all_17, inputs=[],
                                   outputs=[isotherlan,author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle,
                                            version, location, publisher, publishtime, page, date, url, doi, cita])
    with gr.Tab("连续出版物"):
        with gr.Tab("连续出版物"):
            with gr.Tab("连续出版物"):
                isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                author = gr.Textbox(label="主要责任者",info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                title = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
                othertitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
                year = gr.Textbox(label="年",info="即第一期的出版年")
                juan = gr.Textbox(label="卷（可选）",info="即第一期的卷数")
                qi = gr.Textbox(label="期（可选）",info="即第一期的期数")
                year2 = gr.Textbox(label="年（可选）",info="即最后一期的出版年，如果至今仍在发行忽略即可")
                juan2 = gr.Textbox(label="卷（可选）",info="即最后一期的卷数，如果至今仍在发行忽略即可")
                qi2 = gr.Textbox(label="期（可选）",info="即最后一期的期数，如果至今仍在发行忽略即可")
                location = gr.Textbox(label="出版地（可选）",info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                publisher = gr.Textbox(label="出版者（可选）",info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                publishtime = gr.Textbox(label="出版年",info="出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）；格式为：发行年-结刊年，至今仍在发行的刊物忽略结刊年即可，注意保留“-”")
                button2 = gr.Button("提交", variant='primary')
                clearbutton2 = gr.Button("清除")
                cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                button2.click(lxcbwlxcbwlxcbwqk, inputs=[isotherlan,author, title, othertitle, year, juan, qi, year2, juan2, qi2, location,publisher, publishtime], outputs=cita)
                clearbutton2.click(clear_all_14, inputs=[],outputs=[isotherlan,author, title, othertitle, year, juan, qi, year2, juan2, qi2, location,publisher, publishtime, cita])
            with gr.Tab("电子资源连续出版物"):
                isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                author = gr.Textbox(label="主要责任者",info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                title = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
                othertitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
                year = gr.Textbox(label="年",info="即第一期的出版年")
                juan = gr.Textbox(label="卷（可选）",info="即第一期的卷数")
                qi = gr.Textbox(label="期（可选）",info="即第一期的期数")
                year2 = gr.Textbox(label="年（可选）",info="即最后一期的出版年，如果至今仍在发行忽略即可")
                juan2 = gr.Textbox(label="卷（可选）",info="即最后一期的卷数，如果至今仍在发行忽略即可")
                qi2 = gr.Textbox(label="期（可选）",info="即最后一期的期数，如果至今仍在发行忽略即可")
                location = gr.Textbox(label="出版地（可选）",info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
                publisher = gr.Textbox(label="出版者（可选）",info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                publishtime = gr.Textbox(label="出版年",info="出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）；格式为：发行年-结刊年，至今仍在发行的刊物忽略结刊年即可，注意保留“-”")
                date = gr.DateTime(label="引用日期", include_time=False, type="datetime",value="在右边输入，别再这里输，会报错➞")
                url = gr.Textbox(label="获取和访问路径",info="即链接")
                doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
                button2 = gr.Button("提交", variant='primary')
                clearbutton2 = gr.Button("清除")
                cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                button2.click(lxcbwlxcbwdzzylxcbwqk,inputs=[isotherlan,author, title, othertitle, year, juan, qi, year2, juan2, qi2, location,publisher, publishtime, date, url, doi], outputs=cita)
                clearbutton2.click(clear_all_17, inputs=[],outputs=[isotherlan,author, title, othertitle, year, juan, qi, year2, juan2, qi2, location,publisher, publishtime, date, url, doi, cita])
        with gr.Tab("连续出版物析出文献"):
            with gr.Tab("连续出版物析出文献"):
                with gr.Tab("期刊"):
                    author = gr.Textbox(label="析出文献主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
                    rapidtitle = gr.Textbox(label="连续出版物题名", info="多个题名之间用“;”间隔，至多三个")
                    otherrapidtitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
                    year = gr.Textbox(label="年")
                    juan = gr.Textbox(label="卷")
                    qi = gr.Textbox(label="期")
                    page = gr.Textbox(label="页码", info="例：10-11")
                    button2 = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button2.click(lxcbwlxcbwxcwxlxcbwxcwxqk,
                                  inputs=[author, title, rapidtitle, otherrapidtitle, year, juan, qi, page], outputs=cita)
                    clearbutton.click(fn=clear_all_9, inputs=[],
                                      outputs=[author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, cita])

                with gr.Tab("报纸"):
                    isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                    author = gr.Textbox(label="析出文献主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
                    publisher = gr.Textbox(label="出版者（可选）",
                                           info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                    publishdate = gr.DateTime(label="出版日期", include_time=False, type="datetime",
                                       value="在右边输入，别再这里输，会报错➞")
                    banci = gr.Textbox(label="版次",info="通常在报纸报眉最上面的地方所标明的数字，代表报纸版面的次序。")
                    button2 = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button2.click(lxcbwlxcbwxcwxlxcbwxcwxbz,
                                  inputs=[isotherlan,author, title, publisher, publishdate, banci], outputs=cita)
                    clearbutton.click(fn=clear_all_7, inputs=[],
                                      outputs=[isotherlan,author, title, publisher, publishdate, banci, cita])

            with gr.Tab("电子资源连续出版物析出文献"):
                with gr.Tab("期刊"):
                    author = gr.Textbox(label="析出文献主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
                    rapidtitle = gr.Textbox(label="连续出版物题名", info="多个题名之间用“;”间隔，至多三个")
                    otherrapidtitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
                    year = gr.Textbox(label="年")
                    juan = gr.Textbox(label="卷")
                    qi = gr.Textbox(label="期")
                    page = gr.Textbox(label="页码", info="例：10-11")
                    date = gr.DateTime(label="引用日期", include_time=False, type="datetime",
                                       value="在右边输入，别再这里输，会报错➞")
                    url = gr.Textbox(label="获取和访问路径",info="即链接")
                    doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
                    button2 = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button2.click(lxcbwlxcbwxcwxdzzylxcbwxcwxqk,
                                  inputs=[author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, date, url,
                                          doi], outputs=cita)
                    clearbutton.click(fn=clear_all_12, inputs=[],
                                      outputs=[author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, date,
                                               url, doi, cita])
                with gr.Tab("报纸"):
                    isotherlan=gr.Checkbox(label="此参考文献是否为外文")
                    author = gr.Textbox(label="析出文献主要责任者",
                                        info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
                    title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
                    publisher = gr.Textbox(label="出版者（可选）",
                                           info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
                    publishdate = gr.DateTime(label="出版日期", include_time=False, type="datetime",
                                              value="在右边输入，别再这里输，会报错➞")
                    banci = gr.Textbox(label="版次",info="通常在报纸报眉最上面的地方所标明的数字，代表报纸版面的次序。")
                    date = gr.DateTime(label="引用日期", include_time=False, type="datetime",
                                       value="在右边输入，别再这里输，会报错➞")
                    url= gr.Textbox(label="获取和访问路径",info="即链接")
                    doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
                    button2 = gr.Button("提交", variant='primary')
                    clearbutton = gr.Button("清除")
                    cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
                    button2.click(lxcbwlxcbwxcwxdzzylxcbwxcwxbz,
                                  inputs=[isotherlan,author, title, publisher, publishdate, banci, date, url,doi], outputs=cita)
                    clearbutton.click(fn=clear_all_10, inputs=[],
                                      outputs=[isotherlan,author, title, publisher, publishdate, banci, date, url, doi, cita])
    with gr.Tab("专利文献"):
        with gr.Tab("专利文献"):
            author = gr.Textbox(label="专利所有者或申请者",
                                info="专利所有者或申请者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
            title = gr.Textbox(label="专利题名")
            num = gr.Textbox(label="专利号")
            publictime = gr.DateTime(label="公告日期或公开日期", include_time=False, type="datetime",
                                     value="在右边输入，别再这里输，会报错➞")
            button2 = gr.Button("提交", variant='primary')
            clearbutton2 = gr.Button("清除")
            cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
            button2.click(zlwxzlwx, inputs=[author, title, num, publictime], outputs=cita)
            clearbutton2.click(clear_all_5, inputs=[], outputs=[author, title, num, publictime, cita])
        with gr.Tab("电子资源专利文献"):
            author = gr.Textbox(label="专利所有者或申请者",
                                info="专利所有者或申请者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
            title = gr.Textbox(label="专利题名")
            num = gr.Textbox(label="专利号")
            publictime = gr.DateTime(label="公告日期或公开日期", include_time=False, type="datetime",
                               value="在右边输入，别再这里输，会报错➞")
            date = gr.DateTime(label="引用日期", include_time=False, type="datetime",
                               value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径",info="即链接")
            doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
            button2 = gr.Button("提交", variant='primary')
            clearbutton2 = gr.Button("清除")
            cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
            button2.click(zlwxdzzyzlwx, inputs=[author, title, num, publictime, date, url, doi], outputs=cita)
            clearbutton2.click(clear_all_8, inputs=[], outputs=[author, title, num, publictime, date, url, doi, cita])
    with gr.Tab("电子公告"):
        author = gr.Textbox(label="主要责任者",
                            info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”或与之相应的词；个人著者采用姓在前名在后的著录形式，姓全部著录，字母全大写，名可缩写为首字母（仅欧美，省略缩写点），如用首字母无法识别该人名时，则用全名；欧美著者的中译名只著录其姓，同姓不同名的欧美著者，其中译名不仅要著录其姓，还需著录其名的首字母。")
        maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
        othertitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
        changetime = gr.DateTime(label="更新或修改日期（可选）", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
        date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
        url = gr.Textbox(label="获取和访问路径",info="即链接")
        doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如“10.4236/nr.2019.103004”；如果获取和访问路径里有就不用加了")
        button = gr.Button("提交", variant='primary')
        clearbutton = gr.Button("清除")
        cita = gr.Textbox(label="Citation", interactive=False, show_copy_button=True)
        button.click(dzgg,
                     inputs=[author, maintitle, othertitle, changetime, date,url, doi], outputs=[cita])
        clearbutton.click(fn=clear_all_8, inputs=[],
                          outputs=[author, maintitle, othertitle, changetime,date, url, doi, cita])
    gr.HTML(copyright_html)

demo.launch(inbrowser=True,server_name="0.0.0.0",server_port=8888,favicon_path="./pic/IMG_8527.JPG",show_api=False)