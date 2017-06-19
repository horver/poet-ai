import urllib.request
import bs4

def get_text_url(url):
    return bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser").find("body").get_text()

def get_poems(raw, delimiter = "\n\n\n\xa0\n\n\n\n"):
    return raw.split(delimiter)

def main():
    poems = get_poems(get_text_url("http://mek.oszk.hu/01000/01006/html/vs184602.htm#28"))
    print(poems)

if __name__ == "__main__":
    main()
