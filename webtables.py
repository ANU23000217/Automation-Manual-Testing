from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome()
driver.get("https://assertqa.com/practice/webtables")

heading = driver.find_element(By.XPATH, '//*[@id="employees-table"]/thead')
print("The Table Heading are: ")
print(heading.text)

first_row = driver.find_element(By.XPATH, '//*[@id="employees-table"]/tbody/tr[1]')
print("First employee record:")
print(first_row.text)

rows_dropdown = driver.find_element(By.XPATH, '//*[@id="main-content"]/main/div/div/div[3]/div[2]/div[2]/div[1]/select')
dropdown = Select(rows_dropdown)
rows_value = input("Enter number of rows(10,15,25):")
dropdown.select_by_value(rows_value)

last_row = driver.find_element(By.XPATH, f'//*[@id="employees-table"]/tbody/tr[{rows_value}]')
print("Last employee record:")
print(last_row.text)

search =driver.find_element(By.XPATH, '//*[@id="main-content"]/main/div/div/div[3]/div[1]/div[1]/div[1]/input')
name = input("Enter to search for an employee by last name:")
search.send_keys(name)

row_results = driver.find_element(By.XPATH, '//*[@id="employees-table"]/tbody/tr')
print("Employee Details Found by Last Name:")
print(row_results.text)

driver.refresh()

rows_dropdown = driver.find_element(By.XPATH, '//*[@id="main-content"]/main/div/div/div[3]/div[2]/div[2]/div[1]/select')
dropdown = Select(rows_dropdown)
rows_value = input("Enter number of rows(10,15,25):")
dropdown.select_by_value(rows_value)

mail = driver.find_elements( By.XPATH, '//*[@id="employees-table"]/tbody/tr/td[4]')
print("All Email Addresses:")
for m in mail:
    print(m.text)

print("Does the Website Link exist [ Pass or Fail]:")
links_exist = driver.find_elements(By.TAG_NAME,"a")
if len(links_exist)>0:
    print("PASS")
else:
    print("FAIL")


rows = driver.find_elements(By.XPATH, '//*[@id="employees-table"]/tbody/tr')
print("Total data rows:", len(rows))

input("Enter to close the brower....")

driver.quit()