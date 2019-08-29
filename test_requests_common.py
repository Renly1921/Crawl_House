# coding=UTF-8

import re
import requests
import requests_common
import socket
import traceback



def main():
    target_url = "https://www.xxorg.com/tools/checkproxy/"
    target_url = "http://icanhazip.com/"
    timeout = 1
    header = requests_common.get_random_header()

#    ip_list = requests_common.get_xici_ip_address(header)
    ip_list = requests_common.get_ip_in_json()
#    requests_common.save_ip_in_json(ip_list)
    http_ip_list = requests_common.get_all_ip_http(ip_list)
    print(http_ip_list)
    requests_common.proxy_http_verify(http_ip_list)
#            data.raise_for_status()
#            data.encoding = data.apparent_encoding
#            print(data.text)
#            data = urllib.urlopen(target_url, proxies=proxy_ip).read()
#        except Exception as e:
#           http_ip_list.remove(proxy_ip)
#            continue





'''
    proxy_ip = {'http': '120.236.128.201:8060', 'https': '120.236.128.201:8060'}
    try:
        r = requests.get(target_url, timeout=timeout, headers=header, proxies=proxy_ip)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
        print("ok")
    except:
        print("error")
'''





if __name__ == "__main__":
    main()
