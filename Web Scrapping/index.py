import requests
from bs4 import BeautifulSoup

def get_HTML_text(url):
    response = requests.get(url)
    response_page = response.text   
    response_status = response.status_code

    if response_status = 200:
        return response_page
    elif response_status = 403:
        raise Exception("try after some time")
    else:
        raise Exception("Error")


response_page = get_HTML_text("https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht")
response_page_soup = BeautifulSoup(response_page, "html.parser")
container = response_page_soup.find("table",{"class": "chart full-width"})
trs = container.find("tbody").findAll("tr")

#file creste
f = open("movies.csv", "w")
f.write("name, image \n")


for tr in trs:
    title = tr.find("td", {"class", "titleColumn"}).a.text
    image = tr.find("td",{"class", "posterColumn"}).a.img["src"]
    f.write(title+"," +image+ "\n" )

f.close()

print(response)
# print(response_page)
print(container)
