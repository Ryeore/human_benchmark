import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# Use a web driver (in this case, ChromeDriver) to open the webpage
driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/typing")

# Allow some time for the page to load dynamically generated content
time.sleep(5)  # You may need to adjust the sleep time based on the page's load time

# Get the HTML content of the page
html_content = driver.page_source

# Close the browser


# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the HTML element by its ID or other relevant attributes
# Replace 'example' with the actual ID or attributes of the element you want to extract
element = soup.find('div', class_='letters notranslate')
textInput = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[1]/div/div[2]/div")
textInput.click()
# Extract text from the element
if element:
    text = element.get_text()
    # for num in text:
    #     pyautogui.press(num)
    print(text)
    textInput.send_keys(text)
else:
    print("Element not found.")

time.sleep(20)
