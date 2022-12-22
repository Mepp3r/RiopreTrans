from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv, main
#id_point = [1814, 1691, 2089, 3514, 1033]
def firefox(idPoint):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    driver = webdriver.Firefox(options=fireFoxOptions)
    driver.get("http://linhasriopreto.riopretrans.com.br/mapa/")
    driver.execute_script(f"viewNextHour({idPoint})")
    element = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[4]/div/div/div/div[2]/form/div[1]/div[2]/div/table/tbody'))).text)
    with open('cache.csv', 'w') as file_out:
        for line in element:
            file_out.write(line)
    driver.quit()

#firefox(1814)