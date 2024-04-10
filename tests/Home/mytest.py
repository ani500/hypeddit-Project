from selenium import webdriver
from PIL import Image

driver = webdriver.Firefox()

mylist = ["https://www.hypeddit.com/aboutus","https://www.google.com"]
length = len(mylist)

for i in range(length):
    driver.get(mylist[i])
    print("F:\\New folder\\" + mylist[i] + ".png")

    driver.save_screenshot("F:\\New folder\\anil"+ str(i) + ".png")






