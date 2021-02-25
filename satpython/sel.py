# Import the necessary modules for development
import time
from selenium import webdriver

with open('list434.txt', 'r') as furls:
    urls = furls.readlines()
chrome_options = webdriver.ChromeOptions()
with open('list43_url_https.txt', 'w') as configuration:
    configuration.write(f' {"URL": <50} {"Working[Yes/No]": <40}\n')
    for url in urls:
        driver = webdriver.Chrome(
            r"./chromedriver.exe",
            options=chrome_options)
        # urlup = "https://"+url.strip()
        # print(urlup)
        # driver.get(urlup)
        # driver.close()
        try:
            urlup = "https://" + url.strip()
            driver.get(urlup)

            if(driver.getTitle() != null):
                configuration.write(f' {url: <50} {"Yes": <40}\n')
            else:
                configuration.write(f' {url: <50} {"No": <40}\n')
        except BaseException:
            configuration.write(f' {url: <50} {"No": <40}\n')
        finally:
            driver.current_url
            # driver.get_screenshot_as_file("test.png")
            # S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
            # driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
            # driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
            driver.quit()
            driver.close()
