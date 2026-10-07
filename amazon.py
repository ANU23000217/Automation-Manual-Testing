from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

time.sleep(5)
login = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
#login = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
login.click()

time.sleep(3)
emobile = driver.find_element(By.ID, "ap_email_login").send_keys("7358591318")

time.sleep(3)
continue_button = driver.find_element(By.CLASS_NAME, "a-button-input")
continue_button.click()

password_in = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
password_in.send_keys("131894")

sign_in = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
sign_in.click()

'''otp_login =driver.find_element(By.XPATH, '//input[@id="continue"]')
otp_login.click()

otp = input("Enter OTP: ")

otp_input = driver.find_element(By.ID, "cvf-input-code")

otp_input.send_keys(otp)

verify_otp = driver.find_element(By.CLASS_NAME, "a-button-input")
verify_otp.click()
'''
search_bar = driver.find_element(By.NAME, "field-keywords")
search_bar.send_keys("guitars")
search_bar.send_keys(Keys.ENTER)
time.sleep(3)

add_cart = driver.find_element(By.XPATH, '//*[@id="a-autoid-7"]/span/input')                  
add_cart.click()

time.sleep(3)

go_to_cart = driver.find_element(By.XPATH, '//*[@id="ewc-cart-button-loaded-retail"]/span/span/a')
go_to_cart.click()

time.sleep(2)
pay = driver.find_element(By.XPATH, "//*[@id='sc-buy-box-ptc-button']/span/input")
pay.click()


input("Enter to close the brower")

driver.quit()
