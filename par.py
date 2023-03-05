
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# Create your views here.


def home(request):
    visuword = request.POST.get['visuword']
    str = "https://api.datamuse.com/words?ml=" + visuword
    html = urlopen(str)
    soup = BeautifulSoup(html, 'html.parser')
    type(soup)
    posts = soup.get_text
    print(posts)
    context = {'posts': posts}
   

