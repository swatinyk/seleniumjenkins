from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.binary_location = "/usr/local/bin/chromedriver"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox")
options.add_argument("--headless")
# driver=webdriver.Chrome(options=options,executable_path=r'/usr/local/bin/chromedriver')
driver = webdriver.Chrome(options=options)

# driver=webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get('https://www.makemytrip.com/')
# sleep(5)
#
#
# from_city=driver.find_element(By.ID,'fromCity')
# driver.execute_script("arguments[0].click();", from_city)
# sleep(5)
# from_city.send_keys('Delhi')
# Action=ActionChains(driver)
# sleep(5)
# Action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
# sleep(5)
# search=driver.find_element(By.XPATH,'//*[text()="Search"]')
# driver.execute_script("arguments[0].click();", search)
# sleep(5)
# # driver.switch_to.alert.dismiss()
# sleep(5)
# driver.find_element(By.XPATH,'//*[text()="OKAY, GOT IT!"]').click()
# sleep(5)
# last_height = driver.execute_script("return document.body.scrollHeight")
# print("last height before while loop",last_height)
# new_height=0
# while last_height != new_height:
#         last_height = new_height
#         # Scr
#         # \]ell down to the bottom.
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#         # Wait to load the page.
#         sleep(2)
#
#         # Calculate new scroll height and compare with last scroll height.
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         print("new height in while loop", new_height)
#
#         # if new_height == last_height:
#         #     flight_details = driver.find_elements(By.XPATH,
#         #                                           '//*[@class="fliCode"]/following::div[@class="priceSection"]//p')
#         #     print(len(flight_details))
#         #     break
#         #
#         # print("last height in while loop", last_height)


driver.get("https://www.swiggy.com/")
driver.find_element(By.NAME,'location').send_keys('PUNE')
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_1oLDb"]/button[last()]/span[last()]'))).click()
# print(last_option)
# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_1oLDb"]/button[3]'))).click()

count_of_restaurants=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="BZR3j"]'))).text
# count_of_restaurants=driver.find_element(By.XPATH,'//div[@class="BZR3j"]').text
int_value=count_of_restaurants.split()
print(count_of_restaurants,int_value[0])
assert int(int_value[0]) > 1000
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# sleep(5)
WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='_2GhU5']//div[@class='MZy1T']//div[@class='_3Ztcd'])[3]"))).click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//div[@class="_1RPOp"]').click()
driver.find_element(By.XPATH,'//span[@class="_1W_TH"]').click()
driver.find_element(By.XPATH,'(//label[@class="b5XpK"])[3]').click()
driver.find_element(By.XPATH,"(//label[@class='b5XpK'])[6]").click()
driver.find_element(By.XPATH,"(//label[@class='b5XpK'])[9]").click()
driver.find_element(By.XPATH,'//span[@class="_38xdN"]').click()
subtotal=driver.find_element(By.XPATH,"//div[@class='EEeV3']//div/span").text
print(subtotal)
dish=driver.find_element(By.XPATH,"//div[@class='_33KRy']").text
print(dish)
sleep(5)
