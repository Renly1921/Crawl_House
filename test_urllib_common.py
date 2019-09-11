# coding=UTF-8

import re
import urllib.request
import urllib.error
import urlllib_common
import socket

timeout = 5

def main():
    socket.setdefaulttimeout(timeout)
    header = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
#    header = urlllib_common.get_random_header()
#    ip_list = urlllib_common.get_xici_ip_address(header)
#    urlllib_common.save_ip_in_json(ip_list)
#    proxy_ip = urlllib_common.get_random_ip(protocal_type="https", ip_list=ip_list)
    proxy_ip = {'http': '120.236.128.201:8060'}
    if proxy_ip == []:
        return
    else:
        proxy = urllib.request.ProxyHandler(proxy_ip)
        https_handler = urllib.request.HTTPSHandler(debuglevel=1)
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
#        req = urllib.request.Request(url='https://www.xxorg.com/tools/checkproxy/', headers=headers)
#        with urllib.request.urlopen(req) as response:
#            data = response.read().decode('utf-8')
        req = urllib.request.Request(url="http://icanhazip.com/", headers=header)

        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')

#        try:
#            data = urllib.request.urlopen(req).read().decode('utf-8')
#        except urllib.request.URLError as e:
#            print(proxy_ip, "出现异常: " + str(e))
#            return
        print(data)
#        print(proxy_ip, '验证通过--  ')


if __name__ == "__main__":
    main()
