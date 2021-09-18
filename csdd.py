from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import pyttsx3 as pyttsx
import base64

from PIL import Image
import io



from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



driver = webdriver.Chrome("E:\desktop\chromedriver.exe")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 99999)
class CsddBot:
    def __init__(self):
        
        
 
        driver.get("https://e.csdd.lv/")
        sleep(1)
        
        loginbuttonxpath = "/html/body/main/div/div/div[1]/div[1]/button[1]"
        driver.find_element_by_xpath(loginbuttonxpath).click()
        
        sleep(1)
        agreecheckbox = "/html/body/form/center/div[2]/div/div[2]/input"
        driver.find_element_by_xpath(agreecheckbox).click()
        
        
        sleep(1)
        swedbankauth = "/html/body/form/center/div[2]/div/div[3]/ul/li/ul/li[4]/div/input"
        driver.find_element_by_xpath(swedbankauth).click()
        
        sleep(1)
        usernumber = "/html/body/div[1]/div/ui-views/ui-view/login-widget/ui-tabs/ui-views/ui-tab[1]/ui-form/form/ui-field[1]/div[2]/input"
        driver.find_element_by_xpath(usernumber).send_keys("ff")
        
        sleep(1)
        personalnumber = "/html/body/div[1]/div/ui-views/ui-view/login-widget/ui-tabs/ui-views/ui-tab[1]/ui-form/form/ui-field[2]/div[2]/input"
        driver.find_element_by_xpath(personalnumber).send_keys("gg")
        
        sleep(1)
        loginbuttonswed = "/html/body/div[1]/div/ui-views/ui-view/login-widget/ui-tabs/ui-views/ui-tab[1]/ui-form/form/ui-buttonbar/div[2]/button"
        driver.find_element_by_xpath(loginbuttonswed).click()
        
        sleep(15) #give user some time to accept duo push notif
        
        senduserdata = "/html/body/div[3]/main/div/form/section/ui-buttonbar/div[2]/input"
        driver.find_element_by_xpath(senduserdata).click()
        
        sleep(5)
        CsddBot.examCheck()

    def examCheck(): 
        driver.get("https://e.csdd.lv/examp/")

        
        take_exam_xpath = "/html/body/main/div/div[1]/section[1]/form/fieldset/input[2]"
        
        wait.until(ec.visibility_of_element_located((By.XPATH, take_exam_xpath)))
        
        driver.find_element_by_xpath(take_exam_xpath).click()
        
        
        choose_department = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div[1]/table/tbody/tr/td/select")
                            
        select_depart = Select(choose_department)
        select_depart.select_by_value('5') # 1=riga 5=jelgava
        
        continue_button = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input")\
                          .click()
        
        getlicense = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/fieldset/label")\
                     .click()
        
        continue_button2 = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/fieldset/input")\
                           .click()
        
        exam_type = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/div/table/tbody/tr[1]/td/fieldset/label/input")\
                    .click()
        
        #CAPTCHA start
        capcha_xpath = "/html/body/main/div/div[1]/section[1]/form/div[2]/div/label/img"
        
        ele_captcha = wait.until(ec.visibility_of_element_located((By.XPATH, capcha_xpath)))

        
        img_captcha_base64 = driver.execute_async_script("""
            var ele = arguments[0], callback = arguments[1];
            ele.addEventListener('load', function fn(){
                ele.removeEventListener('load', fn, false);
                var cnv = document.createElement('canvas');
                cnv.width = this.width; cnv.height = this.height;
                cnv.getContext('2d').drawImage(this, 0, 0);
                callback(cnv.toDataURL('image/jpeg').substring(22));
            }, false);
            ele.dispatchEvent(new Event('load'));
            """, ele_captcha)
        #print(img_captcha_base64)
        
        
        
        img_captcha_base64 = img_captcha_base64[1:] #remove first character

        #print(img_captcha_base64)
        
        wait.until_not(ec.presence_of_element_located((By.XPATH, capcha_xpath)))
        avail_dates = driver.find_element_by_xpath("/html/body/main/div/div[1]/section[1]/form/div/table/tbody/tr/td/select")
                      
        select_dates = Select(avail_dates)
        options = select_dates.options
        isEmpty = False
        for index in range(1, len(options)-1):
            current_line = options[index].text
            print(current_line)
            if current_line[-1] != '0':
                isEmpty = True
        avail_dates.click()
        if isEmpty: 
            what2Say = 'csdd'
            # Speaking engine
            speakEngine = pyttsx.init()
            speakEngine.say(what2Say)
            speakEngine.runAndWait()

            while(True):
                speakEngine.say(what2Say)
                speakEngine.runAndWait()
        
        sleep(20)
        CsddBot.examCheck()
        
CsddBot()



