from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManage

# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()



def launchBrowser():
    '''
    This function configures the chrome browser manually, from the chromedriver.exe
    which may be helpful in future 
    '''
    # chrome_options = Options()
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.python.org/")
    driver.maximize_window()
    print(driver.title)
    # driver.close


def launchBrowserWebdriver():
    pass

# def launchBrowser():
#    chrome_options = Options()
#    chrome_options.binary_location="../Google Chrome"
#    chrome_options.add_argument("disable-infobars");
#    driver = webdriver.Chrome(chrome_options=chrome_options)

#    driver.get("http://www.google.com/")
launchBrowser()