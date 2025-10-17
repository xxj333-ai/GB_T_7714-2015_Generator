# Copyright (c) 2024-2025 Maxxj
# Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
#
# This script is free for non-commercial use.
# For commercial use, please contact xxjlyh3332@gmail.com.

import gradio as gr

def zz(author, maintitle, othertitle, type, otherauthor, version, location, publisher, publishtime, page, date, url, doi):
    citation = []
    citation.append(author + ". " + maintitle)
    if othertitle:
        citation.append(":" + othertitle)
    citation.append("[" + type[:1])
    if url:
        citation.append("/OL")
    citation.append("]. ")
    if otherauthor:
        citation.append(otherauthor + ". ")
    if version:
        citation.append(version + ". ")
    if not location:
        citation.append("[出版地不详]:")
    else:
        citation.append(location + ":")
    if not publisher:
        citation.append("[出版者不详],")
    else:
        citation.append(publisher + ",")
    if publishtime:
        citation.append(publishtime + ":")
    citation.append(page + "[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url + ". ")
    if doi:
        citation.append("DOI:" + doi + ". ")
    return ''.join(citation)

def qk(author, title, othertitle, year, juan, qi, year2, juan2, qi2, location, publisher, publishtime, date, url, doi):
    citation = []
    citation.append(author + ". " + title)
    if othertitle:
        citation.append(":" + othertitle)
    citation.append("[J")
    if url:
        citation.append("/OL")
    citation.append("]. " + year)
    if juan:
        citation.append("," + juan)
    if qi:
        citation.append("(" + qi + ")")
    citation.append("-" + year2)
    if juan2:
        citation.append("," + juan2)
    if qi2:
        citation.append("(" + qi2 + ")")
    citation.append(". ")
    if location:
        citation.append(location + ":")
    else:
        citation.append("[出版地不详]:")
    if publisher:
        citation.append(publisher + ". ")
    else:
        citation.append("[出版者不详],")
    citation.append(publishtime + "[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url + ". ")
    if doi:
        citation.append("DOI:" + doi + ". ")
    return ''.join(citation)

def zl(author, title, num, publictime, date, url, doi):
    citation = []
    citation.append(author + ". " + title + ":" + num + "[P")
    if url:
        citation.append("/OL")
    citation.append("]. " + publictime + "[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url)
    if doi:
        citation.append("DOI:" + doi + ". ")
    return ''.join(citation)

def zzxc(author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version, location, publisher, publishtime, page, date, url, doi):
    citation = []
    citation.append(author + ". " + title + "[" + type[:1])
    if url:
        citation.append("/OL")
    citation.append("]. ")
    if otherauthor:
        citation.append(otherauthor)
    citation.append("//" + bigauthor + ". " + bigtitle)
    if otherbigtitle:
        citation.append(":" + otherbigtitle)
    citation.append(". ")
    if version:
        citation.append(version + ". ")
    if location:
        citation.append(location + ":")
    else:
        citation.append("[出版地不详]:")
    if publisher:
        citation.append(publisher + ". ")
    else:
        citation.append("[出版者不详],")
    citation.append(publishtime + ":" + page + "[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url + ". ")
    if doi:
        citation.append("DOI:" + doi + ". ")
    return ''.join(citation)

def qkxc(author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, date, url, doi):
    citation = []
    citation.append(author + ". " + title + "[J")
    if url:
        citation.append("/OL")
    citation.append("]. " + rapidtitle)
    if otherrapidtitle:
        citation.append(":" + otherrapidtitle)
    citation.append("," + year)
    if juan:
        citation.append("," + juan)
    if qi:
        citation.append("(" + qi + "):")
    citation.append(page + "[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url)
    if doi:
        citation.append("DOI:" + doi + ". ")
    return ''.join(citation)

def bzxc(author, title, rapidtitle, otherrapidtitle, publishyear, banci, date, url):
    citation = []
    citation.append(author + ". " + title + "[N")
    if url:
        citation.append("/OL")
    citation.append("]. " + rapidtitle)
    if otherrapidtitle:
        citation.append(":" + otherrapidtitle)
    citation.append("," + str(publishyear)[:10] + "]. ")
    if banci:
        citation.append("(" + banci + ")")
    citation.append("[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url)
    return ''.join(citation)

def dzzy(author, maintitle, othertitle, location, publisher, publishtime, changetime, page, date, url, doi):
    citation = []
    citation.append(author + ". " + maintitle)
    if othertitle:
        citation.append(":" + othertitle)
    citation.append("[EB/OL]. ")
    if location:
        citation.append(location + ":")
    else:
        citation.append("[出版地不详]:")
    if publisher:
        citation.append(publisher + ",")
    else:
        citation.append("[出版者不详],")
    citation.append(publishtime + ":" + page)
    if changetime:
        citation.append("(" + changetime + ")")
    citation.append("[" + str(date)[:10] + "]. ")
    if url:
        citation.append(url + ". ")
    if doi:
        citation.append("DOI:" + doi + ". ")
    return ''.join(citation)

def clear_all():
    return [""] * 14

with gr.Blocks() as demo:
    gr.Markdown("# GB/T 7714-2015参考文献生成器")
    gr.Markdown('''
### Created by xxj
免责声明：本生成器禁止用于任何商业用途或盈利，生成结果仅为参考，任何由于对本生成器的错误利用或盲目依赖此生成器造成的相关后果包括citation那一项没分等由使用者承担，与创作者无关。
    ''')
    with gr.Tab("参考文献本体"):
        with gr.Tab("专著"):
            author = gr.Textbox(label="主要责任者",info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；责任者情况不明可写“佚名”等")
            maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
            othertitle = gr.Textbox(label="其它题名信息（可选）",info="其它题名信息包括副题名，说明题名文字，多卷书的分卷书名、卷次、册次、标准号等。")
            type = gr.Radio(["M（普通图书）", "C（会议录）","G（汇编）","D（学位论文）", "S（标准）"], label="文献类型标识")
            otherauthor = gr.Textbox(label="其它责任者（可选）",info="这里通常是译者，超过三个时加上“,译”即可")
            version = gr.Textbox(label="版本项（可选）",info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代")
            location = gr.Textbox(label="出版地（可选）",info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
            publisher = gr.Textbox(label="出版者（可选）",info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
            publishtime = gr.Textbox(label="出版年",info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
            page = gr.Textbox(label="引文页码", info="例：10-11；引自序言或扉页题词的页码，可按实际情况著录")
            date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径（可选）")
            doi = gr.Textbox(label="数字对象唯一标识符（可选）",info="如果获取和访问路径里有就不用加了")
            button = gr.Button("提交",variant='primary')
            clearbutton=gr.Button("清除")
            cita = gr.Label(value="", label="Citation")
            button.click(zz, inputs=[author, maintitle, othertitle, type, otherauthor, version, location, publisher,publishtime, page, date, url, doi], outputs=[cita])
            clearbutton.click(clear_all, inputs=[], outputs=[author, maintitle, othertitle, type, otherauthor, version, location, publisher, publishtime, page, date, url, doi, cita])
        with gr.Tab("期刊"):
            author = gr.Textbox(label="主要责任者", info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”")
            title = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
            othertitle = gr.Textbox(label="其它题名信息", info="其它题名信息包括副题名，说明题名文字")
            year = gr.Textbox(label="年")
            juan = gr.Textbox(label="卷（可选）")
            qi = gr.Textbox(label="期（可选）")
            year2 = gr.Textbox(label="年")
            juan2 = gr.Textbox(label="卷（可选）")
            qi2 = gr.Textbox(label="期（可选）")
            location = gr.Textbox(label="出版地（可选）", info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
            publisher = gr.Textbox(label="出版者（可选）", info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
            publishtime = gr.Textbox(label="出版年", info="出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
            date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径（可选）")
            doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如果获取和访问路径里有就不用加了")
            button2 = gr.Button("提交", variant='primary')
            clearbutton2 = gr.Button("清除")
            cita = gr.Label(value="", label="Citation")
            button2.click(qk, inputs=[author, title, othertitle, year, juan, qi, year2, juan2, qi2, location, publisher, publishtime, date, url, doi], outputs=cita)
            clearbutton2.click(clear_all, inputs=[], outputs=[author, title, othertitle, year, juan, qi, year2, juan2, qi2, location, publisher, publishtime, date, url, doi, cita])
        with gr.Tab("专利"):
            author = gr.Textbox(label="专利所有者或申请者", info="专利所有者或申请者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”")
            title = gr.Textbox(label="专利题名")
            num = gr.Textbox(label="专利号")
            publictime = gr.Textbox(label="公告日期或公开日期")
            date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径（可选）")
            doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如果获取和访问路径里有就不用加了")
            button2 = gr.Button("提交", variant='primary')
            clearbutton2 = gr.Button("清除")
            cita = gr.Label(value="", label="Citation")
            button2.click(zl, inputs=[author, title, num, publictime, date, url, doi], outputs=cita)
            clearbutton2.click(clear_all, inputs=[], outputs=[author, title, num, publictime, date, url, doi, cita])
    with gr.Tab("析出文献"):
        with gr.Tab("专著"):
            author = gr.Textbox(label="析出文献主要责任者", info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”")
            title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
            type = gr.Radio(["M（普通图书）", "C（会议录）", "G（汇编）", "D（学位论文）", "S（标准）"], label="文献类型标识")
            otherauthor = gr.Textbox(label="析出文献其它责任者（可选）")
            bigauthor = gr.Textbox(label="专著主要责任者", info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”")
            bigtitle = gr.Textbox(label="专著题名", info="多个题名之间用“;”间隔，至多三个")
            otherbigtitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
            version = gr.Textbox(label="版本项（可选）", info="第1版不著录，其他版本说明应著录；版本用阿拉伯数字、序数缩写形式或其他标识表示；古籍的版本可著录“写本”、“抄本”、“刻本”、“活字本”等，可加朝代")
            location = gr.Textbox(label="出版地（可选）", info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
            publisher = gr.Textbox(label="出版者（可选）", info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
            publishtime = gr.Textbox(label="出版年", info="如有其他纪年形式时，将原有的纪年形式置于“()”内，例如“1947(民国三十六年)”；出版年无法确定时，可依次选用版权年（例如“c1985”）、印刷年（例如“1985 印刷”）、估计的出版年（例如“[1985]”）")
            page = gr.Textbox(label="析出文献的页码", info="例：10-11")
            date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径（可选）")
            doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如果获取和访问路径里有就不用加了")
            button2 = gr.Button("提交", variant='primary')
            clearbutton2 = gr.Button("清除")
            cita = gr.Label(value="", label="Citation")
            button2.click(zzxc, inputs=[author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version, location, publisher, publishtime, page, date, url, doi], outputs=cita)
            clearbutton2.click(clear_all, inputs=[], outputs=[author, title, type, otherauthor, bigauthor, bigtitle, otherbigtitle, version, location, publisher, publishtime, page, date, url, doi, cita])
        with gr.Tab("期刊"):
            author = gr.Textbox(label="析出文献主要责任者",info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”")
            title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
            rapidtitle = gr.Textbox(label="连续出版物题名")
            otherrapidtitle = gr.Textbox(label="其它题名信息",info="其它题名信息包括副题名，说明题名文字")
            year = gr.Textbox(label="年")
            juan = gr.Textbox(label="卷（可选）")
            qi = gr.Textbox(label="期（可选）")
            page = gr.Textbox(label="页码",info="例：10-11")
            date = gr.DateTime(label="引用日期",include_time=False,type="datetime", value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径（可选）")
            doi = gr.Textbox(label="数字对象唯一标识符（可选）",info="如果获取和访问路径里有就不用加了")
            button2 = gr.Button("提交",variant='primary')
            clearbutton = gr.Button("清除")
            cita = gr.Label(value="", label="Citation")
            button2.click(qkxc,inputs=[author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, date, url, doi], outputs=cita)
            clearbutton.click(fn=clear_all, inputs=[], outputs=[author, title, rapidtitle, otherrapidtitle, year, juan, qi, page, date, url, doi, cita])
        with gr.Tab("报纸"):
            author = gr.Textbox(label="析出文献主要责任者", info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”")
            title = gr.Textbox(label="析出文献题名", info="多个题名之间用“;”间隔，至多三个")
            rapidtitle = gr.Textbox(label="连续出版物题名", info="多个题名之间用“;”间隔，至多三个")
            otherrapidtitle = gr.Textbox(label="其它题名信息",info="其它题名信息包括副题名，说明题名文字")
            publishyear = gr.Textbox(label="出版年")
            banci = gr.Textbox(label="版次（可选）")
            date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
            url = gr.Textbox(label="获取和访问路径（可选）")
            button2 = gr.Button("提交",variant='primary')
            clearbutton = gr.Button("清除")
            cita = gr.Label(value="", label="Citation")
            button2.click(bzxc, inputs=[author, title, rapidtitle, otherrapidtitle, publishyear, banci, date, url], outputs=cita)
            clearbutton.click(fn=clear_all, inputs=[], outputs=[author, title, rapidtitle, otherrapidtitle, publishyear, banci, date, url, cita])
    with gr.Tab("电子资源"):
        author = gr.Textbox(label="主要责任者",
                            info="责任者超过三个时写上“,等”即可，例如“印森林,吴胜和,李俊飞,等”；作者情况不明可写“佚名”等")
        maintitle = gr.Textbox(label="题名", info="多个题名之间用“;”间隔，至多三个")
        othertitle = gr.Textbox(label="其它题名信息（可选）", info="其它题名信息包括副题名，说明题名文字")
        location = gr.Textbox(label="出版地（可选）",
                              info="对同名异地或不为人们熟悉的城市名，宜在城市名后附省、州名或国名等限定语")
        publisher = gr.Textbox(label="出版者（可选）",
                               info="出版者可以按著录信息源所载的形式著录，也可以按国际公认的简化形式或缩写形式著录；如有多个出版者，只写第一个或处于显要位置的出版者")
        publishtime = gr.Textbox(label="出版年",
                                 info="出版年无法确定时，可依次选用版权年（例如“c1985”）和估计的出版年（例如“[1985]”）")
        changetime = gr.Textbox(label="更新或修改日期（可选）")
        page = gr.Textbox(label="引文页码（可选）", info="例：10-11")
        date = gr.DateTime(label="引用日期", include_time=False, type="datetime", value="在右边输入，别再这里输，会报错➞")
        url = gr.Textbox(label="获取和访问路径（可选）")
        doi = gr.Textbox(label="数字对象唯一标识符（可选）", info="如果获取和访问路径里有就不用加了")
        button = gr.Button("提交", variant='primary')
        clearbutton = gr.Button("清除")
        cita = gr.Label(value="", label="Citation")
        button.click(dzzy,
                     inputs=[author, maintitle, othertitle, location, publisher, publishtime, changetime, page, date,
                             url, doi], outputs=[cita])
        clearbutton.click(fn=clear_all, inputs=[],
                          outputs=[author, maintitle, othertitle, location, publisher, publishtime, changetime, page,
                                   date, url, doi, cita])

demo.launch(show_error=True,share=True)