from html.parser import HTMLParser
import codecs
import re
links = []
class Myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for a,b in attrs:
                if 'http' in b:
                    return(links.append(b))
def getlinks():
    gallery = []
    for x in links:
        gallery.append(re.findall(r"https:\D+\d+", x))
    print(gallery)
f = codecs.open("gal.html", 'r')
parser = Myhtmlparser()
parser.feed(f.read())
f.close()
getlinks()