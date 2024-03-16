import time
from selenium import webdriver
from selenium.webdriver.common.by import By
str1 = input("你的学号")
num = int(input("当前学习进度"))-1
driver = webdriver.Chrome()
driver.get("https://zjbti.rymooc.com/")
driver.find_element(By.XPATH, '//*[@id="header-wrap"]/nav/div/div/div[2]/div[1]/div/a/span').click()
time.sleep(1)
driver.find_element(By.ID, 'Email').send_keys(f"23021111{str1}")
driver.find_element(By.ID, 'Password').send_keys("ryxy123A!")
driver.find_element(By.XPATH, '//*[@id="loginForm"]/form/div[5]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="header-wrap"]/nav/div/div/div[2]/div[1]/div/div[1]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="header-wrap"]/nav/div/div/div[2]/div[1]/div/ul/li[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div/div/div[1]/a/img').click()
time.sleep(1)
for i in range(33):
    driver.find_elements(By.CLASS_NAME, 'clue-popover')[i+num].click()
    time.sleep(1)
    b = driver.find_element(By.XPATH, '//*[@id="item-number"]/span[4]').text
    for j in range(int(b)):
        a = driver.find_element(By.XPATH, '//*[@id="player-bottom"]/div[3]/a[2]')
        time.sleep(1)
        driver.execute_script("arguments[0].removeAttribute('disabled')", a)
        a.click()
        time.sleep(1)
