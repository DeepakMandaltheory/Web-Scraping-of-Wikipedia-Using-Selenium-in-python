# Importing All the Necessary Libraries
#pip install selenium 
#pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import os

##Configure -> " Chrome browser options" .

# Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Creating WebDriver instance
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion statement (Verfy the name of Website)
assert "Wikipedia" in wd.title

# Print the entire HTML
#print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by=By.ID, value="searchInput")

# Sending keys
input_element.send_keys('NSE')

# Fetch search button through CSS class name
search = wd.find_element(by=By.CLASS_NAME, value="pure-button")

# Click the search button
wd.execute_script("arguments[0].click();", search)

# Wait for page to load
time.sleep(2)  # Adjust this as needed

# Switching windows
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "NSE - Wikipedia" in wd.title

# Printing the title
print("Successfully loaded the page ", wd.title)


# ====== Fetch the NSE detail =========

# Fetch search button through link text
link_text = wd.find_element(By.LINK_TEXT, "National Stock Exchange of India")

# Clicking the link
wd.execute_script("arguments[0].click();", link_text)

# Wait for page to load
time.sleep(2)  # Adjust this as needed

# Switching window
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "National Stock Exchange of India - Wikipedia" in wd.title

# Printing the title
print("Successfully loaded the page ", wd.title)

# Fetch all elements with <p> tags
p_tags = wd.find_elements(by=By.TAG_NAME, value="p")

# Printing the array with <p> tag elements
print("Number of <p> tags found: ", len(p_tags))

# Extract text from all elements
text_lines = ''
for p_tag in p_tags:
    text_lines += p_tag.text

# Print the text
print(text_lines)

# Match all digits occurring in squared brackets in the string and replace them with an empty string
pattern = r'\[[0-9]+\]'
new_string = re.sub(pattern, '', text_lines)
print(new_string)

# Save the text to a file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "extracted_data.txt")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(new_string)

# Print the Extracted Data File in Word Format 
print(f"Extracted data saved to {file_path}")

# Extract nested elements using CSS selector
elems = wd.find_elements(by=By.CSS_SELECTOR, value='p > a')

# # Creating Dictionary of All the Elements If Required 
# link_dict = {}
# for elem in elems:
#     link_dict[elem.text] = elem.get_attribute('href')
# print(link_dict)

# Closing the browser
wd.quit()
