from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver executable
chrome_driver_path = "/path/to/chromedriver"  # Update this path

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the ChromeDriver service
service = Service(chrome_driver_path)

# Start the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Your search function
def search_google_web_automation(query):
    driver.get(f"https://www.google.com/search?q={query}")
    # Perform your search actions here

# Example query
query = "example search"
search_google_web_automation(query)

# Close the driver
driver.quit()
