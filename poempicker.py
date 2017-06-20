import urllib.request
import bs4
import markovify

urls = [
    'http://mek.oszk.hu/01000/01006/html/vs184602.htm',
    'http://mek.oszk.hu/00500/00588/html/vers1401.htm',
    'http://mek.oszk.hu/06200/06266/html/tragedia0002.html'
]

def get_text_url(url):
    return bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser").find("body").get_text()

def get_poems(raw, delimiter = "\n\n\n\xa0\n\n\n\n"):
    return raw.split(delimiter)

def generate_poems(text, number = 10):
    text = text.replace('\r\n', '<br>')
    model = markovify.Text(text)
    content = '<div>'
    for i in range(number):
        sentence = str(model.make_sentence())
        if (sentence != 'None'):
            content += sentence
    content += '</div>'
    return content
