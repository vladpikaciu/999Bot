from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--headless")#


PATH = "C:/Users/vladpikaciu/Desktop/999Bot-main/chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get("https://999.md/ro/profile/vladpikaciu")

description = """Se vinde server in stare buna, pentru mai multe detalii despre hard diskuri sau altceva scrieti in privat. Serverul a fost cumparat din Marea Britanie cu 5 luni in urma. Nu a fost folosit pentru mining. Se vinde din motiv ca am cumparat unul mai nou.
Procesor................2x Intel Xeon E5-2420 (1.9 GHz-2.4GHz, 6 core 12 thread)
Memorie.................16 GB DDR3 (Max 192 GB)
Internet................HP Ethernet 1Gb 4-port 366i Adapter
Gestionare la distanța..HP iLO (Firmware: HP iLO 4)
Raid Controller.........HP Dynamic Smart Array B120i Controller for SATA drives
Alimentare..............2 X 460W
Stocare.................2X 500GB 7200k HDD
Railurile sunt incluse.
"""

def anunt_add():
    add_ad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#js-add-ad"))
    )
    add_ad.click()
    add_config = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#js-pjax-container > div > div.form-pjax-container.category-form > section > div > div.form-element__prepare > form > ul > li:nth-child(4) > a"))
    )
    add_config.click()
    driver.find_element(By.CSS_SELECTOR,
                        "#js-pjax-container > div > div.form-pjax-container.category-form > section > div > div.form-element__prepare > form > div > ul:nth-child(1) > li:nth-child(1) > ul > li:nth-child(2) > a").click()
    driver.find_element(By.ID, "control_12").send_keys("HP ProLiant DL360e Gen8")
    driver.find_element(By.ID, "control_13").send_keys(description)
    select = Select(driver.find_element_by_id("control_7"))
    select.select_by_value("12900")
    driver.find_element_by_id("control_2").send_keys("5100")
    select = Select(driver.find_element_by_id("control_673"))
    select.select_by_value("7369")
    select = Select(driver.find_element_by_id("control_593"))
    select.select_by_value("6371")
    select = Select(driver.find_element_by_id("control_949"))
    select.select_by_value("20707")
    select = Select(driver.find_element_by_id("control_674"))
    select.select_by_value("7371")
    sleep(2)
    select = Select(driver.find_element_by_id("control_675"))
    select.select_by_value("20720")
    driver.find_element_by_css_selector("#control_676").click()
    driver.find_element_by_css_selector("#control_676").send_keys("1900")
    select = Select(driver.find_element_by_id("control_677"))
    select.select_by_value("7387")
    select = Select(driver.find_element_by_id("control_679"))
    select.select_by_value("7404")
    select = Select(driver.find_element_by_id("control_1244"))
    select.select_by_value("23183")
    select = Select(driver.find_element_by_id("control_683"))
    select.select_by_value("7411")
    select = Select(driver.find_element_by_id("control_681"))
    select.select_by_value("7408")

    try:
        driver.find_element_by_id("fileupload-file-input").send_keys(
            "C:/Users/vladpikaciu/Desktop/999Bot-main/s-l1600.jpg")
        driver.find_element_by_id("fileupload-file-input").send_keys(
            "C:/Users/vladpikaciu/Desktop/999Bot-main/s-l1600 (1).jpg")
        driver.find_element_by_id("fileupload-file-input").send_keys(
            "C:/Users/vladpikaciu/Desktop/999Bot-main/s-l1600 (2).jpg")
        driver.find_element_by_id("fileupload-file-input").send_keys(
            "C:/Users/vladpikaciu/Desktop/999Bot-main/s-l1600 (4).jpg")
    except:
        print("Imagini uploadate")
    sleep(2)
    driver.find_element_by_id("agree").click()
    driver.find_element_by_css_selector("#js-add-form > section.board__content__group.container_25 > div > div > button").click()
    print("Anunt postat")

def login():
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "autentificare"))
    )
    login.click()
    nume = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    nume.send_keys(**PASSWORD**)
    driver.find_element(By.NAME, "login").send_keys("vladpikaciu2@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".login__form__footer__submit").click()


#############################Start########################
try:
    anunt = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT , "HP ProLiant DL360e Gen8"))
    )
    anunt.click()
    sleep(2)
    login()
    sleep(3)
    driver.find_element(By.LINK_TEXT, "Ştergere").click()
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/footer/button[1]").click()
    print("Anunt sters")
    anunt_add()
except:
    try:
        login()
        anunt_add()
        sleep(1)
        ##aaa = driver.current_url[-25:]
    except:
        driver.quit()
        print("Nu sa putut adauga anuntul")
finally:
    print("Script complet")
    driver.quit()
