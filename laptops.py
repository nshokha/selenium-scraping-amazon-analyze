import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

brands = []
model_names = []
screen_sizes = []
cpu_models = []
rams = []
storages = []
operating_systems = []
prices = []
ratings = []
reviews = []
graphics = []

url = "https://www.amazon.in/s?k=laptops"
count = 1
while True:
    laptop_links = []
    for i in range(1):
        driver.get(url)
        time.sleep(3)

    laptop_urls = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal']")
    for url in laptop_urls:
        links = url.get_attribute('href')
        laptop_links.append(links)

    for link in laptop_links:
        driver.get(link)

        try:
            brand = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-brand']"
                                                    "//td[@class='a-span9']"
                                                    "//span").text
        except:
            brand = 'No brand'
        print(count)
        print('Brand:',brand)
        brands.append(brand)

        try:
            name = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-model_name']"
                                                       "//td[@class='a-span9']"
                                                       "//span").text
        except:
            name = 'No model name'
        print('Model Name:',name)
        model_names.append(name)

        try:
            model = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']"
                                                    "//td[@class='a-span9']"
                                                    "//span").text
        except:
            model = 'No cpu model'
        print('Cpu Model:', model)
        cpu_models.append(model)

        try:
            screen = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']"
                                                  "//td[@class='a-span9']"
                                                  "//span").text
        except:
            screen = 'No screen'
        print('Screen:', screen)
        screen_sizes.append(screen)

        try:
            storage = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']"
                                                     "//td[@class='a-span9']"
                                                     "//span").text
        except:
            storage = 'No storage'
        print('Storage:', storage)
        storages.append(storage)

        try:
            ram = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-ram_memory.installed_size']"
                                                    "//td[@class='a-span9']"
                                                    "//span").text
        except:
            ram = 'No ram'
        print('Ram:', ram)
        rams.append(ram)

        try:
            operating_system = driver.find_element(By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Operating System')]"
                                                        "/following-sibling::td"
                                                ).text
        except:
            operating_system = 'No operating_system'
        print('Operating_system:', operating_system)
        operating_systems.append(operating_system)

        try:
            graphic = driver.find_element(By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Graphics Card Interface')]"
                                                                "/following-sibling::td"
                                                    ).text
        except:
            graphic = 'No graphic'
        print('Graphic:', graphic)
        graphics.append(graphic)

        try:
            price = driver.find_element(By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
                                                                 "//span"
                                                      "//span[@class='a-price-whole']"
                                                     ).text
        except:
            price = 'No price'
        print('Price:', price)
        prices.append(price)

        try:
            rating = driver.find_element(By.XPATH, "//span[@class='reviewCountTextLinkedHistogram noUnderline']").text
        except:
            rating = 'No rating'
        print('Rating:', rating)
        ratings.append(rating)

        try:
            review = driver.find_element(By.XPATH, "//span"
                                                    "//span[@class='a-size-base a-text-normal']").text
        except:
            review = 'No review'
        print('Review:', review)
        reviews.append(review)

        count+=1

    try:
        next_page = driver.find_element(By.XPATH,
                                        "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        print(f"next_page_url {next_page}")
        url = next_page.get_attribute('href')
    except:
        print('This is the last page!')
        break

df = pd.DataFrame({
    'brands': brands,
    'model_names': model_names,
    'screen_size': screen_sizes,
    'cpu_models': cpu_models,
    'storages': storages,
    'rams': rams,
    'operating_systems': operating_systems,
    'prices': prices,
    'graphics': graphics,
    'ratings': ratings,
    'reviews': reviews,
})
df.to_csv('laptops.csv')










