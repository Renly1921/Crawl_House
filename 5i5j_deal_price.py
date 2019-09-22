# coding=UTF-8

import re
import requests
import requests_common
import csv
import json
import socket
import traceback

timeout = 3
xiaoqu_list_url = "https://hz.5i5j.com/xiaoqu/"

def prepare():
    header = requests_common.get_random_header()
    proxy_ip_list = requests_common.get_xici_ip_address_all(header, 10)
    https_ip_list = requests_common.get_all_ip_https(proxy_ip_list)
    valid_https_ip_list = requests_common.proxy_https_verify(https_ip_list)
    requests_common.save_ip_in_json(valid_https_ip_list)

def get_xiaoqu_info(page):
    valid_proxy_ip_list = requests_common.get_ip_in_json()
    while True:
        header = requests_common.get_random_header()
        proxy_ip = requests_common.get_random_ip_https(valid_proxy_ip_list)
        real_target_url = xiaoqu_list_url + page
        try:
            r = requests.get(real_target_url, timeout=timeout, headers=header, proxies=proxy_ip)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print("Successfully open web page ", real_target_url, " with proxy ip: ", proxy_ip)
            break
        except:
            print("failed open web page ", real_target_url, " with proxy ip: ", proxy_ip)
            continue
    #print(r.text)
    xiaoqu_list = re.findall('href="/xiaoqu/(\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d).html" target="_blank">', r.text, re.S)

    next_page = re.findall('<div class="pageSty rf"><a href="/xiaoqu/(.*?)/" class="cPage">下一页</a>', r.text, re.S)

    if next_page != []:
        next_page_deals = get_xiaoqu_info(next_page[0])
        print("get data from next page:", next_page[0])
        xiaoqu_list.extend(next_page_deals)
    else:
        print("Seem can not find page info with web address: ", xiaoqu_list_url)

    print(xiaoqu_list)
    return xiaoqu_list

def save_xiaoqu_list_in_json(xiaoqu_list):
    with open("xiaoqu_list.json", "w") as f:
        json.dump(xiaoqu_list, f)
    print("****************************************************")
    print("Successfully save %d xiaoqu info into json file" % len(xiaoqu_list))
    return

def get_xiaoqu_list_in_json():
    with open("xiaoqu_list.json", "r") as f:
        xiaoqu_list = json.load(f)
    print("****************************************************")
    print("Successfully get %d xiaoqu info from json file" % len(xiaoqu_list))
    return xiaoqu_list

'''
只获取一个页面的成交价格信息
def crawl_deals_info_first_page():
    valid_proxy_ip_list = requests_common.get_ip_in_json()
    while True:
        header = requests_common.get_random_header()
        proxy_ip = requests_common.get_random_ip_https(valid_proxy_ip_list)
        try:
            r = requests.get(target_url, timeout=timeout, headers=header, proxies=proxy_ip)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print("Successfully open web page with proxy ip: ", proxy_ip)
            break
        except:
            print("failed to open web page with proxy ip: ", proxy_ip)
            continue
#    print(r.text)
    # get page number info:
    temp_info = re.findall('<div class="pageSty rf">.*?下一页</a>(.*?)class="cur">', r.text, re.S)
    page_info = re.findall('<a href="/sold/.*?/(.*?)/" class="">.*?</a>', str(temp_info), re.S)
    page_info.reverse()
#    page_info.insert(0,'')
    # get deal price info:
    draft_deals = re.findall('<p class="sTit">.*?<strong>(.*?)</strong>.*?'
                       '<em class="ting"></em>(.*?)</p>.*?'
                       '<p><em class="dayTime"></em>(.*?)</p>.*?'
                       '<div class="jiage">.*?<strong>(.*?)</strong>.*?'
                       '<p>(.*?)</p>', r.text, re.S)
    print(page_info)
    return draft_deals
'''

def crawl_deals_info_recursion(page = '', xiaoqu_url=''):
    '''
    递归方式获取所有该小区的成交价格信息，默认打开的是第一页
    '''
    valid_proxy_ip_list = requests_common.get_ip_in_json()
    while True:
        header = requests_common.get_random_header()
        proxy_ip = requests_common.get_random_ip_https(valid_proxy_ip_list)
        target_url_with_page = xiaoqu_url + str(page)
        try:
            r = requests.get(target_url_with_page, timeout=timeout, headers=header, proxies=proxy_ip)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print("Successfully open web page ", target_url_with_page, " with proxy ip: ", proxy_ip)
            break
        except:
            print("failed open web page ", target_url_with_page, " with proxy ip: ", proxy_ip)
            continue
    #    print(r.text)

    # get deal price info:
    draft_deals = re.findall('<p class="sTit">.*?<strong>(.*?)</strong>.*?'
                             '<em class="ting"></em>(.*?)</p>.*?'
                             '<p><em class="dayTime"></em>(.*?)</p>.*?'
                             '<div class="jiage">.*?<strong>(.*?)</strong>.*?'
                             '<p>(.*?)</p>', r.text, re.S)

    next_page = re.findall('<div class="pageSty rf"><a href="/sold/\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d/(.*?)/" class="cPage">下一页</a>', r.text, re.S)
    if next_page != []:
        next_page_deals = crawl_deals_info_recursion(next_page[0], xiaoqu_url)
        print("get data from next page:", next_page[0])
        draft_deals.extend(next_page_deals)
    else:
        print("Seem can not find page info with web address: ", xiaoqu_url)
#    print(draft_deals)
    return draft_deals

def data_clean(draft_deals):
    deals = []
    for draft_deal in draft_deals:
        deal = ['', '', '', '', '']  # 必须要放在循环内，否则会出现append被覆盖的问题
        deal[0] = draft_deal[0].strip().split(' ')[0]
        deal[1] = draft_deal[1].strip()
        deal[2] = draft_deal[2].strip().split('：')[1]
        deal[3] = draft_deal[3].strip()
        deal[4] = draft_deal[4].strip()[2:7]
#        print(deal)
        deals.append(deal)
    return deals

def save_to_file(deals):
    headers = ['Position', 'house info', 'date', 'total price', 'price/m2']
    with open('5i5j_history_deal_price.csv', 'w', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(deals)
    return

def save_delta_to_file(deals):
    with open('5i5j_history_deal_price.csv', 'a', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(deals)
    print("Successfully save added info into CSV file！")
    return

def main():
    all_xiaoqu_deals = []

#    xiaoqu_list = get_xiaoqu_info('')
#    save_xiaoqu_list_in_json(xiaoqu_list)
    xiaoqu_list = get_xiaoqu_list_in_json()

    for xiaoqu in xiaoqu_list[0:3]:
        xiaoqu_url = "https://hz.5i5j.com/sold/" + xiaoqu + "/"
        current_xiaoqu_deals = crawl_deals_info_recursion('', xiaoqu_url)
        deals = data_clean(current_xiaoqu_deals)
        print("Successfully get history deal info from ", xiaoqu_url)
        save_delta_to_file(deals)

#        all_xiaoqu_deals.extend(current_xiaoqu_deals)
#    deals = data_clean(all_xiaoqu_deals)
#    save_to_file(deals)
#    print(deals)


if __name__ == "__main__":
    prepare()
#    main()