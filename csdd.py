from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import pyttsx3 as pyttsx

driver = webdriver.Chrome('chromedriver')

class CsddChecker:
    def login():

        driver.get("https://e.csdd.lv/login/?action=getLoginForm") #open CSDD login link
        sleep(1) #wait 1 second
        
        fileUsername = open("C:\\secret\\usr.txt", 'r') #open username text file
        filePassword = open("C:\\secret\\pwd.txt", 'r') #open password text file 
        
        username = fileUsername.read() #read username from text file
        password = filePassword.read() #read password from text file
        
        #fill username field
        driver.find_element_by_xpath("/html/body/main/section/div/div/form/div[1]/input").send_keys(username)
        
        #fill password field
        driver.find_element_by_xpath("/html/body/main/section/div/div/form/div[2]/div/input").send_keys(password)
        
        #click login button
        driver.find_element_by_xpath("/html/body/main/section/div/div/form/input").click()


    def examCheck():

        driver.get("https://e.csdd.lv/examp/") #open CSDD 'apply for exam' form
        sleep(2) #wait 2 seconds
        
        #take exam button
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input[2]").click()
        sleep(2) #wait 2 seconds
        
        #pick branch
        pick_branch = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div[1]/table/tbody/tr/td/select")
        sleep(2) #wait 2 seconds
        
        pick_branch = Select(pick_branch)
        #pick_branch.select_by_value('1') #1 Rigas KAC
        #pick_branch.select_by_value('2') #2 Daugavpils
        pick_branch.select_by_value('4034') #4034 Rigas Bikiernieku
        
        #click continue button
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input").click()
        sleep(14) #wait 4 seconds
        
        #pick reason (Iemesls)
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/fieldset/label").click()
        
        #click continue button
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input").click()
        sleep(4) #wait 4 seconds
        
        #pick exam type (Eksamena veids)
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/fieldset/label/input").click()
        
        #click continue button
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input").click()
        sleep(2)  #wait 2 seconds               
        
        #read dates from 'available dates' dropdown 
        avail_dates = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/select")
        
        #click 'available dates' dropdown (only for user convenience)
        driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/select").click()

        #read all values from dropdown
        select_dates = Select(avail_dates)
        options = select_dates.options
        
        #define flag 'empty slot detected'
        isEmptySlotDetected = False
        
        #loop through dropdown values
        for index in range(1, len(options)-3):
            
            currentLine = options[index].text #current line :)
            print(currentLine) #print current line in console
            
            #check last character of current line
            #e.g. 19.05.2021 Brīvās vietas: 0
            #                               ^
            if currentLine[-1] != '0':
                
                #there is empty slot! because last character is not equal to 0
                isEmptySlotDetected = True
        
        print(" ")  #print new(empty) line
        
        if isEmptySlotDetected == True:  #if there is empty slot, notify user
            
            #text to say
            what2Say = 'csdd'

            #endless loop
            while(True):
                #speaking engine
                speakEngine = pyttsx.init()
                speakEngine.say(what2Say)
                speakEngine.runAndWait()
                sleep(2)  #wait 2 seconds
              
        else: #otherwise re-check again  
            sleep(30) #wait 9 seconds
            CsddChecker.examCheck() #execute exam check method again
        
#initialize
CsddChecker.login()

#execute exam check method
CsddChecker.examCheck()
