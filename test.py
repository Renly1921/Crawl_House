# coding=UTF-8


import re
import urllib.request
import urllib.error


def main():
    target_url = "https://www.xicidaili.com/nn/1"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    proxy_ip = {'https': 'https://1.198.72.29:9999/'}
#        print(proxy_ip)
    proxy = urllib.request.ProxyHandler(proxy_ip)
    http_handler = urllib.request.HTTPHandler(debuglevel=1)
    https_handler = urllib.request.HTTPSHandler(debuglevel=1)
#        print(proxy)
    opener = urllib.request.build_opener(proxy, https_handler)
#    request = urllib.request.Request("https://www.xxorg.com/tools/checkproxy/")
#    response = opener.open(request)
#    print(response.read().decode('utf-8'))

    urllib.request.install_opener(opener)
    try:
        data = urllib.request.urlopen('https://www.xxorg.com/tools/checkproxy/').read().decode('utf-8')
    except urllib.request.URLError as e:
        print(proxy_ip, "出现异常: " + str(e))
        return
    print(data)
    print(proxy_ip, '验证通过--  ')


if __name__ == "__main__":
    main()

