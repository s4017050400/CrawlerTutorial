import re
import requests
import urllib.parse
from utils import pretty_print  # in other file
from requests_html import HTML

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

#url="https://www.ptt.cc/bbs/Stock/index.html"
#resp=fetch(url)
#post_entries = parse_article_entries(resp.text)

start_url = 'https://www.ptt.cc/bbs/Stock/index.html'
metadata = get_paged_meta(start_url, num_pages=5)
for meta in metadata:
    pretty_print(meta['push'], meta['title'], meta['date'], meta['author'])
    


results
______________________________________________________________________________

4	(本文已被刪除) [ab626]                            12/20	ab626
 11	Re: [標的] 2382廣達                               12/20	zesonpso
 18	Re: [心得] 長期投資，心得分享，一起討論補充       12/20	jfubgabc
  3	(本文已被刪除) [ab626]                            12/20	ab626
  6	[新聞] 經濟壓力考驗房市 廣州珠海限購放鬆          12/20	nightwing
  7	Re: [標的] 美元指數 長期空                        12/20	Babygirl170
 29	[新聞] 中國嗆美不得實施《西藏旅行對等法》後果     12/20	tangolosss
  7	Re: [新聞] 川普下令美軍撤出敘利亞，五角大廈、敘利 12/20	kenbbc12321
 31	[新聞] 「台灣薪資真的給太低」矽谷創投教父給台     12/20	cjol
  9	[新聞] 32家庫藏股 護盤不力                        12/20	tangolosss
  9	Re: [新聞] 川普下令美軍撤出敘利亞，五角大廈、敘利 12/20	Atima
 10	[新聞] 明年八大公股全加薪 第一金、華南年終發5     12/20	pttmans
   	[其他] 107/12/20 加權股價指數成分股暨市值比重     12/20	BreezeCat
  1	Re: [心得] 長期投資，心得分享，一起討論補充       12/20	fill8800541
 44	[公告] 精華區導覽Q&A                              1/25	IanLi
   	[公告] Stock 板規V2.3 (2018/11/03)                11/03	eyespot
  爆	[閒聊] 2018/12/20 盤後閒聊                        12/20	tim0259
  1	(本文已被刪除) [YenFuOne]                         12/20	YenFuOne
 12	Fw: [心得] 從選擇權看安樂死與繁衍的價值           12/20	SMIC5566
 13	[新聞] 技術分析師：標普下個支撐在2450 但頭肩      12/20	richshen
 58	[閒聊] 2018/12/20 盤後閒聊                        12/20	tim0259
 14	[心得] 長期投資，心得分享，一起討論補充           12/20	sim2347
 41	[其他] 107年12月20日 三大法人買賣金額統計表       12/20	coconing
 19	[新聞] 向高雄求救？華映董事長林蔚山遞密函給       12/20	GoOdGaMe
 15	[新聞] 華映重訊宣布恢復供料 22日復工              12/20	GoOdGaMe
  7	[新聞] SEMI：2019年全球晶圓廠設備投資下滑7.8%     12/20	zxcvxx
  6	(本文已被刪除) [elfish123]                        12/20	elfish123
  5	[新聞] 蘋果成長放緩之際，將在2019年推出新服務     12/20	zxcvxx
 16	[請益] 同是FOD為何狂炒神盾但gis沉淪?              12/20	Avandia
 31	[新聞] 川普下令美軍撤出敘利亞，五角大廈、敘利     12/20	howard172
  5	Re: [標的] 5876上海銀                             12/20	moodhunter
  7	[請益]                                            12/20	NASH7788
  2	[新聞] 中國出新招變相降息　人民幣失守6.91         12/20	deepdish
 78	[新聞] 韓國瑜將在楠梓發展賽馬產業鏈               12/20	rtwodtwo
  5	Re: [請益]                                        12/20	ppp123
 31	[新聞] 美國升息台股跌 顧立雄：失望的不是升息      12/20	rocklorl
  2	[新聞] 處變不「金」！股債商品全跌　它單季飆4.     12/20	deepdish
  8	[標的] 聯發科 2454 短中長多                       12/20	ZhuBeiCity
 26	Re: [心得] 自認不是高手的，良心建議，長期投資吧   12/20	safelove
 21	[新聞] 公司派放火燒整城!謝金:老牌家電廠吞惡果     12/20	tangolosss
 88	[標的] 放空6182 合晶 現股當沖實戰教學 必勝        12/20	Ejaculation
 77	[新聞] 韓國瑜坦言迪士尼蓋不出來 還沒上任跳票!     12/20	tangolosss
  4	[新聞] 賽靈思推軍規晶片，採用台積電16奈米製程     12/20	idunhav1
 11	[標的] 2375 智寶 多                               12/20	lelo
 13	[標的] 2308台達電                                 12/20	wangwi
  9	[新聞] 潛艦國造最後衝刺 海軍:明年3月20日可完成簽約12/20	idunhav1
  7	[標的] 4958臻鼎KY（作多）                         12/20	GoToWeGo
  9	[新聞] 中共加強「數據維穩」 經濟寒冬欲蓋彌彰      12/20	CLV518
  5	Re: [標的] 中裕 橫向盤整以及回測                  12/20	Plasticine
  4	[新聞] 三星屏下指紋訂單挹注 外資調高神盾評等5     12/20	hebe986
  8	[新聞] 川普的一天：自豪只睡3-4小時是成功關鍵      12/20	CLV518
  2	Re: [標的] (多)元黃金正二 00708L                  12/20	hrma
  7	Re: [標的] 中裕 橫向盤整以及回測                  12/20	ZhuBeiCity
  6	[新聞] 防範中資收購，德國緊縮外人投資規定         12/20	sky419012
 10	[新聞] 大同驚爆第三波假外資 金管會年底前開鍘      12/20	nightwing
  7	[新聞] 謝金河指大同公司派出了下策：放火將整城 燒成灰燼12/20	sinana
 31	[新聞] 北京要求享有開發中國家待遇！美國WTO大      12/20	nightwing
 X1	Re: [新聞] 中國大媽買台股 暫不開放                12/20	alberchi
   	Re: [心得]如何判斷大盤開始走長多                  12/20	YAYA6655
 18	[新聞] 川普氣pupu！Fed再升息1碼今年第4升          12/20	deepdish
 11	Re: [請益] 為什麼會有人相信技術分析這種蠢事       12/20	aalluubbaa
 19	[新聞] Fed升息一碼，並暗示2019只會升兩次          12/20	meRscliche
  4	[標的] 1台指加空                                  12/20	lynos
  1	[新聞] 這國狂課770億新稅　股市嚇到暴跌10趴        12/20	sleepyuan
 26	Re: [新聞] Fed升息一碼，並暗示2019只會升兩次      12/20	lynos
 20	[新聞] 7奈米以下燒錢大戰　台積電暫領先三星        12/20	kaube
  2	[請益] 損益表的百慕達三角                         12/20	Tite
  6	[請益] 跟常虧錢散戶反作賺錢可能性                 12/20	ttmb
 26	[新聞] WTO恐成戰場！中國將請求WTO調查美國關稅     12/20	nightwing
  4	[新聞] 2019年手機產業不可忽視的幾件事             12/20	zyquan1207
  6	[請益] 熊市的投資建議,美債or台灣50                12/20	YenFuOne
 10	[新聞] 坦承欠款、融資困難 ofo創辦人：為每分錢     12/20	nightwing
 91	[閒聊] 2018/12/20 盤中閒聊                        12/20	annz
  9	Re: [心得]如何判斷大盤開始走長多                  12/20	gk1329
 29	[新聞] Fed升息美股跌逾1％ 道瓊大跌351點           12/20	charles0939
  6	[新聞] 基亞、高端 瞄準細胞治療大餅                12/20	k020164043
   	[標的] 2360致茂                                   12/20	Satsuki7552
 14	[新聞] 貿易戰打到不想消費 陸客「沒了」害慘旅      12/19	SatoTakuma
 39	[新聞]英特爾宣布：將關閉「晶圓代工業務」          12/19	AguTp
  8	Re: [新聞] 華為稱：在德、法、日等多國的5G業務正常 12/19	PigIsBignana
  9	[新聞] 外資12月以來大賣新光金18.9萬張             12/19	Noemen
  6	[標的] 4999鑫禾                                   12/19	lsl297
 33	[心得] 良心建議，長期投資，心得分享               12/19	sim2347
 11	[新聞] 五眼聯盟狙擊華為，這些國家已相繼將華       12/19	sky419012
 11	[新聞] 《各報要聞》美股最慘12月，堪比1931大       12/19	charloette
 12	[請益] 放空操作（實際）                           12/19	KKlin813
  7	Re: [請益] 為什麼會有人相信技術分析這種蠢事       12/19	Justisaac
  8	[新聞] 中國大媽買台股 暫不開放                    12/19	GoOdGaMe
  8	Re: [請益] 為什麼會有人相信技術分析這種蠢事       12/19	alihue
 11	[新聞] 宏致三大利多加持 明年轉骨獲利挑戰5年高     12/19	cjol
   	Re: [請益] 為什麼會有人相信技術分析這種蠢事       12/19	sunsonsam
  7	[心得]如何判斷大盤開始走長多                      12/19	noldorelf
  4	[請益] 升息與數據                                 12/19	dharma
  8	Re: [請益] 為什麼會有人相信技術分析這種蠢事       12/19	stalna
  2	[標的] (空)華頓黃豆00693U(明天的規劃)             12/20	hrma
  7	Re: [請益] 為什麼會有人相信技術分析這種蠢事       12/20	cutbear123
 17	[新聞] 習式改革中國改革開放40年經濟陷空前困境     12/20	tangolosss
