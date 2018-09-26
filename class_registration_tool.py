#Carlton Welch, 2018
#selenium class automation

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#requires specific information about class selection.
class_list = ('Collapse section 34200 - Computer Organization',
				'Collapse section 33500 - Programming Language Paradigms')

browser = webdriver.Firefox()
url = "https://home.cunyfirst.cuny.edu/"
browser.get(url)

username = browser.find_element_by_id("CUNYfirstUsernameH")
password = browser.find_element_by_id("CUNYfirstPassword")

username.clear()
username.send_keys("USERNAME GOES HERE")
password.send_keys("PW GOES HERE")

time.sleep(2)

submitButton = browser.find_element_by_id("submit")
submitButton.click()

button = browser.find_element_by_id("crefli_HC_SSS_STUDENT_CENTER")
button.click()

time.sleep(2)

browser.switch_to.frame(browser.find_element_by_id("ptifrmtgtframe"))
button = browser.find_element_by_name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR1")
button.click()

time.sleep(2)

select = browser.find_element_by_id("CLASS_SRCH_WRK2_INSTITUTION$31$")
for option in select.find_elements_by_tag_name('option'):
	if option.text == 'City College':
		option.click()
		break
		
time.sleep(2)

select = browser.find_element_by_id("CLASS_SRCH_WRK2_STRM$35$")
for option in select.find_elements_by_tag_name('option'):
	if option.text == '2018 Fall Term':
		option.click()
		break
		
time.sleep(2)

select = browser.find_element_by_id("SSR_CLSRCH_WRK_SUBJECT_SRCH$0")
for option in select.find_elements_by_tag_name('option'):
	if option.text == 'CSC - Computer Science':
		option.click()
		break

button = browser.find_element_by_id("CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH")
button.click()

time.sleep(5)

for cls in class_list:
	if browser.find_elements_by_xpath("//a[@title='{}']".format(cls)):
		print("Found {}".format(cls[14::]))
	
# if (browser.find_elements_by_xpath("//a[@title='Collapse section CSC 34200 - Computer Organization']")):
#	print("Found 342")
	
# if (browser.find_elements_by_xpath("//a[@title='Collapse section CSC 33500 - Programming Language Paradigms']")):
#	print("Found 335")

print("Program end.")

	





