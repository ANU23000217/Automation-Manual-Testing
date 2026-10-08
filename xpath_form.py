from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")
first_name = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]').send_keys("Anu Radha")
last_name = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys("N")

address = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys("ZXM , abc Street, LKJH Nagar, chennai - 6000012")

email = driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[3]/div[1]/input').send_keys("anuradha123@gmail.com")

phone = driver.find_element(By.XPATH, '//input[contains(@type, "tel")]').send_keys("1010101010")

gender_F = driver.find_element(By.XPATH, '//input[@value = "FeMale"]').click()

hobbies = driver.find_element(By.XPATH, '//input[@type = "checkbox" and @id= "checkbox2"]').click()

skills = driver.find_element(By.XPATH, '//*[@id="Skills"]')
dropdown = Select(skills)
dropdown.select_by_value('Art Design')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span').click()
time.sleep(2)
country = driver.find_element(By.XPATH, '//input[@class ="select2-search__field"]')
country.send_keys("India")
country.send_keys(Keys.ENTER)

years = driver.find_element(By.XPATH, '//*[@id="yearbox"]')
dropdown = Select(years)
dropdown.select_by_value('2005')

month= driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
dropdown = Select(month)
dropdown.select_by_value('August')

days = driver.find_element(By.XPATH, '//*[@id="daybox"]')
dropdown = Select(days)
dropdown.select_by_value('9')

password = driver.find_element(By.XPATH, '//input[@id="firstpassword"]').send_keys("123makasjd")
confirm_password = driver.find_element(By.XPATH, '//input[@id="secondpassword"]').send_keys("123makasjd")

'''submit_button = driver.find_element(By.XPATH, '//button[text()=" Submit "]').click()
'''
time.sleep(3)
refresh_button = driver.find_element(By.XPATH, '//button[text()="Refresh"]').click()

input("Enter to close the brower....")
driver.quit()