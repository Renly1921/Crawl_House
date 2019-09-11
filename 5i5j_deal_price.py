# coding=UTF-8

import re
import requests
import requests_common
import csv
import socket
import traceback

timeout = 3
target_url = "https://hz.5i5j.com/sold/100000000003563/"

def prepare():
    header = requests_common.get_random_header()
    proxy_ip_list = requests_common.get_xici_ip_address_all(header, 30)
    https_ip_list = requests_common.get_all_ip_https(proxy_ip_list)
    valid_https_ip_list = requests_common.proxy_https_verify(https_ip_list)
    requests_common.save_ip_in_json(valid_https_ip_list)

def crawl_deals_info():
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
    draft_deals = re.findall('<p class="sTit">.*?<strong>(.*?)</strong>.*?'
                       '<em class="ting"></em>(.*?)</p>.*?'
                       '<p><em class="dayTime"></em>(.*?)</p>.*?'
                       '<div class="jiage">.*?<strong>(.*?)</strong>.*?'
                       '<p>(.*?)</p>', r.text, re.S)
#    print(draft_deals)
    return draft_deals

def data_clean(draft_deals):
    deals = []
    for draft_deal in draft_deals:
        deal = ['', '', '', '', '']  # 必须要放在循环内，否则会出现append被覆盖的问题
        deal[0] = draft_deal[0].strip()
        deal[1] = draft_deal[1].strip()
        deal[2] = draft_deal[2].strip()
        deal[3] = draft_deal[3].strip()
        deal[4] = draft_deal[4].strip()
        deals.append(deal)
    return deals

def save_to_file(deals):
    headers = ['Position', 'house info', 'data', 'total price', 'price/m2']

    with open('test.csv', 'w', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(deals)


def main():
#    prepare()
    draft_deals = crawl_deals_info()
    deals = data_clean(draft_deals)
    save_to_file(deals)
#    print(deals)


if __name__ == "__main__":
    main()