import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.trukky.com/door-to-door-goods-delivery")
time.sleep(7)

pickup_city = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/form/div/div[1]/input')
pickup_city.send_keys("Hyderabad")
time.sleep(1)

select_pickup_city = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/form/div/div[1]/div/ul/li[1]')
select_pickup_city.click()
time.sleep(1)

drop_city = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/form/div/div[2]/input')
drop_city.send_keys("Delhi")
time.sleep(1)

select_drop_city = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div/form/div/div[2]/div/ul/li[1]')
select_drop_city.click()

check_price_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/form/button')
check_price_button.click()
time.sleep(3)

service_type_personal = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/ul/li[2]')
service_type_personal.click()
time.sleep(2)

select_load_service_few = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/ul/li[1]')
select_load_service_few.click()
time.sleep(2)

add_material = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div/div[1]')
add_material.click()
time.sleep(1)

choose_material = driver.find_element(By.XPATH, '//*[@id="form_0"]/div[1]/div[2]/select')
choose_material.click()

window_ac = driver.find_element(By.XPATH, '//*[@id="form_0"]/div[1]/div[2]/select/option[7]')
window_ac.click()

no_of_items = driver.find_element(By.XPATH,'//*[@id="form_0"]/div[2]/div/div[2]/input')
no_of_items.send_keys('2')

item_next_button = driver.find_element(By.XPATH, '//*[@id="form_0"]/div[3]/button')
item_next_button.click()
time.sleep(1)

next_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/button')
next_button.click()
time.sleep(2)

calendar_strafe_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div/div/div[1]/button[4]')
calendar_strafe_button.click()
calendar_strafe_button.click()
calendar_strafe_button.click()

select_date = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div/div/div[2]/div/div/div/div[2]/button[29]')
select_date.click()

next_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/button')
next_button.click()
time.sleep(1)

phone_number = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/form/div/input')
phone_number.send_keys('your phonr number')
time.sleep(2)

submit_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/button')
submit_button.click()

otp = input("Enter otp: ")
otp_entry = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[1]/div[2]/div[1]/div[1]/input')
otp_entry.send_keys(otp)

next_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[1]/div[2]/div[2]/button[2]')
next_button.click()
