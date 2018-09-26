# python-selenium-recurring-voter-in-online-contest-with-30-minutes-cooldown-period

<b>PURPOSE</b>: Script to cast vote for a participant in a Cute Baby contest on www.cutebaby.in, every 30 minutes using Python and Selenium.

![Alt text](screenshot.PNG?raw=true "python-selenium-recurring-voter-in-online-contest-with-30-minutes-cooldown-period")

<b>SITUATION</b>: A friend of ours had a distant relative, who had entered their baby in a contest on www.cutebaby.in. Our friend was trying to register as many votes from his side for the baby. To register a vote, he went to the URL of the participant baby, clicked on 2 buttons (occurring over a span of 1-2 minutes timed dialog boxes) before finally clicking on the actual VOTE button. Also, once a vote had been recorded, he could vote after a period of 30 minutes. We automated this for him using this script.

<b>AUTHORS</b>: Nalini Aggarwal & Lakshay Arora

<b>PRE-REQUISITE TO RUN THE SCRIPT</b>: Selenium package. To install selenium driver for Python, enter in command line:
$ pip install selenium
pip is Python's package manager. For more information on pip, refer to "https://www.djangospin.com/python-installing-external-modules-using-pip/".

<b>INPUTS TO SCRIPT</b>:
1. URL of the participant to cast vote on.
2. CSS selectors of all the button that need to be clicked to cast the vote.

<b>TO RUN THE SCRIPT</b>, enter in command line:
$ python clicker.py

<b>INFO</b>: The script maintains a counter of how many votes have been cast since the script has been commenced. Also gives the timestamp for the next vote.

<b>IF YOU NEED TO LOGIN TO FACEBOOK FIRST</b>, there's a commented out code block in the script to do that. Uncomment the block, fill in your credentials, and take it out for a spin.

<b>IF YOU NEED TO ADD ANOTHER BUTTON CLICK</b> in your sequence, follow the procedure mentioned in the script. Basically:
1. Get CSS selector for your new button from the webpage (right click on the button on the web page > Inspect > Right click on 
the tag which refers to #the button > Copy > Copy Selector > paste its value in identifier 'buttonSelector4' in the code).
2. Pass the 'buttonSelector4' in the function call in the end of the script.
3. Add the new argument in the function definition.
4. Comment out the code headed by 'DUMMY CODE BLOCK FOR AN ADDITIONAL BUTTON'. 
5. Enter sleep time for page or popup to occur.
6. Test the script.

<b>FOR RESOLVING SELENIUM ERROR</b> "shader_disk_cache", refer to https://stackoverflow.com/questions/37317427/unable-to-move-the-cache-error-in-selenium-webdriver".

We hope you find the script of utility. Reach out to us at naliniaggarwal1@gmail.com or lakshayarora7@gmail.com for any questions.
