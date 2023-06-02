from selenium import webdriver
from time import sleep
driver = webdriver.Edge()

driver.get("https://www.symbolab.com/solver/step-by-step/%5Cint%20x%5Csqrt%7B4-x%5E%7B4%7D%7Ddx")
sleep(3)
selects = driver.find_elements_by_xpath("//span[@class='locked-step']")
for select in selects:
    driver.execute_script("arguments[0].setAttribute('class', 'showStepsButton')", select)