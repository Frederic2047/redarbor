from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
#Define all objets identificators, routes and actions. 

base_url = "https://www.computrabajo.com/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.colombiaFlag = "Colombialink" 
        self.place_search_input = 'place-search-input'
        self.city_input = "place-search-input"
        self.city = "Guainía"
        self.search_button = 'search-button'
        self.notification_ko = "button[onclick*='webpush_subscribe_ko(event);']"
        self.input_cargo = 'prof-cat-search-input'
        self.cargo = 'qa'
        self.salary = "//p[text()='Salario']//.."
        self.salary_filter = "//span[text()='Menos de $ 700.000']" 
        self.experiencia = "//p[text()='Experiencia']//.."
        self.experiencia_filter = "//span[text()='1 año']" 
        self.div_offers = "offersGridOfferContainer"
        self.offer = "Test automation Engineer QA"
        self.menubtn = "opt_dots"
        self.postular = "Postular"
        self.login_email = "LoginModel_Email"
        self.continue_mail_btn = "continueWithMailButton"
        self.account_name = "Name"
        self.account_surName = "SurName"
        self.account_password = "Password"
        self.account_cargo = "Cargo"
        self.account_dpto_select = "//select[@id='LocationId']"
        self.account_dpto_option = f"//ul[@class='list']/li[text()='{self.city}']"
        self.account_captcha = "CaptchaInputText"
        self.account_continue_btn = "continueButton"
        self.captcha_error = "validation-summary-errors"
        
        
        
    #########Getters:    
    def get_colombiaFlag(self):
        return self.driver.find_element(By.ID, self.colombiaFlag)
    
    def get_search_place_input(self):
        return self.driver.find_element(By.ID, self.city_input)
        
    def get_type_place_input(self):
        return self.driver.find_element(By.ID, self.city)
        
    def get_search_button(self):
        return self.driver.find_element(By.ID, self.search_button)
        
    def get_notification_ko_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.notification_ko )
    
    def get_cargo(self):
        return self.driver.find_element(By.ID, self.input_cargo)
        
    def get_salary(self):
        return self.driver.find_element(By.XPATH, self.salary)
        
    def get_salary_filter(self):
        return self.driver.find_element(By.XPATH, self.salary_filter)    
        
    def get_experience(self):
        return self.driver.find_element(By.XPATH, self.experiencia)
        
    def get_experience_filter(self):
        return self.driver.find_element(By.XPATH, self.experiencia_filter)
    
    def get_div_offers(self):
        return self.driver.find_element(By.ID, self.div_offers)
    
    def get_offer(self):
        div = self.get_div_offers()
        return div.find_element(By.LINK_TEXT, self.offer)
    
    def get_input_email(self):
        return self.driver.find_element(By.ID, self.login_email)
    
    def get_continue_with_mail_btn(self):
        return self.driver.find_element(By.ID, self.continue_mail_btn)
    
    def get_account_name(self):
        return self.driver.find_element(By.ID, self.account_name)
    
    def get_account_surName(self):
        return self.driver.find_element(By.ID, self.account_surName)

    def get_account_password(self):
        return self.driver.find_element(By.ID, self.account_password)

    def get_account_cargo(self):
        return self.driver.find_element(By.ID, self.account_cargo)

    def get_account_dpto(self):
        return Select(self.driver.find_element(By.XPATH, self.account_dpto_select))
    
    def get_account_dpto_option(self):
        return self.driver.find_element(By.XPATH, self.account_dpto_option)

    def get_captcha(self):
        return self.driver.find_element(By.ID, self.account_captcha)

    def get_continue_btn(self):
        return self.driver.find_element(By.ID, self.account_continue_btn)

    def get_captcha_error(self):
        return self.driver.find_element(By.XPATH, f"//div[@class='{self.captcha_error}']/span")
    
    
    
    ########__Actions__########:
    def click_colombiaFlag(self):
        self.get_colombiaFlag().click()
        
           
    def search_city(self):
        self.get_search_place_input().send_keys(self.city)
        
        
    def click_search_button(self):
        self.get_search_button().click()
        
        
    def click_ko_button(self):
        self.get_notification_ko_btn().click()
        
    
    def type_qa_in_prof(self):
        self.get_cargo().send_keys(self.cargo)
        
    
    def click_salary(self):
        self.get_salary().click()
        
        
    def click_salary_filter(self):
        self.get_salary_filter().click()
        
        
    def click_experience(self):
        self.get_experience().click()
        
        
    def click_experience_filter(self):
        self.get_experience_filter().click()   
        
        
    def validation_offer(self):
        try:
            job = self.get_offer()
            job.find_element(By.XPATH, f"//../../p[contains(text(),'{self.city}')]")
            print('Result validation: Job Found')
        except NoSuchElementException:
            print('Result validation: Job not found\nTaking a screenshot in reports folder.')
            self.driver.save_screenshot('reports/JobOfferError.png')
            
            
    def click_menu_btn_and_postulate(self):
        job = self.get_offer()
        menubtn = job.find_element(By.XPATH,f"//../div[@class='{self.menubtn}']")
        menubtn.click()
        postulate = menubtn.find_element(By.LINK_TEXT, self.postular)
        postulate.click()
    
    def type_email(self, email):        
        time.sleep(1)
        self.get_input_email().send_keys(email)    
        self.get_continue_with_mail_btn().click()
    
    def fill_form(self, name, apellido, contrasenya, trabajo, dpto, captcha):
        time.sleep(1)
        self.get_account_name().send_keys(name)
        self.get_account_surName().send_keys(apellido)
        self.get_account_password().send_keys(contrasenya)
        self.get_account_cargo().send_keys(trabajo)
        self.get_account_dpto().select_by_visible_text("Selecciona")

        option = self.get_account_dpto_option()
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        time.sleep(1)        
        self.driver.execute_script("arguments[0].click();", option )
        self.driver.execute_script("arguments[0].click();", option )
        self.get_captcha().send_keys(captcha)
    
    def click_continue_btn(self):
        self.get_continue_btn().click()
    
    def validation_captcha(self):
        try:
            captcha = self.get_captcha_error()
            print(f'Result validation: {captcha.text}')
        except NoSuchElementException:
            print('Result validation: Captcha error not found\nTaking a screenshot in reports folder.')
            self.driver.save_screenshot('reports/CaptchaNotError.png')
    
    @staticmethod
    def get_base_url():
        return base_url
