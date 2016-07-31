#coding=utf-8
import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getInformation(html):
    infDict = {}
    reg = r'<!--#.-->.{0,10}</td>'
    comreg = re.compile(reg)
    items = re.findall(comreg, html)
    print items # this is used to verify the items

    infDict['Current Station ID:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'l']
    infDict['Car Position Index:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'p']

    infDict['DOOR1 State:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'd']
    infDict['DOOR2 State:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'm']
    infDict['DOOR3 State:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'q']
    infDict['DOOR4 State:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'a']
    infDict['DOOR5 State:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'u']
    infDict['DOOR6 State:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'u']

    infDict['DOOR Open Time:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'n']
    infDict['DOOR Close Time:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'b']

    infDict['DOOR Open Ready Time:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'b']
    infDict['DOOR Close Ready Time:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'c']

    infDict['Entered Car Code:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'k']

    infDict['CAN Communication:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'e']
    infDict['IS Obstacles:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'o']
    infDict['NRF Communication:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 'f']
    infDict['Obstacle Stop:'] = [(item.split('<')[1])[8:] for item in items if item[5] == 's']
    return infDict


'''
def getItem(html):
    reg = r'href=".+?\.png" sizes'
    comre = re.compile(reg)
    item = re.findall(reg, html)
    x = 0
    for imgurl in item:
        urllib.urlretrieve("https://static.zhihu.com/static/revved/img/ios/touch-icon-152.87c020b9.png", '%s.png' % x)
        x += 1
    return item
'''
html = getHtml("http://192.168.1.30/STM32F407STATUS.shtml")
a  = getInformation(html)
print a
