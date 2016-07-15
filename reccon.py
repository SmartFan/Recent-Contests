import urllib.request as req
import json
import datetime as dt

url = 'http://contests.acmicpc.info/contests.json'
page = req.urlopen(url)
buf = page.read().decode("utf8")
jsonData = json.loads(buf)

x = dt.datetime.now() + dt.timedelta(days=7)
for crt in jsonData:
    if crt['access'] == 'Private':
        continue
    crtTime = dt.datetime.strptime(crt['start_time'], '%Y-%m-%d %X')
    if crtTime < x:
        print('%14s  %30s  %s' %
              (crt['oj'], crt['name'], crtTime.strftime('%d %b %a %I:%M')))
    else:
        break
