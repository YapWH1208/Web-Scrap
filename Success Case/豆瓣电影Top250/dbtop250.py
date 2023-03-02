from bs4 import BeautifulSoup # webpage analyze, get data
import re # word matching (dev mode)
# urllib change be change into request
import urllib.request, urllib.error # generate url, get webpage data 
import xlwt # Save in Excel
import sqlite3 # Save in SQL

'''
__STEPS__
1. get url
2. analyze web page one by one
3. save data
'''

def main():
    URL = 'https://movie.douban.com/top250?start='
    datalist  = getData(URL)

    savepath = "./豆瓣电影TOP250.xls"
    saveData2EX(datalist, savepath)

    dbpath = './豆瓣电影TOP250.db'
    saveData2DB(datalist, dbpath)

findLink = re.compile(r'<a href="(.*?)">')
findImgLink = re.compile(r'<img .* src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findComment = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findInfo = re.compile(r'<p class="">(.*?)</p>', re.S)

def getData(URL):
    datalist = []
    for i in range(0, 10):
        link = URL + str(i*25)
        html = askURL(link)

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            img = re.findall(findImgLink, item)[0]
            data.append(img)

            title = re.findall(findTitle, item)
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("/","")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            comment = re.findall(findComment, item)[0]
            data.append(comment)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            
            info = re.findall(findInfo, item)[0]
            info = re.sub('<br(\s+)?/>(\s+)?', " ", info)
            info = re.sub('/', " ", info)
            data.append(info.strip())

            datalist.append(data)

    return datalist


def askURL(URL):
    # visiting web page as client but not as program
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"}
    
    request = urllib.request.Request(URL, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    
    return html


def saveData2EX(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("bdtop250", cell_overwrite_ok=True)
    col = ("详情链接","图片链接","中文名","外语名","评分","评价数","概况","相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print(f"第{i}条")
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])
    
    book.save(savepath)


def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250 (
                info_link, pic_link, cname, ename, score, rated, introduction, info)
                values(%s)'''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
