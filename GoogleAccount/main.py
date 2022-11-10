from selenium import webdriver
from selenium.webdriver.common.by import By
import names
import random
import string
import os
import sys
import time
import csv


def gen_name():
    return names.get_full_name(gender='male').split()


def random_value(i=10):
    unique_value = ''.join(random.choice(
        string.ascii_letters + string.digits)for x in range(i))
    return unique_value


def chrom(url): 
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = os.path.join(sys.path[0], 'chromedriver.exe')
    service = webdriver.chrome.service.Service(executable_path=driver)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver


def input_name(driver):
    fname, lname = gen_name()
    lastname = driver.find_element('id', 'lastName')  # lastname
    lastname.clear()
    lastname.send_keys(lname)
    firstname = driver.find_element('id', 'firstName')  # firstname
    firstname.clear()
    firstname.send_keys(fname)


def input_username(driver):
    head = random_value(i=4).lower()
    tail = random.randint(1000000, 10000000)
    username = driver.find_element('id', 'username')
    username.clear()
    username.send_keys(f'{head}{tail}')
    return f'{head}{tail}@gmail.com'


def input_password(driver):
    passwd = random_value(12)
    password = driver.find_element('name', 'Passwd')
    password.clear()
    password.send_keys(passwd)
    confirmpasswd = driver.find_element('name', 'ConfirmPasswd')
    confirmpasswd.clear()
    confirmpasswd.send_keys(passwd)
    return passwd


def next(driver):
    xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
    driver.find_element(By.XPATH, xpath).click()


def input_phone(driver, phone_num):
    xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div[2]/div[1]/label/input'
    phone = driver.find_element(By.XPATH, xpath)
    phone.clear()
    phone.send_keys(phone_num)


def input_validate(driver, code):
    xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input'
    validate = driver.find_element(By.XPATH, xpath)
    validate.clear()
    validate.send_keys(code)


def input_info(driver, recovery_email):
    # backupmail
    backupmail = driver.find_element('name', 'recoveryEmail')
    backupmail.clear()
    backupmail.send_keys(recovery_email)
    # year
    year = driver.find_element('name', 'year')
    year.clear()
    year.send_keys('1992')
    # month
    month_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[2]/div/div/div[2]/select/option[2]'
    month = driver.find_element(By.XPATH, month_xpath)
    month.click()
    # day
    day = driver.find_element('name', 'day')
    day.clear()
    day.send_keys('22')
    # gender
    gender_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[4]/div[1]/div/div[2]/select/option[3]'
    gender = driver.find_element(By.XPATH, gender_xpath)
    gender.click()


def click_skip(driver):
    xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/span'
    skip = driver.find_element(By.XPATH, xpath)
    skip.click()


def write_to_csv(email, password):
    csv_path = os.path.join(sys.path[0], 'gmail.csv')
    with open(csv_path, newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, password])


def main():
    google_signup_url = 'https://accounts.google.com/signup'
    phone = '<phone_number>'
    recovery_email = '<recovery_email>'
    driver = chrom(google_signup_url)
    time.sleep(30)
    input_name(driver)
    email = input_username(driver)
    password = input_password(driver)
    next(driver)
    time.sleep(3)
    input_phone(driver, phone)
    next(driver)
    code = input('Validation code: ')
    input_validate(driver, code)
    next(driver)
    time.sleep(3)
    input_info(driver, recovery_email)
    next(driver)
    time.sleep(3)
    click_skip(driver)
    time.sleep(3)
    next(driver)
    write_to_csv(email, password)


if __name__ == '__main__':
    main()
