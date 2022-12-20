from selenium.webdriver.common.by import By
from selenium import webdriver
import time



#text
textToSend = """hello"""

#open browser
browser = webdriver.Firefox(executable_path='/home/user/desktop/geckodriver')



browser.get('https://www.omegle.com')
browser.maximize_window()
time.sleep(5)

ChatButton = browser.find_element(By.ID, 'textbtn').click()

alreadySent = False
#box

Boxclick = browser.find_element(By.XPATH, '/html/body/div[7]/div/p[1]/label/input').click()
time.sleep(3)
Boxclick = browser.find_element(By.XPATH, '/html/body/div[7]/div/p[2]/label/input').click()
time.sleep(3)
Boxclick = browser.find_element(By.XPATH, '/html/body/div[7]/div/p[3]/input').click()
time.sleep(5)

while True:
    try:
        TextBox = browser.find_element(By.CLASS_NAME,"chatmsg")
        TextBox.send_keys(textToSend)
        time.sleep(3)
        SendButton = browser.find_element(By.CLASS_NAME,"sendbtn").click()
        print("text sent")
        alreadySent = True
        pass
        
        if alreadySent == True:

            Boxclick = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()
            time.sleep(3)
            Boxclick = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()
            time.sleep(5)
            DisconnectButton = browser.find_element(By.CLASS_NAME,"disconnectbtn").click()
            time.sleep(5)
    except:
        pass
