import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    for i in range (1,3):
        
        driver.get(f"https://www.mathworks.com/matlabcentral/fileexchange/?page={i}&amp;sort=date_desc_updated")
        
        elements = driver.find_elements(By.CSS_SELECTOR, "div.card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width a")
        # elements = driver.find_elements(By.CSS_SELECTOR,"div.card_container div.card_body div.panel div.panel-heading h3")
        for i in elements:
            # texts.append(i.text)
            texts.append(i.get_attribute("href"))
        # elements.
    # print(texts)
    print(len(elements))
    print(len(texts))
    print(texts)
    print(len(set(texts)))


gettingMultipleItems()




# .card_container.explorer_view.add_long_title.add_card_bg_null.add_fixed_width