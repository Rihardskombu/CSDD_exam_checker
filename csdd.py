from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import pyttsx3 as pyttsx

fileUsername = open("E:\\desktop\\secret\\usr.txt", 'r')
filePassword = open("E:\\desktop\\secret\\pwd.txt", 'r')

username = fileUsername.read()
password = filePassword.read()
driver = webdriver.Chrome('chromedriver')

class CsddBot2:
    def login():#, username, password):
        
        driver.get("https://e.csdd.lv/login/?action=getLoginForm")
        sleep(1)
        
  
        login_field = driver.find_element_by_xpath("/html/body/main/section/div/div/form/div[1]/input")\
                      .send_keys(username)
        password_field = driver.find_element_by_xpath("/html/body/main/section/div/div/form/div[2]/div/input")\
                         .send_keys(password)
        login_button = driver.find_element_by_xpath("/html/body/main/section/div/div/form/input")\
                        .click()
        CsddBot2.process()
       
        
                
    def process():
        driver.get("https://e.csdd.lv/examp/")
        sleep(2)
        
        take_exam = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input[2]")\
                    .click()
        
        sleep(2)
        choose_department = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div[1]/table/tbody/tr/td/select")\
                            #.select_by_value('1')
        sleep(2)
        select_depart = Select(choose_department)
        select_depart.select_by_value('1')
        
        sleep(2)
        continue_button = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input")\
                          .click()
        sleep(2)
        getlicense = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/fieldset/label")\
                     .click()
        sleep(2)
        continue_button2 = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input")\
                           .click()
        sleep(2)
        exam_type = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/fieldset/label/input")\
                    .click()
        
        sleep(2)
        continue_button3 = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input")\
                           .click()
        
        sleep(2)
        avail_dates = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/select")\
                      
        avail_dates2 = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/select")\
                      .click()

   
        select_dates = Select(avail_dates)
        options = select_dates.options
        
        isEmpty = False
        
        for index in range(1, len(options)-1):
            current_line = options[index].text
            print(options[index].text)
            if current_line[-1] != '0':
                isEmpty = True
        print(" ")
        if isEmpty: 
            what2Say = 'csdd'
            

            # Speaking engine
            speakEngine = pyttsx.init()
            speakEngine.say(what2Say)
            speakEngine.runAndWait()

            while(True):
                speakEngine.say(what2Say)
                speakEngine.runAndWait()
        else:
            sleep(120)
            CsddBot2.process()
        
        


CsddBot2.login()




