import urllib.request as url_request
import urllib.error as url_error

def get_HTML(url, data=None, username=None, password=None):
    response = fetch_response(url, data ,username, password)
    return _get_HTML_text(response)

def fetch_response(url, data=None, username=None, password=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    request = url_request.Request(url, data=None, headers=headers)
    return url_request.urlopen(request)

def _get_HTML_text(response):
    try:
        charset = response.info().get_content_charset()
        htmlBytes = response.read()
        if charset is not None:
            htmlStr = htmlBytes.decode(charset)
        else:
            htmlStr = htmlBytes.decode('utf-8')
        return htmlStr
        # except url_error.HTTPError as e:
        #     raise e
    except Exception as e:
        raise e