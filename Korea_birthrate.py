import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1428&param=013")
soup = BeautifulSoup(html, "lxml")

birthrate_table = soup.find_all('table', {"id":"t_Table_142801"})
print(len(birthrate_table))
print(type(birthrate_table))
print(type(birthrate_table[0]))

birthrate_table_tbody=birthrate_table[0].find_all("tbody")
birthrate_table_tbody_row=birthrate_table_tbody[0].find_all("tr")

birthrate_info=[]
for tr in birthrate_table_tbody_row:
    year_birthrate_info=[]
    td=tr.find_all("td")

    for content in td:
        print(content.get_text(), end=', ')
        year_birthrate_info.append(content.get_text())
    print("")
    birthrate_info.append(year_birthrate_info)

print("")

birthrate_table = soup.find_all('table', {"id":"t_Table_142801"})
print(len(birthrate_table))
print(type(birthrate_table))
print(type(birthrate_table[0]))

birthrate_table_tbody=birthrate_table[0].find_all("thead")
birthrate_table_tbody_row=birthrate_table_tbody[0].find_all("tr")

birthrate_info=[]
for tr in birthrate_table_tbody_row:
    year_birthrate_info=[]
    td=tr.find_all("th")

    for content in td:
        print(content.get_text(), end=', ')
        year_birthrate_info.append(content.get_text())
    print("")
    birthrate_info.append(year_birthrate_info)

print("")
