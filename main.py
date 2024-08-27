import requests
# 目標網址
base_url = 'https://www.ptt.cc/bbs/'

# 目標看板
target_board = 'Stock'

# 目標頁面
target_page = '/index'

# 目標頁面的頁數
page_num = ''

# 目標頁面的頁面的附屬檔名
html_ext = '.html'

# 合併完整路徑
target = base_url + target_board + target_page + page_num + html_ext


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

'''
常數區塊
'''
# 目標網址
BASE_URL = 'https://www.ptt.cc/bbs/'
# 目標頁面
TARGET_PAGE = '/index'
# 目標頁面的頁面的附屬檔名
HTML_EXT = '.html'


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}




'''
執行參數
'''''
page_num=''
target_board='Stock'
arget = BASE_URL + target_board + TARGET_PAGE + page_num + HTML_EXT
def download_html(target,hearders=HEADERS):
    #data=requests.get(target,headers=headers)
    #return data
    return requests.get(target,headers=headers)
'''
test
'''
x=download_html(target)
print(x.content)