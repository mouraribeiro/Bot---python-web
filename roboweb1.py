from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
import time
import xlrd


abre_arquivo = xlrd.open_workbook(r'C:\Users\rayan\OneDrive\Área de Trabalho\CURSO BOT\robowebteste.xls')
sheet = abre_arquivo.sheet_by_name('Planilha1') 
linhas = sheet.nrows
colunas = sheet.ncols
arq_txt=open('resultado.txt',"w") 

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://registro.br/")


for i in range(0,linhas):
    x = sheet.cell_value(i,0)
    pesquisa = driver.find_element(By.ID,"is-avail-field")
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong') modelo antigo de xpath
    driver.find_element(by =By.XPATH, value='//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    texto= "Domínio %s %s \n" % (x, driver.find_element(by =By.XPATH, value='//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
    arq_txt.write(texto)

arq_txt.close()
driver.close() 



