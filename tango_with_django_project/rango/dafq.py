__author__ = 'Nikolay'
import urllib2
import re
import json
code = u'\xe2\x98\x85'
code2 = u'\xe2\x84\xa2'
replace = {' ':'%20', '(':'%28', ')':'%29', '\\xe2\\x98\\x85':'%E2%98%85', '\\xe2\\x84\\xa2':'%E2%84%A2'}
import time

def replaceString(name):
    global replace
    for i,j in replace.iteritems():
        name = name.replace(i,j)
    return name
def searchHandle(item):

    global code
    global code2
    item = item.replace(" ","+")
    page = urllib2.urlopen("http://steamcommunity.com/market/search?q="+item)
    html = page.read()
    regex = '<span id="result_0_name" class="market_listing_item_name" style="color: (.+?);">(.+?)</span>'
    pattern = re.compile(regex)
    result = re.findall(pattern,html)
    if not result:
        return False
    result = str(result[0]).split("'")
    colorCode = result[1]
    name = result[3]
    urlName = replaceString(name)

    if name.find('\\xe2\\x98\\x85') != -1:
        name = name.replace('\\xe2\\x98\\x85', code.encode("latin-1").decode("utf-8"))

    if name.find('\\xe2\\x84\\xa2') != -1:
        name = name.replace('\\xe2\\x84\\xa2', code2.encode("latin-1").decode("utf8"))

    request = urllib2.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name="+urlName)
    info = json.load(request)
  #  print info
    info['name'] = name
 #   print("--- %s seconds ---" % (time.time() - start_time))
 #   print info['name'], info['median_price'], info['volume']
    return info

##item = raw_input('Name of item: ')
#searchHandle(item)

#print urllib2.urlopen("http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=StatTrak%E2%84%A2%20M4A1-S%20|%20Hyper%20Beast%20%28Minimal%20Wear%29").read()
