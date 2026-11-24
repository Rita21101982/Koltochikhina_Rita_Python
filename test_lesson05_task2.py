from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.find_element(By.NAME, "custname").click()

    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys("Рита Колточихина")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"

    driver.quit()
