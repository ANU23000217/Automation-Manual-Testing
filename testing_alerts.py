from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
print( "The website name is:" ,driver.title)

wait = WebDriverWait(driver, 10)

#This tests alerts: click me
click_me =driver.find_element(By.ID, "alert")
click_me.click()
time.sleep(3)
alert = wait.until(EC.alert_is_present())
print("The alert Message is:")
print(alert.text)
alert.accept()

time.sleep(2)

#Let's make the prompt happen
prompt_happen = driver.find_element(By.ID, "prompt")
prompt_happen.click()
time.sleep(2)
alert = wait.until(EC.alert_is_present())
print("The prompt_happen Alert Message is:", alert.text)
alert.accept()

time.sleep(2)

#A SLOW alert
slow = driver.find_element(By.ID, "slow-alert")
slow.click()
time.sleep(2)
alert = wait.until(EC.alert_is_present())
print("The Slow Alert Message is:",alert.text)
alert.accept()

time.sleep(2)

#This is a test of a confirm: test confirm
test_confirm = driver.find_element(By.ID, "confirm")
test_confirm.click()
time.sleep(2)
test_alert = wait.until(EC.alert_is_present())
print("The Test Confirm Alert Message is:", test_alert.text)
test_alert.accept()
time.sleep(2)
driver.back()

time.sleep(2)

#This is a test of an alert open from onload event handler: open new page
open_new_page = driver.find_element(By.ID, "open-page-with-onload-alert")
open_new_page.click()
time.sleep(2)
alert_open = wait.until(EC.alert_is_present())
print("The Open New Page shows Alert Message as:", alert_open.text)
alert_open.accept()
time.sleep(2)
driver.back()

'''original_window = driver.current_window_handle
open_new_window = driver.find_element(By.ID, "open-window-with-onload-alert")
open_new_window.click()
wait.until(EC.number_of_windows_to_be(2))
for window in driver.window_handles:
    if window != original_window:
        driver.switch_to.window(window)
        break
time.sleep(3)
print("Switched to the new window")
alert_window = wait.until(EC.alert_is_present())
print("The Open New Window Alert Message is:", alert_window.text)
alert_window.accept()
time.sleep(3)
print("Alert accepted")
driver.switch_to.window(original_window)'''

print("Switched back to the original window")

input("Enter to close the browser...")
driver.quit()
