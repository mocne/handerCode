#coding = utf-8
import urllib
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return  html
    print(html)


def getImg(html):
    reg = r'src="(./img/*?\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')   # python3以上必须加这句，不然会报错 can't use a string pattern on a bytes-like object
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x = x + 1

if __name__ == '__main__':  
    html = getHtml("http://news.ifeng.com/a/20170905/51874729_0.shtml")
    print(getImg(html))
