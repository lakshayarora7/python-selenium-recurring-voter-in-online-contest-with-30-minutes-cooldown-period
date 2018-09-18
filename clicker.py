## python-selenium-recurring-voter-in-online-contest-with-30-minutes-cooldown-period

## PURPOSE: Script to cast vote for a participant in a Cute Baby contest on 
### www.cutebaby.in, every 30 minutes using Python and Selenium.

## AUTHORS: Nalini Aggarwal & Lakshay Arora

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

global counter
counter = 0
URL = "https://mycutebaby.in/contest/participant/?n=5ba007555ee4e"
buttonSelector1 = "button#onesignal-popover-cancel-button.align-right.secondary.popover-button"
buttonSelector2 = '#fb-close'
buttonSelector3 = "#vote_btn"

# For adding a new button selector, use the identifier immediately below. 
# This identifier is not used in the current script.
# If you intend to use it:
# Get the CSS selector for your new button by, 
# right click on the button on the web page > Inspect > Right click on 
# the tag which refers to #the button > Copy > Copy Selector > paste it in 
# below identifier.
# Remember to pass it in the function call at the bottom of the script.
# Then add it to the function definition a couple of lines bneath this one.
# Then comment out the 'DUMMY CODE LOCK FOR AN ADDITIONAL BUTTON' code block 
# and enter time to wait for the page/popup if needed. 
buttonSelector4 = "placeholder_for_new_button_selector"	

def clicker(URL, buttonSelector1, buttonSelector2, buttonSelector3):
	'''Function to cast vote for a participant in a Cute Baby contest on 
	www.cutebaby.in. Takes the URL of the participant and CSS selectors of
	buttons to be clicked to cast vote'''
	global counter
	counter += 1
	print("Vote #" + str(counter), str(datetime.datetime.now()))
	driver = webdriver.Chrome()

    # COMMENT OUT THE FOLLOWING CODE BLOCK IF YOU NEED FACEBOOK LOGIN
    #driver.get("http://facebook.com")
    #time.sleep(2)
    #print("Logging into facebook....")
    #element = driver.find_element_by_name("email")
    #element.clear()
    #element.send_keys("userNameHere")
    #element = driver.find_element_by_name("pass")
    #element.clear()
    #element.send_keys("passwordHere")
	#element.send_keys(Keys.RETURN)

	# OPEN THE URL AND CLICK ON A BUTTON TO GET RID OF 1ST POPUP WINDOW
	driver.get(URL)
	print("Waiting for 10 seconds before clicking Cancel button in popup window...")
	time.sleep(10)
	print("Clicking Cancel button in popup window...")
	driver.find_element_by_css_selector(buttonSelector1).click()

	# CLICK ON 'X' IN 2ND POPUP WINDOW
	print("Waiting for 35 seconds before clicking 'x' in 'Connect With Us' popup window...")
	time.sleep(35)			
	print("Clicking 'x' in 'Connect With Us' popup window...")
	driver.find_element_by_css_selector(buttonSelector2).click()

	# DUMMY CODE BLOCK FOR CLICKING AN ADDITIONAL BUTTON
	#driver.get(URL)
	#print("Waiting for 35 seconds before clicking ''...")
	#time.sleep(35)			
	#print("Clicking '' button in '' popup window...")
	#driver.find_element_by_css_selector(buttonSelector4).click()

	# CLICK THE PRIMARY VOTING BUTTON TO CAST VOTE
	print("Waiting for 15 seconds before clicking 'Tap to Vote' button...")
	time.sleep(15)			
	print("Clicking 'Tap to Vote' button...")
	driver.find_element_by_css_selector(buttonSelector3).click()

	# EXIT BROWSER 
	print("Waiting for 10 seconds before exiting browser.")
	time.sleep(10)
	print("Exiting browser...")
	driver.close()

	# PRINT TIME FOR NEXT VOTE
	print("Next vote at:", str(datetime.datetime.now() + datetime.timedelta(0, 1800)), "\n")
	time.sleep(1800)			

# IF CONSTRUCT TO RUN ONLY IF SCRIPT EXECUTED USING DOUBLE CLICK OR COMMAND LINE, AND
# NOT WHEN IMPORTED
if __name__ == '__main__':
	while True:
		clicker(URL, buttonSelector1, buttonSelector2, buttonSelector3)
