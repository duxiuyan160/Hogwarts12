import urllib.request

def test_urllib():
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.status)
    print(response.read())