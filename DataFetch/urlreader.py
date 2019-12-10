import urllib.request as urllib


def fetch_HTML(url, data=None, username=None, password=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    request = urllib.Request(url, data=None, headers=headers)
    try:
        response = urllib.urlopen(request)
        charset = response.info().get_content_charset()
        htmlBytes = response.read()
        if charset is not None:
            htmlStr = htmlBytes.decode(charset)
        else:
            htmlStr = htmlBytes.decode('utf-8')
        return htmlStr
    except Exception as e:
        print(e)
