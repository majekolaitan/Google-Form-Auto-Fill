from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScXbCCt7aQPhdO1-__0zZQBbezoLlvkMRAqtQyKVJIytS1ErA/viewform?usp=sf_link')

data = pd.read_csv('data.csv')

# Assuming the order of the CSV columns matches the order of the input fields
for idx, row in data.iterrows():
    time.sleep(2)
    
    # Find all text input elements
    text_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    
    # Loop through each text input element and the corresponding data in the row
    for i, input_element in enumerate(text_inputs):
        # Send the data to the input element
        # Use the i-th column's value from the row
        input_element.send_keys(row[i])

    # Submit the form
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    time.sleep(2)

    # Click on the link to submit another response
    submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
