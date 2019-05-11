from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

login_url = 'http://sfrz.cug.edu.cn/tpass/login?service=http%3A%2F%2Fxyfw.cug.edu.cn%2Ftp_up%2F'

rsa = '71CD0D332BF8D926DF24F73F7CFCFF3DF48DE4021A265274AC29A35F4D283980E57B57D5694675DD3F87C346C8672F7CE7D5506C91106F5577926E18905A063303FE226734D225B86C76D6065AF6CFC7940F6A996038F2B3539ABC4D967BB535EAFE06CD5E00F07BB2FD3CCE665C710B605A05528280F48BA50C5D1683A42AAB9668FE464C1DBD45'

form_data = {
    'rsa': rsa,
    'ul': '11',
    'pl': '9',
    'lt': '',
    'execution': '',
    '_eventId': 'submit'
}

r = requests.get(login_url)
print(r.sel)
