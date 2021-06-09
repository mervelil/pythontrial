from selenium import webdriver
#import time

driver = webdriver.Chrome("Users\merve çelik\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webdriver")
url ="https://www.python.org"


driver.get(url)
"""
"""
"""
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.png")

print(driver.title)
driver.close()
"""
"""
import http.client
from urllib.parse import urlencode
conn=http.client.HTTPConnection("http://www.python.org")
params ={
    "q": "aranacakyazi"
}
conn.request("GET","/search/?q="+urlencode(params))
resp=conn.getresponse()

if b'No result' in resp.read():
    print("yok")
conn.close()
"""