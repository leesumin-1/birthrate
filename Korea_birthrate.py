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

#리스트 생성
year_list=[]
birth_number_list=[]
birth_rate_list=[]
a=[]

for year_info_ in birth_info:
    #print(year_info_)
    a.append(year_info_)
birth_number_list.extend(a[0])
birth_rate_list.extend(a[1])
print(birth_number_list)
print(birth_rate_list)
for year in year_info:
    year_list.extend(year_info[1:10])
    break
print(year_list)


#그래프 만들기
matplotlib.rcParams["axes.unicode_minus"]=False #폰트 깨짐 대처
plt.rc('font', family='Malgun Gothic')

x=range(len(year_list))

fig, ax1 = plt.subplots()
ax1.set_title('출생아 수 및 합계 출산율')
ax1.plot(x, birth_rate_list, '-o',color="red")
ax1.set_ylim(0,2)
ax1.set_ylabel('합계출산율')

ax2=ax1.twinx() # x축 공유하겠다
ax2.bar(x, birth_number_list, color="gray")
ax2.set_ylim(300,500)
ax2.set_xlabel('년도')
ax2.set_ylabel('출산아 수')

ax1.set_zorder(ax2.get_zorder() + 10) # 그래프 앞뒤 위치(클수록 위쪽에)
ax1.patch.set_visible(False) #

ax1.set_xticks(x) #꺾은선그래프 위 점 찍겠다
ax1.set_xticklabels(year_list) #x축 값 설정

plt.show()