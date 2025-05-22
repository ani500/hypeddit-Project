from base.selenium_driver import SeleniumDriver
import os
import time
from urllib.parse import urlparse, urljoin


class ScreenSave(SeleniumDriver):
    aLocator = 'a'
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
        self.SCREENSHOT_DIR = 'Files1'
        os.makedirs(self.SCREENSHOT_DIR, exist_ok=True)


    def takeScreen(self, baseUrl):

        links = self.getElements(self.aLocator, "tagname")
        internal_links = set()

        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith(baseUrl):
                clean_link = href.split('#')[0].rstrip('/')
                internal_links.add(clean_link)

        print(f"Found {len(internal_links)} internal links")

        # --- Take Screenshots of Each Page ---
        for url in internal_links:
            try:
                self.driver.get(url)
                time.sleep(5)  # Wait for page to load

                parsed = urlparse(url)
                slug = parsed.path.strip('/').replace('/', '_') or 'home'
                filename = f"{slug}.png"
                filepath = os.path.join(self.SCREENSHOT_DIR, filename)

                self.driver.save_screenshot(filepath)
                print(f"Saved screenshot: {filepath}")
            except Exception as e:
                print(f"Failed to screenshot {url}: {e}")





