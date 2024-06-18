from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

def sso_login(driver):
    driver.get("https://rent.pe.ntu.edu.tw/sso2_go.php")
    username_box = driver.find_element(By.ID, "ContentPlaceHolder1_UsernameTextBox")
    password_box = driver.find_element(By.ID, "ContentPlaceHolder1_PasswordTextBox")
    submit_button = driver.find_element(By.ID, "ContentPlaceHolder1_SubmitButton")

    load_dotenv()
    username = os.getenv("ntu_username")
    password = os.getenv("ntu_password")

    username_box.send_keys(username)
    password_box.send_keys(password)
    submit_button.click()

    # handle login succes alert
    alert = driver.switch_to.alert
    alert.accept()

def fill_form(driver):
    driver.get("https://rent.pe.ntu.edu.tw/order/?Add=A:4")
    student_num_box = driver.find_element(By.NAME, "MemberType[1]")
    student_num_box.send_keys("2")
    select_time_script = (
        """
        let table_slot = document.querySelector(".SContents");
        let day_slot = table_slot.querySelector("div[d='2024-06-22']");
        let time_slot = day_slot.querySelector("a[v='21'][title*='21 ~ 22']");
        time_slot.click();
        """
    )
    driver.execute_script(select_time_script)

if __name__ == '__main__':
    start = time.time()
    driver = webdriver.Chrome()
    sso_login(driver)
    fill_form(driver)
    # step 2 confirmation
    driver.execute_script("document.getElementsByName('Send')[0].click();")
    time.sleep(5)
    # step 3 confirmation
    driver.execute_script("document.getElementsByName('Send')[0].click();")
    end = time.time()
    print(end-start)

    while True:
        time.sleep(1)