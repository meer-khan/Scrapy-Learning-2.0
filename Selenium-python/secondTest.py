import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def DemoFindElementByID():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.mathworks.com/login")
    elements = driver.find_element(By.NAME,"div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width")
    print(driver.page_source)
    print("TYPEEEE",type(elements))
    print(elements)


# DemoFindElementByID()




def mathworksLogin():


    driver = webdriver.Firefox()
    driver.get("http://somedomain/url_that_delays_loading")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()




def mathworksClicking():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.mathworks.com/matlabcentral/fileexchange/?sort=date_desc_updated")
    element = driver.find_element(By.CSS_SELECTOR, "a.mwa-nav_login")
    element.click()
    # print(element.get_attribute('href'))
    # element.get_attribute('href').click()
    time.sleep(5)



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
    print(len(elements))
    print(len(texts))
    # print(texts)

    return driver, texts
    # print(len(set(texts)))

def getDatafromInnerPage(driver, urls):
    repoName = []
    for i in urls:
        driver.get(i)
        name = driver.find_element(By.CSS_SELECTOR, "h2[class='add_font_color_emphasize add_margin_5'] span")
        name = name.text
        repoName.append(name)
    
    print(repoName)

def demoJS():
    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
    driver.execute_script("window.open('https://www.mathworks.com/matlabcentral/fileexchange/?page=1&amp;sort=date_desc_updated', '_self')")
    demo_element = driver.execute_script("return document.getElementsByTagName('p')[1]")
    driver.execute_script("arguments[0].click()",demo_element)
    print(demo_element.text)
    time.sleep(10)



driver, urls = gettingMultipleItems()
getDatafromInnerPage(driver,urls)

# demoJS()



# .card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width