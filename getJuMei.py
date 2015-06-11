import urllib2
import json
import xlwt
from datetime import datetime


baseURL = 'http://www.jumeiglobal.com/ajax_new/getDealsByPage?type=new&pagesize='

pageSize = 200

otherURL = '&index=0&page=global&callback=global_load_callback'

targetURL = baseURL + str(pageSize) + otherURL

xlsFileAddr = '/home/eric/dev/jumei'

isSoldOut = False

#data = urlopen(targetURL).read()
data = ''
#req = urllib2.Request(targetURL)

try:
    data = urllib2.urlopen(targetURL).read()
except urllib2.URLError as e:
    print e.reason
else:
    print 'Get Jumei data: OK!!!'



data = data.replace('global_load_callback','')[1:-1]

data = json.loads(data)

items = data['list']


lens = len(items)

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YYhh:mm:ss')

wb = xlwt.Workbook()
ws = wb.add_sheet('Ju Mei Global')
ws.write(0, 0,'Time:'+ str(datetime.now()))
ws.write(0, 1,'Name 1')
ws.write(0, 2,'Name 2',)
ws.write(0, 3,'Buyer Number')
ws.write(0, 4, 'Price')
ws.write(0, 5, 'Status')

rawNum = 1
for l in items:
    ws.write(rawNum, 0, rawNum)
    ws.write(rawNum, 1, l['pro_stitle'])
    ws.write(rawNum, 2, l['medium_name'])
    ws.write(rawNum, 3, l['price_home'])
    ws.write(rawNum, 4, l['buyer_number'])

    if l['pro_status'] == 1:
        ws.write(rawNum, 5, 'On Sale')
    else:
        if l['pro_status'] == 2:
            ws.write(rawNum, 5, 'Sold Out')
    rawNum += 1

#wb.save('/Users/binchen/dev/jumei/data/JuMei.xls')
wb.save('JuMei.xls')




