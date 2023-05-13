# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:53:29 2023

@author: LENOVO
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from matplotlib import pyplot as plt
import seaborn as sns

website="https://www.imdb.com/chart/top/"
path="C:/Users/LENOVO/Downloads/chromedriver"

driver=webdriver.Chrome(path)
driver.get(website)

rows=driver.find_elements(By.XPATH,"//tbody/tr")

ratings=[]

for row in rows:
    
    ratings.append(row.find_element(By.XPATH,".//td/strong").text)
    
    

print(ratings)

links=driver.find_elements(By.XPATH,"//tbody/tr/td[2]/a")

title=[]
year=[]
certificate=[]
duration=[]
gross=[]
country=[]
director=[]
genre=[]

for link in links:
    
    website=link.get_attribute("href")
    path="C:/Users/LENOVO/Downloads/chromedriver"
    driver=webdriver.Chrome(path)
    driver.get(website)
    
    
    
        
    title.append(driver.find_element(By.XPATH,"//h1/span").text)
    yearr=driver.find_element(By.XPATH,"//h1/../ul/li[1]/a").text
    year.append(yearr)
    print(yearr)
        
    try:   
        certificate.append(driver.find_element(By.XPATH,"//h1/../ul/li[2]/a").text)
        
    except:
        certificate.append(None)
        
    try:
        duration.append(driver.find_element(By.XPATH,"//h1/../ul/li[3]").text)
    except:
        
        duration.append(None)
    try:    
        gross.append(driver.find_element(By.XPATH,"//section[@data-testid='BoxOffice']/div/ul/li[4]/div/ul/li/span").text)
        
    except:
        gross.append(None)
        
    country.append(driver.find_element(By.XPATH,"//section[@data-testid='Details']/div[2]/ul/li[2]/div/ul/li/a").text)
    director.append(driver.find_element(By.XPATH,"//section[@data-testid='title-cast']/ul/li[1]/div/ul/li/a[1]").text)
    genre.append(driver.find_element(By.XPATH,"//a[contains(@href,'genres=')]/span").text)
        
    


imdb_dict={
    'title':title,
    'year':year,
    'certificate':certificate,
    'duration':duration,
    'gross':gross,
    'country':country,
    'director':director,
    'genre':genre,
    'ratings':ratings,
    
    }

df=pd.DataFrame(imdb_dict)
    
df.to_csv("imdb_data.csv",index=False)


# print(title)
# print(year)
# print(certificate)
# print(duration)
# print(gross)
# print(country)
# print(director)
# print(genre)