from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ast
from time import sleep


def get_log_pass(file):
    with open(file, "rt", encoding="utf-8") as fl:
        login_pass = ast.literal_eval(fl.read())
        return login_pass


def auth(file, hold=10):
    login_password = get_log_pass(file)
    driver = webdriver.Chrome()
    driver.get(url="https://passport.yandex.ru/auth/")
    WebDriverWait(driver=driver, timeout=hold).until(
        EC.presence_of_element_located((By.XPATH, '//button [@data-type="login"]'))
    )

    driver.find_element(By.XPATH, '//button [@data-type="login"]').click()
    WebDriverWait(driver=driver, timeout=hold).until(
        EC.presence_of_element_located((By.ID, "passp-field-login")))

    elem = driver.find_element(By.ID, "passp-field-login")
    elem.clear()
    elem.send_keys(login_password['login'])
    driver.find_element(By.ID, "passp:sign-in").click()
    WebDriverWait(driver=driver, timeout=hold).until(
        EC.presence_of_element_located((By.ID, "passp-field-passwd")))

    elem = driver.find_element(By.ID, "passp-field-passwd")
    elem.clear()
    elem.send_keys(login_password['password'])
    driver.find_element(By.ID, "passp:sign-in").click()
    WebDriverWait(driver=driver, timeout=hold).until(
        EC.presence_of_element_located((By.XPATH, '//button [@data-t="button:action"]')))

    # Sending sms code
    driver.find_element(By.XPATH, '//button [@data-t="button:action"]').click()
    WebDriverWait(driver=driver, timeout=hold).until(
        EC.presence_of_element_located((By.XPATH, '//form [@method="post"]')))

    # code_ = input("Input secret code: ")
    # Try to enter sms code into a form
    sms_code = 111000
    elem = driver.find_element(By.TAG_NAME, 'ul')
    elem.send_keys(sms_code)
    sleep(10)


if __name__ == "__main__":
    auth("Enter.txt")
