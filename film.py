import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os

def cls():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")

def cari_film(q="avengers"):
	url = f"http://149.56.24.226/?s={q}#gsc.tab=0&gsc.q={q}&gsc.page=1"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	source=requests.get(url, headers=headers, timeout=(3.05, 27)).text
	soup = BeautifulSoup(source, 'html.parser')
	hasil = soup.find_all("div","search-item")
	judul = []
	for x in hasil:
		judul.append([x.h2.text,x.h2.a["href"]])
	return judul

def links(url):
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')

	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get(url)
	hasil = driver.find_element_by_class_name("FEMBED").get_attribute('href')
	return hasil

def play():
	pilih = cari_film(input("Judul : "))
	for x in pilih:
		print(x)
		print("-"*10)
	n=int(input("Mana : "))
	url = links(pilih[n][1])

	print(url)

	driver = webdriver.Chrome()
	driver.get(url)
	iddd = driver.find_elements_by_css_selector("div")
	# hasil = driver.find_element_by_class_name("faplbu").find_element_by_css_selector('svg').find_element_by_css_selector('path')
	# print(iddd);input()
	for x in iddd:
		try:
			x.click()
		except Exception as e:
			pass

	driver.switch_to_window(driver.window_handles[0])

	iddd = driver.find_elements_by_css_selector("div")
	for x in iddd:
		try:
			x.click()
		except Exception as e:
			pass

	driver.switch_to_window(driver.window_handles[0])
	# print(driver.find_element_by_id("vstr").get_attribute('innerHTML'));input()
	time.sleep(3)
	hasilll = driver.find_element_by_css_selector("video")
	cls()
	print("Judul: avengers")
	print("-"*20)
	for y,x in enumerate(pilih):
		print(f"{y+1}. {x[0]}")
		print("-"*20)
	print("Pilih: 1\n")
	print("Link: "+hasilll.get_attribute('src'))
if __name__ == '__main__':
	play()