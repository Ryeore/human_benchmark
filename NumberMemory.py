from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

elements = {
    "number": (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]"),
    "agree": (By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'),
    "start": (By.XPATH, "//button[contains(text(),'Start')]"),
    "input_field": (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]"),
    "submit": (By.XPATH, "//button[contains(text(),'Submit')]"),
    "next_stage": (By.XPATH, "//button[contains(text(),'NEXT')]")

}


def test_login_form(browser):
    def element_locator(elem):
        try:
            found_elem = WebDriverWait(browser, 3600).until(
                EC.element_to_be_clickable(elem)
            )
            return found_elem
        except NoSuchElementException:
            print(f"{elem} was not found")

    browser.get("https://humanbenchmark.com/tests/number-memory")
    element_locator(elements["agree"]).click()
    element_locator(elements["start"]).click()

    while True:
        number = element_locator(elements["number"])
        answer = number.text
        # print(answer)
        input_field = element_locator(elements["input_field"])
        input_field.send_keys(answer)
        element_locator(elements["submit"]).click()
        element_locator(elements["next_stage"]).click()


driver = webdriver.Chrome()
test_login_form(driver)
