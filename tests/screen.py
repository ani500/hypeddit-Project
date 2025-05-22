#from PIL import Image, ImageChops

#image_1= Image.open("C:\\Users\\pc\\Desktop\\New folder (3)\\new music\\1.jpg")
#image_2=Image.open("C:\\Users\\pc\\Desktop\\New folder (3)\\new music\\3.jpg")
#difference_0= ImageChops.difference(image_1,image_2)
#difference_0.show()

import os
import time
from urllib.parse import urlparse, urljoin

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# --- Configuration ---
BASE_URL = 'https://hypeddit.com/'  # Replace with your target site
SCREENSHOT_DIR = 'Files'

# --- Setup Chrome Driver ---
#chrome_options = Options()
#chrome_options.add_argument('--headless')  # Run in headless mode
#chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Firefox()

# --- Create Screenshot Folder ---
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# --- Visit Home Page ---
driver.get(BASE_URL)
time.sleep(2)  # Wait for page to load

# --- Grab All Internal Links ---
links = driver.find_elements(By.TAG_NAME, 'a')
internal_links = set()

for link in links:
    href = link.get_attribute('href')
    if href and href.startswith(BASE_URL):
        clean_link = href.split('#')[0].rstrip('/')
        internal_links.add(clean_link)

print(f"Found {len(internal_links)} internal links")

# --- Take Screenshots of Each Page ---
for url in internal_links:
    try:
        driver.get(url)
        time.sleep(5)  # Wait for page to load

        parsed = urlparse(url)
        slug = parsed.path.strip('/').replace('/', '_') or 'home'
        filename = f"{slug}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)

        driver.save_screenshot(filepath)
        print(f"Saved screenshot: {filepath}")
    except Exception as e:
        print(f"Failed to screenshot {url}: {e}")

driver.quit()