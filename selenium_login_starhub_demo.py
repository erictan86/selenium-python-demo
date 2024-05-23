from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

username = "" # input your username
password = "" # input your password
target_url = 'https://www.starhub.com/personal.html'

driver = webdriver.Chrome(service=Service(os.path.expanduser("~/Downloads/chromedriver.exe")))
driver.get(target_url)
driver.maximize_window()

def click_single_element_on_page(element_xpath):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
    driver.find_element(By.XPATH, element_xpath).click()
    print(f"{element_xpath} clicked")

def send_elements_to_login_page(username_xpath, password_xpath, login_btn_xpath):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    driver.find_element(By.XPATH, username_xpath).send_keys(username)
    driver.find_element(By.XPATH, password_xpath).send_keys(password)
    driver.find_element(By.XPATH, login_btn_xpath).click()
    print(f"{login_btn_xpath} clicked")

def switch_to_iframe(iframe_xpath):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, iframe_xpath)))
    iframe = driver.find_element(By.XPATH, iframe_xpath)
    driver.switch_to.frame(iframe)

def main():
    click_single_element_on_page('//*[@id="dropdownMenu2"]/span')
    click_single_element_on_page('//*[@id="btnLogin"]')
    switch_to_iframe(iframe_xpath='//*[@id="iam-popup-login"]')
    send_elements_to_login_page('//*[@id="form_fake_uid"]', '//*[@id="inputpassword"]','//*[@id="submit"]')

main()