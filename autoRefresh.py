from selenium import webdriver
import time

#Paste the path were your webdriver is located
PATH = "C:\Program Files\chromedriver.exe"

#Open Chrome webbrowser
driver = webdriver.Chrome(PATH)
driver.get("PASTE YOUR URL HERE")

#The time frequence is set to 5 seconds
while True:
    time.sleep(5)
    driver.refresh()
driver.quit()