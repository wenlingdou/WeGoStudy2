import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
import WeGoStudy_locators as locators
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'Test starts at {datetime.datetime.now()}.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.app_url)

    if driver.current_url == locators.app_url and locators.homepage_title in driver.title:
        print(f'{locators.app} website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch successfully, please check your code and launch again!')
        print(f'Current URL: {driver.current_url}, Current page title: {driver.title}.')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'---------The test is passed.----------------')
        print(f'---------The test is completed on {datetime.datetime.now()}.-------------')
        sleep(0.5)
        driver.close()
        driver.quit()

def login():
    driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'user_email').send_keys(locators.admin_email)
    sleep(0.25)
    driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@value="SIGN IN"]').click()
    sleep(0.5)
    driver.find_element(By.ID,'authentication-popup').is_displayed()
    sleep(3)
    print('------------Signed up successfully!-----------------')

def create_new_student():
    if driver.current_url==locators.login_page_url:
        print(f'----------Current URL: {locators.login_page_url}--------')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(0.25)
    if driver.current_url==locators.student_page_url:
        print(f'-------------Create New Student----------------------')
    driver.find_element(By.XPATH, '//a[normalize-space()="Create New Student"]').click()
    sleep(0.25)

    # date of birth
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('1')
    sleep(1.5)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(10*Keys.BACKSPACE)
    sleep(1.5)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.birthday)
    sleep(0.5)

    # select citizenship
    driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
    sleep(1.25)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(locators.country)
    sleep(1.25)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.RETURN)
    sleep(1.25)

    # select country
    driver.find_element(By.CLASS_NAME, 'chosen-single').click()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'chosen-search-input').send_keys('Canada')
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'chosen-search-input').send_keys(Keys.RETURN)
    sleep(0.25)

    # select province
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_state_chosen').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys('British Columbia')
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys(Keys.RETURN)
    sleep(0.25)

    # select city
    driver.find_element(By.XPATH, '//span[contains(.,"City")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys('Vancouver')
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys(Keys.RETURN)
    sleep(0.25)

    # select Credentials
    driver.find_element(By.XPATH, '//span[contains(., "Credentials")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys('Degree')
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(Keys.RETURN)
    sleep(0.25)

    # select GPA Scale
    driver.find_element(By.XPATH, '//span[contains(., "GPA Scale")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys('100')
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(Keys.RETURN)
    sleep(0.25)


    for i in range(len(locators.lst_column)):
        clm, fid, val = locators.lst_column[i], locators.lst_id[i], locators.lst_value[i]
        driver.find_element(By.ID, fid).send_keys(str(val))
        sleep(0.25)

    driver.find_element(By.XPATH, '//input[@value="Save"]').click()
    sleep(0.5)
    driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
    sleep(0.25)
    print('-------------Student is created successfully.-----------')




setUp()
login()
create_new_student()
tearDown()



