from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scraping(driver):
    data = {}
    data["Title"] = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/h1").text
    data["Price"] = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[3]/div/div[1]/div[1]/div/div").text
    data["Location"] = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/a/span").text
    data["Date"] = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]").text
    data["ID"] = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[2]/span").text
    atts = driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[2]/div[1]/div[4]/ul/li")

    for att in atts:
        try:
            key = att.find_element(By.XPATH, "span[1]").text
            value = att.find_element(By.XPATH, "span[2]").text
        except:
            key = att.find_element(By.XPATH, "span").text
            value = att.find_element(By.XPATH, "a").text

        data[key] = value

    data["Text"] = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[2]/div[1]/div[8]/div").text

    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section[1]/div/div[3]/div/div[1]/div[2]/div").click()
    try:
        driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/button[1]").click()
    except:
        pass
    time.sleep(2)
    try:
       data["Phone"] = driver.find_element(By.XPATH, "/html/body/div[12]/div[2]/div/a").text
    except:
       data["Phone"] = driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/a").text
    try:
       driver.find_element(By.XPATH, "/html/body/div[12]/div[1]/button").click()
    except:
       driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/button").click()
  

    return data


url = "https://www.unegui.mn/l-hdlh/l-hdlh-treesllne/oron-suuts/"

driver = Driver(uc=True, headless=False)
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()

datalist = []
for i in range(1, 61):
     driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div[{i}]/div[2]/a").click()
     data = scraping(driver)
     datalist.append(data)
     driver.back()

df = pd.DataFrame(datalist)
df.to_csv("C:/git/Homework/Week4/Data/scraped_data.csv",   index=False, encoding='utf-8-sig')


