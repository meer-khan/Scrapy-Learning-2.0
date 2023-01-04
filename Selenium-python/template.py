import traceback
from datetime import datetime

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

t = 1
timeout = 10

debug = False

headless = False
images = False
maximize = False

incognito = False


def pprint(msg):
    try:
        print(f"{datetime.now()}".split(".")[0], msg)
    except:
        traceback.print_exc()




def gettingMultipleItems():
    texts = []
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    for i in range (1,2):
        
        driver.get(f"https://www.mathworks.com/matlabcentral/fileexchange/?page={i}&amp;sort=date_desc_updated")
        
        elements = driver.find_elements(By.CSS_SELECTOR, "div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width a")
        # elements = driver.find_elements(By.CSS_SELECTOR,"div.card_container div.card_body div.panel div.panel-heading h3")
        
        # print(elements)
        for i in range(0,len(elements),2):
            # texts.append(i.text)
            texts.append(elements[i].get_attribute("href"))
        # elements.
    # print(texts)
    # print(len(elements))
    # print(len(texts))
    # print(texts)

    return driver, texts
    # print(len(set(texts)))

def getDatafromInnerPage(driver, urls):
    repoName = []
    for i in urls:
        # time.sleep()
        driver.get(i)
        name = driver.find_element(By.CSS_SELECTOR, "h2[class='add_font_color_emphasize add_margin_5'] span")
        name = name.text
        repoName.append(name)
    
    print(repoName)





def main():
    driver = getChromeDriver()
    driver.get("https://www.mathworks.com/matlabcentral/fileexchange/?page=1&amp;sort=date_desc_updated")
    gettingMultipleItems()
    
    input("Done")
    


def click(driver, xpath, js=False):
    if js:
        driver.execute_script("arguments[0].click();", getElement(driver, xpath))
    else:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


def getElement(driver, xpath):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))


def getElements(driver, xpath):
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))


def sendkeys(driver, xpath, keys, js=False):
    if js:
        driver.execute_script(f"arguments[0].value='{keys}';", getElement(driver, xpath))
    else:
        getElement(driver, xpath).send_keys(keys)


def getChromeDriver(proxy=None):
    options = webdriver.ChromeOptions()
    if debug:
        # print("Connecting existing Chrome for debugging...")
        options.debugger_address = "127.0.0.1:9222"
    else:
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--user-data-dir=C:/Selenium1/ChromeProfile')
    if not images:
        # print("Turning off images to save bandwidth")
        options.add_argument("--blink-settings=imagesEnabled=false")
    if headless:
        # print("Going headless")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
    if maximize:
        # print("Maximizing Chrome ")
        options.add_argument("--start-maximized")
    if proxy:
        # print(f"Adding proxy: {proxy}")
        options.add_argument(f"--proxy-server={proxy}")
    if incognito:
        # print("Going incognito")
        options.add_argument("--incognito")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def getFirefoxDriver():
    options = webdriver.FirefoxOptions()
    if not images:
        # print("Turning off images to save bandwidth")
        options.set_preference("permissions.default.image", 2)
    if incognito:
        # print("Enabling incognito mode")
        options.set_preference("browser.privatebrowsing.autostart", True)
    if headless:
        # print("Hiding Firefox")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
    return webdriver.Firefox(options)


if __name__ == "__main__":
    main()
