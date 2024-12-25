from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

service = Service(executable_path = './chromedriver')

options = Options()
options.add_experimental_option ('detach', True) #this to enrsure chrome browser does not close 

chrome_browser =  webdriver.Chrome(service=service, options=options)

#chrome_browser.maximize_window()
chrome_browser.get('http://almiraxk.pythonanywhere.com/contact.html')

# print ('Title page' in chrome_browser.title) #True

# button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default') 
# print(button) #True 

#button_text = chrome_browser.find_element(By.CLASS_NAME, 'btn-default') 
#print (button_text.get_attribute('innerHTML')) #Send


assert 'Email' in chrome_browser.page_source
user_email = chrome_browser.find_element(By.ID, "email")
user_email.clear()
user_email.send_keys('selenium@gmail.com')

assert 'Subject' in chrome_browser.page_source
subject = chrome_browser.find_element(By.ID, "subject")
subject.clear()
subject.send_keys('selenium test')

assert 'Enter your message' in chrome_browser.page_source
message = chrome_browser.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/form/div/div[1]/div[3]/textarea") #/html/body/div[5]/div/div/div/div[2]/div/form/div/div[1]/div[3]/textarea
message.clear()
message.send_keys('selenium testing message')

assert 'Send' in chrome_browser.page_source
button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default') 
button.click()

assert 'Thank you! I will get in touch with you, shortly!' in chrome_browser.page_source 

#chrome_browser.close() #close the chrome page 
chrome_browser.quit()





