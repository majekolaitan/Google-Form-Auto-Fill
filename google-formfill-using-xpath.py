from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScnzPyjHlxzBISYbiX6i3WpjDdMmLw9iK0vPY47mxyKtPhYDA/viewform')

data = pd.read_csv('data.csv')

for idx, row in data.iterrows():
    time.sleep(2)

    gender = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender.send_keys(row['Gender'])

    # Age
    age = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    age.send_keys(row['Age'])

    # Occupation
    occupation = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    occupation.send_keys(row['Occupation'])

    # Education Level
    education_level = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    education_level.send_keys(row['Education Level'])

    # Frequency of Technical Issues
    tech_issues_freq = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    tech_issues_freq.send_keys(row['Frequency of Technical Issues'])

    # Technical Problems
    tech_problems = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    tech_problems.send_keys(row['Technical Problems'])

    # Methods of Distribution
    distribution_methods = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    distribution_methods.send_keys(row['Methods of Distribution'])

    # Important Factors
    important_factors = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
    important_factors.send_keys(row['Important Factors'])

    # Likelihood of Using Platform
    platform_likelihood = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')
    platform_likelihood.send_keys(row['Likelihood of Using Platform'])

    # Expected Features
    expected_features = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')
    expected_features.send_keys(row['Expected Features'])

    # User Friendly Expectations
    user_friendly_expectations = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')
    user_friendly_expectations.send_keys(row['User Friendly Expectations'])

    # Willingness to Provide Personal Info
    personal_info_willingness = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input')
    personal_info_willingness.send_keys(row['Willingness to Provide Personal Info'])

    # Customer Support Importance
    customer_support_importance = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')
    customer_support_importance.send_keys(row['Customer Support Importance'])


    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    time.sleep(2)

    submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()





















