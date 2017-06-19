import urllib.request
import bs4

def get_text_url(url):
    return bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser").find("body").get_text()

def get_poems(raw, delimiter = "\n\n\n\xa0\n\n\n\n"):
    return raw.split(delimiter)
