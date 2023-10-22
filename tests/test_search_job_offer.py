from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage 
import time
import json

class Tests_Redarbor(WebDriverSetup):
    
    def test_search_and_postulate_job(self):  
    ##################_______TEST 1_______###################
        driver = self.driver 
        self.driver.get(HomePage.get_base_url())
        home = HomePage(driver)
        # User selects Colombia
        home.click_colombiaFlag() 
        time.sleep(1)
        
        #User types "Guainía" in place input
        home.search_city()
                
        #click in search button
        home.click_search_button()

        #User refuse subscribe notifications
        home.click_ko_button()
                                
        #user types a proffesion: QA
        home.type_qa_in_prof()
        #Setting Salary 
        home.click_salary()
        home.click_salary_filter()
        #Setting experience  
        home.click_experience()
        home.click_experience_filter()

        #Assertion 
        home.validation_offer()
        
        
    ##################_______TEST 2_______###################
        
        #User clicks in 3 points menu button
        home.click_menu_btn_and_postulate()
        with open('src/PageObject/Pages/credentials.json', 'r') as file: 
           datos = json.load(file)
        for persona in datos['Persona']:
            name = persona['Name']
            apellido = persona['Apellido']
            email = persona['Email']
            contrasenya = persona['pass']
            trabajo = persona['trabajo']
            dpto = persona['departamento']
            captcha = persona['captcha']
        #User types email and continue 
        home.type_email(email)
        
        #User fill's the form 
        home.fill_form(name, apellido, contrasenya, trabajo, dpto, captcha)
        
        home.click_continue_btn()

        home.validation_captcha()