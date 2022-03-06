import requests
import urllib.parse
from bs4 import BeautifulSoup






banner = '''



         _______  _______  _______  _______  ___      _______        ___  __   __  __    _  ___   _ 
        |       ||       ||       ||       ||   |    |       |      |   ||  | |  ||  |  | ||   | | |
        |    ___||   _   ||   _   ||    ___||   |    |    ___|      |   ||  | |  ||   |_| ||   |_| |
        |   | __ |  | |  ||  | |  ||   | __ |   |    |   |___       |   ||  |_|  ||       ||      _|
        |   ||  ||  |_|  ||  |_|  ||   ||  ||   |___ |    ___|   ___|   ||       ||  _    ||     |_ 
        |   |_| ||       ||       ||   |_| ||       ||   |___   |       ||       || | |   ||    _  |
        |_______||_______||_______||_______||_______||_______|  |_______||_______||_|  |__||___| |_|

                                                            Script by Agun
                                                    


'''

blacklist = ['support.google.com', 'accounts.google.com']

print(banner)
dorks = input("Enter Your dork: ")
page_num = input(" Enter Page Number: ")
int_page_num = int(page_num)
mainurl = f"https://www.google.com/search?q={dorks}&start="


proxie = {
    'http': "88.198.50.103:3128",
    'http': "88.198.24.108:8080",
    'http': "176.9.75.42:3128",
}

def single_scrap(url, page, proxie):

    request = requests.get(url+str(page), proxies=proxie).text

    soup = BeautifulSoup(request, 'html.parser')

    links = soup.findAll('a')

    idnt = "&sa"
    for x in links:
        y = x['href']
        if y.startswith("/url?q="):
            gg = y.replace("/url?q=", "")
            hr = gg.split("&sa=")
            hk = hr[0]
            gf = hk.split("//")[1]
            k = gf.split("/")[0]
            if k in blacklist:
                pass
            else:
                enc = urllib.parse.unquote(hk)
                print(enc)

page = 0

for x in range(int_page_num):
    single_scrap(mainurl, page, proxie)
    page += 10

