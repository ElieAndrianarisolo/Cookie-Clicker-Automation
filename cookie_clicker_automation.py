from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the cookie consent button to appear and click to accept
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "fc-primary-button"))
)
button_consent = driver.find_element(By.CLASS_NAME, "fc-primary-button")
button_consent.click()

# Wait for the language selection to appear and select English
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)
button_language = driver.find_element(By.ID, "langSelect-EN")
button_language.click()

# Define the IDs of key elements in the game
cookie_id = "bigCookie"  # The clickable cookie
cookies_id = "cookies"  # The element that shows the number of cookies
product_price_prefix = "productPrice"  # Prefix for product prices
product_prefix = "product"  # Prefix for product elements

# Wait for the big cookie to appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# Find the big cookie element and start clicking it
cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

# Main automation loop
while True:
    # Continuously click the big cookie
    cookie.click()

    # Get the current number of cookies and convert it to an integer
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))  # Remove commas for conversion

    # Loop through the first 4 products (can be adjusted for more products)
    for i in range(4):
        # Get the price of each product and clean it up
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        # Skip if the price is not a digit (e.g., when a product is unavailable)
        if not product_price.isdigit():
            continue

        # Convert the product price to an integer
        product_price = int(product_price)

        # Check if we have enough cookies to buy the product
        if cookies_count >= product_price:
            # If yes, find the product element and click to buy it
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break  # Exit the loop after purchasing
