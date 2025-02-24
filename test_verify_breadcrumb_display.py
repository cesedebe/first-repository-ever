from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.smoke
@pytest.mark.regression
def test_breadcrumb_display():
    try:

        driver = webdriver.Chrome()
        driver.get('http://demostore.supersqa.com/product/belt/')
        #driver.get('http://localhost/myEcommSite/product/belt/')


        # Find the breadcrumb element (modify the selector if needed)
        breadcrumb_element = driver.find_element(By.CLASS_NAME, "woocommerce-breadcrumb")


        # Expected breadcrumb text
        expected_breadcrumb = "Home / Clothing / Accessories / Belt"

        # Verify the breadcrumb text matches
        actual_breadcrumb = breadcrumb_element.text.strip()
        assert actual_breadcrumb == expected_breadcrumb, f"Breadcrumb mismatch! Found: {actual_breadcrumb}"


        print("TEST PASS!! ✅ Breadcrumb is correctly displayed!")

    except Exception as e:
        print("Test Failed ❌: " , e )

