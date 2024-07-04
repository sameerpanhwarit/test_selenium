from HelperMethods import Helper
from time import sleep
from datetime import datetime


helper = Helper()
helper.driver.maximize_window()
helper.driver.get('https://www.w3schools.com/')

helper.clickElement('//*[@id="navbtn_tutorials"]', 'xpath')

helper.clickElement('//*[@id="tutorials_backend_links_list"]/div[1]/a[1]','xpath')

helper.clickElement('//*[@id="leftmenuinnerinner"]/a[2]', 'xpath')
helper.driver.implicitly_wait(10)

element = helper.getElement('//*[@id="main"]/h3[3]','xpath')
helper.driver.execute_script("arguments[0].scrollIntoView(true);", element)

text = helper.getElementText('//*[@id="main"]/h3[4]','xpath')

with open('title.txt','a') as file:
    file.write(text)
    file.write('\n'+ str(datetime.now()))
    file.close()