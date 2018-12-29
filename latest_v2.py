import re
import requests
import urllib.parse
from utils import pretty_print
from requests_html import HTML
from collections import OrderedDict #syntax

def get_metadata_from(url):

    def parse_next_link(doc):
        html = HTML(html=doc)
        controls = html.find('.action-bar a.btn.wide')
        link = controls[1].attrs.get('href')
        return urllib.parse.urljoin('https://www.ptt.cc/', link)

    resp = fetch(url)
    post_entries = parse_article_entries(resp.text)
    next_link = parse_next_link(resp.text)

    metadata = [parse_article_meta(entry) for entry in post_entries]
    return metadata, next_link

def get_paged_meta(url, num_pages):
    collected_meta = []

    for _ in range(num_pages):
        posts, link = get_metadata_from(url)
        collected_meta += posts
        url = urllib.parse.urljoin('https://www.ptt.cc/', link)

    return collected_meta


def fetch(url):
    response=requests.get(url)
    return response

def parse_article_entries(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries

def parse_article_meta(entry):
    '''
    每筆資料都存在 dict() 類型中：key-value paird data
    '''
    meta = {
        'title': entry.find('div.title', first=True).text,
        'push': entry.find('div.nrec', first=True).text,
        'date': entry.find('div.date', first=True).text,
    }
    try:
        # 正常狀況取得資料
        meta['author'] = entry.find('div.author', first=True).text
        meta['link'] = entry.find('div.title > a', first=True).attrs['href']
    except AttributeError:
        # 但碰上文章被刪除時，就沒有辦法像原本的方法取得 作者 跟 連結
        if '(本文已被刪除)' in meta['title']:
            # e.g., "(本文已被刪除) [haudai]"
            match_author = re.search('\[(\w*)\]', meta['title'])
            if match_author:
                meta['author'] = match_author.group(1)
        elif re.search('已被\w*刪除', meta['title']):
            # e.g., "(已被cappa刪除) <edisonchu> op"
            match_author = re.search('\<(\w*)\>', meta['title'])
            if match_author:
                meta['author'] = match_author.group(1)
    return meta

    # 最終仍回傳統一的 dict() 形式 paired data
    return meta

def replace_all(text,dic):
    for i, j in dic.items():
        text=text.replace(i,j)
    return text

def dataintxt(meta):
    title=str(meta["title"])
    try:
        fout=open('%s.txt'%title,'wt')
    except :
        od=OrderedDict([("%s"%i,"_") for i in '\/:*?"<>|'])
        title=replace_all(str(meta["title"]),od)#.replace("%s"%rp,"_")
        fout=open('%s.txt'%title,'wt')
    content=str(meta['push']+'\t'+ meta['title']+'\t'+  meta['date']+'\t'+  meta['author'])
    fout.write(content)
    fout.close()  #store file into txt

start_url = 'https://www.ptt.cc/bbs/Stock/index.html'
metadata = get_paged_meta(start_url, num_pages=5)
for meta in metadata:
    #pretty_print(meta['push'], meta['title'], meta['date'], meta['author'])
    dataintxt(meta)
