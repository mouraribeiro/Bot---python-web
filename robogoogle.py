import logging
from ssl import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

pesquisa = input(' Digite a sua pesquisa aqui: ')


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://google.com/")
time.sleep(5)

campo =  driver.find_element(By.XPATH, value = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)
time.sleep(10)

resultados = driver.find_element(By.XPATH, value= "//*[@id='result-stats']").text
print(resultados)

numero_paginas = int(resultados.split("Aproximadamente")[1].split(" resultados")[0].replace(".",""))
maximo_paginas = numero_paginas/10
print("O número máximo de páginas é {}".format(maximo_paginas))

driver.close()

