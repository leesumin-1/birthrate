import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1428&param=013')

soup=BeautifulSoup(html, "lxml")
#print(soup)

#출생아수&출생률

birth_table = soup.find_all('div',{"class":"con_table of_auto wid100p"})

print(len(birth_table))
print(type(birth_table))
print(type(birth_table[0]))

birth_table_tbody=birth_table[0].find_all("tbody")
birth_table_tbody_row= birth_table_tbody[0].find_all("tr")

birth_info=[]
for tr in birth_table_tbody_row:
    number_of_birth=[]
    td=tr.find_all("td")
    #print(td)
    #print(len(td))
    #print("")

    for content in td:
        print(content.get_text(), end=', ')
        number_of_birth.append(content.get_text())
    print("")
    birth_info.append(number_of_birth)

print("")

#년도
year_table = soup.find_all('table',{"id":"t_Table_142801"})

print(len(year_table))
print(type(year_table))
print(type(year_table[0]))

year_table_tbody = year_table[0].find_all("thead")
year_table_tbody_row= year_table_tbody[0].find_all("tr")

year_info=[]
for tr in year_table_tbody_row:
    Year_info=[]
    td=tr.find_all("th")
    #print(td)
    #print(len(td))
    #print("")

    for content in td:
        print(content.get_text(), end=', ')
        year_info.append(content.get_text())
    print("")

print("")


