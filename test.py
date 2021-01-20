import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome('./driver/chromedriver')

keyword = input('input：')
second_keywords = ['hoge', 'fuga', 'nyaaaaaa']
results = []

for i, second_keyword in enumerate(second_keywords):
    # 新しいタブ
    chrome.execute_script("window.open('','_blank');")
    chrome.switch_to.window(chrome.window_handles[i])

    # グーグルを開く
    chrome.get('https://www.google.co.jp')

    # 検索ワード入力
    search_box = chrome.find_element_by_name('q')
    search_words = keyword, second_keyword
    search_box.send_keys(' '.join(search_words))

    # 検索実行
    search_box.send_keys(Keys.RETURN)
    print(chrome.title)
    results.append(chrome.title)

# 先頭のタブに戻る
chrome.switch_to.window(chrome.window_handles[0])

path_w = './output/test.csv'

with open(path_w, mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(['No.', 'search result'])
    for i, result in enumerate(results):
        writer.writerow([i, result])

with open(path_w) as f:
    print(f.read())

