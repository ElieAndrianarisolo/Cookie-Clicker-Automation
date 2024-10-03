# Cookie Clicker Automation with Selenium

## Project Overview
This project is an introductory exercise for using Selenium with Python. The objective is to automate actions on a simple web-based game called **Cookie Clicker**. This project demonstrates how Selenium can be used to interact with web elements, automate user input, and simulate clicks and other interactions on a webpage.

## Prerequisites
- Basic understanding of Python
- **Selenium** installed in Python:
  ```bash
  pip install selenium
  ```
- Download and install **ChromeDriver** for your version of Chrome, and place it in your project directory. 

## Libraries Used:
- **Selenium**: A Python library used to automate web browser interaction.
- **WebDriverWait**: To wait for elements to load before interacting with them.
- **Expected Conditions (EC)**: To define specific conditions to wait for, such as an element being clickable or present.

## Features:
1. **Cookie Clicking**: Automatically clicks on the big cookie in the Cookie Clicker game.
2. **Auto-purchase Upgrades**: The script reads the number of cookies earned, checks if enough cookies are available, and then purchases upgrades.
3. **Handling Pop-ups**: It demonstrates how to manage cookies consent pop-ups and language selection on a website.
   
## How to Use:
1. Download the project files and place **chromedriver.exe** in the project directory.
2. Install Selenium by running:
   ```bash
   pip install selenium
   ```
3. Run the script. The script will:
   - Open the Cookie Clicker game.
   - Accept the cookies consent pop-up.
   - Set the language to English.
   - Start clicking the big cookie.
   - Automatically buy upgrades as cookies are accumulated.
   
## Key Sections:
- **WebDriver Setup**: 
  Initializes the Chrome browser using Selenium WebDriver with:
  ```python
  driver = webdriver.Chrome(service=service)
  ```
  
- **Cookie Consent and Language Selection**: 
  Handles the pop-up consent and sets the language to English using Selenium's element locators and click events.

- **Main Automation Loop**:
  Continuously clicks the cookie and buys upgrades whenever there are enough cookies.

## Conclusion:
This project provides a hands-on introduction to Selenium in Python by automating a web-based game. It's a fun way to discover how Selenium can be used to interact with web pages and simulate user actions, which is a valuable skill for web scraping, testing, and automation tasks. 
