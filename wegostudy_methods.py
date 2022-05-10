from selenium import webdriver
from time import sleep
import datetime

from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select

from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




# s = Service(executable_path='../chromedriver.exe')
# driver = webdriver.Chrome(service=s)



def setUp():
    print(f'launch {locators.app} App')
    print(f'--------------------------------------')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to moodle App website
    driver.get(locators.wegostudy_url)
    # check that  moodle URL and the home page title are as expected
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f' Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title; {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(1.5)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.wegostudy_url:
        driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
        sleep(1)
        driver.find_element(By.ID, 'user_email').send_keys(locators.admin_email)
        sleep(1)
        driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
        sleep(1)
        driver.find_element(By.XPATH, '//input[@name="commit"]').click()
        sleep(6)



def log_out():

        driver.find_element(By.CSS_SELECTOR, 'span[class="my-auto mr-2 pf-name"]').click()
        sleep(1)
        driver.find_element(By.XPATH, '//a[normalize-space()="Log out"]').click()
        sleep(1)
        driver.find_element(By.ID, 'authentication-popup').is_displayed()
        sleep(1)
        print(f'********* LOG OUT IS SUCCUSSEFUL  {datetime.datetime.now()}********************')


# def create_new_student():
#     # if driver.current_url == locators.wegostudy_url:
#         print(f'********* Create  new user ***********************')
#         driver.find_element(By.XPATH,'//span[normalize-space()="My WeGoStudy"]').click()
#         sleep(1)
#         driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
#         sleep(1)
#         driver.find_element(By.LINK_TEXT, 'Create New Student').click()
#         # driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm"]').click()
#         sleep(1.25)
#         # driver.find_element(By.XPATH, 'a[contains(., "Create New Student")]').click()
#         # assert driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm"]').click()
#         # driver.find_element(By.CSS_SELECTOR, 'btn.btn-green.btn-sm').click()
#         sleep(1.25)
#         driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
#         sleep(1.25)
#         driver.find_element(By.ID, 'user_student_detail_attributes_middle_name').send_keys(locators.middle_name)
#         sleep(1.25)
#         driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
#         sleep(1.25)
#         driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.full_name)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_birth_date"]').click()
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//th[normalize-space()="March 2012"]').is_displayed()
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//td[normalize-space()="25"]').is_displayed()
#         sleep(1.25)
#         # driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_birth_date"]').click()
#
#         # driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').is_displayed()
#         driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.ssn)
#         sleep(1.25)
#         driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
#         sleep(1.25)
#         Select(driver.find_element(By.ID, 'user_student_detail_attributes_country_of_citizenship')).select_by_value("CA")
#         # driver.find_element(By.XPATH, '//input[@role="searchbox"]').send_keys(locators.country)
#         sleep(1.25
#         driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
#         sleep(1.25)
#         driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.address)
#         sleep(1.25)
#         driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_country').click()
#         sleep(1.25)
#         # Select(driver.find_element(By.XPATH, '//a[@class="chosen-single"]//span[contains(text(),"Country")]')).select_by_visible_text(locators.country)
#         Select(driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_country')).select_by_value("CA")
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//span[normalize-space()="Province/State"]').send_keys(locators.province)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//a[@class="chosen-single"]//span[contains(text(),"City")]').send_keys(locators.city)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_address_attributes_zip_code"]').send_keys(locators.postalcode)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//a[@class="btn btn-green-br ml-auto btn-xs form-group add_fields"]').send_keys(locators.education)
#         Select(driver.find_element(By.XPATH, '//span[normalize-space()="Credentials"]')).select_by_visible_text(locators.credentials)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_school_name"]').send_keys(locators.school_name)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_program"]').send_keys(locators.program)
#         sleep(1.25)
#         Select(driver.find_element(By.XPATH, '//a[@class="chosen-single"]//span[contains(text(),"GPA Scale")]')).select_by_visible_text(locators.gpa_scale)
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_gpa"]').send_keys(locators.gpa)
#         sleep(1.25)
#         driver.find_element(By.LINK_TEXT, '- Remove Education').click()
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//a[@class="btn btn-green-br ml-auto btn-xs mb-3 add_fields"]').click()
#         sleep(1.25)
#



setUp()
log_in()
log_out()
# create_new_student()
tearDown()
