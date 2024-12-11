import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def setup_browser(browser_choice):
    if browser_choice == 1:
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_choice == 2:
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser_choice == 3:
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise ValueError("Unsupported browser!")
    return driver

print("Which browser would you like to use?")
print("1. Chromium-based browser")
print("2. Firefox")
print("3. Edge")
browser_choice = int(input("Enter the number of your browser: "))

driver = setup_browser(browser_choice)
driver.get("https://discord.com/login")
input("Please log in to Discord, navigate to a channel and press Enter...")
js_code = """window.webpackChunkdiscord_app.push([[Math.random()],{},(req)=>{for(const m of Object.keys(req.c).map(key=>req.c[key].exports).filter(e=>e)){if(m.default&&m.default.getToken){const token=m.default.getToken();navigator.clipboard.writeText(token).then(function(){console.log('Token copied to clipboard!');}).catch(function(err){console.error('Failed to copy token: ',err);});return token;}}}]);"""
driver.execute_script(js_code)
print("Token added to clipboard.")

time.sleep(10)
driver.quit()
