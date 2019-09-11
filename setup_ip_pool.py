# coding=UTF-8
"""
判断integration portal上LSV的状态，如果是绿色，就发送邮件通知
"""

import re
import urllib.request
import urllib.error



def get_ip_address(target_url,headers):
    req = urllib.request.Request(url=target_url, headers=headers)
    with urllib.request.urlopen(req) as response:
       html = response.read().decode('utf-8')
#    print(html)
    ips = re.findall('alt="Cn" /></td>.*?'
                     '<td>(.*?)</td>.*?'
                     '<td>(.*?)</td>.*?'
                     '<td>.*?</td>.*?'
                     '<td class="country">.*?</td>.*?'
                     '<td>(.*?)</td>', html, re.S)
    print(ips)
    return ips

def verify_ip_address(ips):
    ip_list = []
    for ip in ips[0:20]:
        proxy_ip = {ip[2]: str(ip[0])+":"+str(ip[1])+"/"}
        if ip[2] == "HTTP":
            proxy_ip = {'http': 'http://' + str(ip[0]) + ":"+ str(ip[1])}
            http_handler = urllib.request.HTTPHandler(debuglevel=0)
            proxy = urllib.request.ProxyHandler(proxy_ip)
            opener = urllib.request.build_opener(proxy, http_handler)
        elif ip[2] == "HTTPS":
            proxy_ip = {'https': 'https://' + str(ip[0]) + ":"+ str(ip[1])}
            https_handler = urllib.request.HTTPSHandler(debuglevel=0)
            proxy = urllib.request.ProxyHandler(proxy_ip)
            opener = urllib.request.build_opener(proxy, https_handler)
        print(proxy_ip)
        urllib.request.install_opener(opener)

#        header = {
#            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#        req = urllib.request.Request(url='https://www.xxorg.com/tools/checkproxy/', headers=header)
#        with urllib.request.urlopen(req) as response:
#            data = response.read().decode('utf-8')
#            print(data)

        try:
            data = urllib.request.urlopen('https://www.xxorg.com/tools/checkproxy/').read().decode('utf-8')
        except urllib.request.URLError as e:
            print(proxy_ip, "出现异常: " + str(e))
            continue
#        print(data)
        print(proxy_ip, '验证通过--  ')
        ip_list.append(ip)

    print(ip_list)
    return ip_list


def main():
    target_url = "https://www.xicidaili.com/nn/1"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    ips = get_ip_address(target_url, headers)
    verify_ip_address(ips)

if __name__ == "__main__":
    main()

