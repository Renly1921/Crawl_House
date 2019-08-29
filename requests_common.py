# coding=UTF-8
"""
basic function for urllib
"""

import re
import urllib.request
import urllib.error
import requests
import random
import json


TIMEOUT = 1
HTTPS_VERIFY_URL = "https://www.xxorg.com/tools/checkproxy/"
HTTP_VERIFY_URL = "http://icanhazip.com/"

DEBUG_TAG = 1

def debug_print(data):
    if DEBUG_TAG == 1:
        print(data)

def get_random_header():
   user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        # iPhone 6：
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",]

   header = {'User-Agent': random.choice(user_agent)}
   print("current header info as: ", header)
   return header



def get_xici_ip_address(header):
    target_url = "https://www.xicidaili.com/nn/1"
    try:
        resp = requests.get(target_url, timeout=TIMEOUT, headers=header)
        resp.encoding = resp.apparent_encoding
        html = resp.text
    except:
        html = ""
        print("ERROR -- unable to open www.xicidaili.com")
    ips = re.findall('alt="Cn" /></td>.*?'
                     '<td>(.*?)</td>.*?'
                     '<td>(.*?)</td>.*?'
                     '<td>.*?</td>.*?'
                     '<td class="country">.*?</td>.*?'
                     '<td>(.*?)</td>', html, re.S)
    ip_list = []
    for ip in ips:
        if ip[2] == "HTTP":
            proxy_ip = {'http': 'http://' + str(ip[0]) + ":"+ str(ip[1])}
        elif ip[2] == "HTTPS":
            proxy_ip = {'https': 'https://' + str(ip[0]) + ":"+ str(ip[1])}
        ip_list.append(proxy_ip)
    if ip_list == []:
        print("No proxy ip found from https://www.xicidaili.com/nn/1")
    else:
        print("Successfully get %d proxy ip address from https://www.xicidaili.com/nn/1" % len(ip_list))
    debug_print("Debug: detail proxy info found from https://www.xicidaili.com/nn/1: " + str(ip_list))
    return ip_list

def get_ip_in_json():
    with open("proxy_ip_pool.json", "r") as f:
        ip_list = json.load(f)
    print("Successfully get %d proxy ip info from json file" % len(ip_list))
    debug_print("Debug: detail proxy info found from json file: " + str(ip_list))
    return ip_list

def save_ip_in_json(ip_list):
    with open("proxy_ip_pool.json", "w") as f:
        json.dump(ip_list, f)
    print("Successfully save %d proxy ip info into json file" % len(ip_list))
    return

def get_random_ip_http(ip_list):
    http_ip_list = []
    for ip in ip_list:
        for key in ip:
            if key == "http":
                http_ip_list.append(ip)
            else:
                continue
    if http_ip_list == []:
        print("Warning: can not get random http proxy ip from list")
        return []
    else:
        debug_print("Total " + str(len(http_ip_list)) + " proxy found")
        random_proxy = random.choice(http_ip_list)
        print("Successfully get random http proxy ip in use. info: ", random_proxy)
        return random_proxy

def get_random_ip_https(ip_list):
    https_ip_list = []
    for ip in ip_list:
        for key in ip:
            if key == "https":
                https_ip_list.append(ip)
            else:
                continue
    if https_ip_list == []:
        print("Warning: can not get random https proxy ip from list")
        return []
    else:
        debug_print("Total " + str(len(https_ip_list)) + " proxy found")
        random_proxy = random.choice(https_ip_list)
        print("Successfully get random https proxy ip in use. info: ", random_proxy)
        return random_proxy

def get_all_ip_http(ip_list):
    http_ip_list = []
    for ip in ip_list:
        for key in ip:
            if key == "http":
                http_ip_list.append(ip)
            else:
                continue
    if http_ip_list == []:
        print("Warning: can not find http proxy ip info from list")
        return []
    else:
        print("Successfully find total ", len(http_ip_list), " http proxy in")
        return http_ip_list

def get_all_ip_https(ip_list):
    https_ip_list = []
    for ip in ip_list:
        for key in ip:
            if key == "https":
                https_ip_list.append(ip)
            else:
                continue
    if https_ip_list == []:
        print("Warning: can not find https proxy ip info from list")
        return []
    else:
        print("Successfully find total ", len(https_ip_list), " https proxy in")
        return https_ip_list

def proxy_http_verify(ip_list):
    header = get_random_header()
    valid_http_ip_list = []
    for ip in ip_list:
        try:
            resp = requests.get(HTTP_VERIFY_URL, headers=header, proxies=ip, timeout=TIMEOUT, verify=False)
            if resp.status_code == 200:
                valid_http_ip_list.append(ip)
                debug_print("Debug: Successfully find valid http proxy ip: " + str(ip))
            else:
                debug_print("Debug; Proxy may works, but failed to open web page, error info: " + str(resp.status_code) + str(ip))
        #        except (requests.exceptions):
        except Exception:
            debug_print("Debug: Invalid proxy ip: " + str(ip))
    print("Successfully find valid http proxy ip as: ", valid_http_ip_list)
    return valid_http_ip_list

def proxy_https_verify(ip_list):
    header = get_random_header()
    valid_https_ip_list = []
    for ip in ip_list:
        try:
            resp = requests.get(HTTPS_VERIFY_URL, headers=header, proxies=ip, timeout=TIMEOUT, verify=False)
            if resp.status_code == 200:
                valid_https_ip_list.append(ip)
                debug_print("Debug: Successfully find valid https proxy ip: " + str(ip))
            else:
                debug_print("Debug; Proxy may works, but failed to open web page, error info: " + str(resp.status_code) + str(ip))
        #        except (requests.exceptions):
        except Exception:
            debug_print("Debug: Invalid proxy ip: " + str(ip))
    print("Successfully find valid https proxy ip as: ", valid_https_ip_list)
    return valid_https_ip_list