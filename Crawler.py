
"""
import requests
import pandas as pd
import pandas as np
link = 'http://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_download.php?l=zh-tw&d=107/02/09&s=0,asc,0'
link2= 'http://pala.tw/js-example/'
reqs = requests.get(link2)

print(reqs.text)
if reqs.ok:    
    print ("Request Get")
else:
    print ("Request not Get")
print ("Done")
"""

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'請輸入路徑')  # PhantomJs
driver.get('http://pala.tw/js-example/')  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
print(pageSource)