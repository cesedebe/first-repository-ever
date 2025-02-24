from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

@pytest.mark.smoke
@pytest.mark.regression
def test_new_user_registration():
    try:

        driver = webdriver.Chrome()
        driver.get('http://demostore.supersqa.com/my-account/')
        #driver.get('http://localhost/myEcommSite/my-account/')


        # generate random email address
        u_name = driver.find_element(By.CSS_SELECTOR, '#reg_email')  # Css is copied from page
        letters = string.ascii_letters
        rand_string = ''.join(random.choice(letters) for i in range (15))
        random_email = rand_string + "@randomemail.com"
        u_name.send_keys(random_email)
        time.sleep(5)

        # Enter any password
        u_name = driver.find_element(By.CSS_SELECTOR, '#reg_password')
        u_name.send_keys('myPassword123!!')
        time.sleep(5)

        # click the register button
        u_name = driver.find_element(By.NAME, 'register')
        u_name.click()


        #check that user is logged in after successful registration
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'woocommerce-breadcrumb'))).text == "Home / My account", "User not logged in after registration"
        print("TEST PASS!! -✅ User is Logged in and registered")

    except Exception as e:
        print("Test Failed ❌: ", e)

