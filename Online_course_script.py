import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

str1 = input("你的学号")
num = int(input("当前学习进度"))-1

# 设置 Chrome 浏览器选项
options = Options()
options.headless = True  # 启用无头模式
options.add_argument("--disable-gpu")  # 禁用 GPU 加速
options.add_argument("--no-sandbox")  # 禁用沙盒模式
options.add_argument("--disable-dev-shm-usage")  # 禁用共享内存
options.add_argument("--disable-extensions")  # 禁用扩展
options.add_argument("--disable-images")  # 禁用图片加载
options.add_argument("--blink-settings=imagesEnabled=false")  # 禁用 CSS 样式
options.add_argument("--disable-javascript")  # 禁用 JavaScript（如果不需要 JavaScript 可以启用）

# 启动 Chrome 浏览器，自动下载兼容的 ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)


# driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://zjbti.rymooc.com/")
driver.find_element(By.XPATH, '//*[@id="header-wrap"]/nav/div/div/div[2]/div[1]/div/a/span').click()
time.sleep(1)
driver.find_element(By.ID, 'Email').send_keys(f"{str1}")
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
