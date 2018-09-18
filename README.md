# python-selenium-recurring-voter-in-online-contest-with-30-minutes-cooldown-period

Script to cast vote for a participant in a Cute Baby contest on www.cutebaby.in, every 30 minutes using Python and Selenium.

Authors: Nalini Aggarwal & Lakshay Arora

Pre-requisite to run the script: Selenium package. To install selenium driver for Python, enter in command line:
$ pip install selenium
pip is Python's package manager. For more information on pip, refer to "https://www.djangospin.com/python-installing-external-modules-using-pip/".

Inputs to script:
1. URL of the participant to cast vote on.
2. CSS selectors of all the button that need to be clicked to cast the vote.

To run the script, enter in command line:
$ python clicker.py

A single user can re-vote after 30 minutes. In order to incorporate slow networks, the script waits at some points to ensure that the page has loaded properly before clicking on the buttons. The script maintains a counter of how many votes have been cast since the script has been commenced. Also gives the timestamp for the next vote.

If you need to login to Facebook first, there's a commented out code block in the script to do that. Uncomment the block, fill in your credentials, and give it a spin.

If you need to add another button click in your sequence, follow the procedure mentioned in the script. Basically:
1. Get CSS selector for your new button from the webpage (right click on the button on the web page > Inspect > Right click on 
the tag which refers to #the button > Copy > Copy Selector > paste its value in identifier 'buttonSelector4' in the code).
2. Pass the 'buttonSelector4' in the function call in the end of the script.
3. Add the new argument in the function definition.
4. Comment out the code headed by 'DUMMY CODE BLOCK FOR AN ADDITIONAL BUTTON'. 
5. Enter sleep time for page or popup to occur.
6. Test the script.


For resolving selenium error "shader_disk_cache", refer to https://stackoverflow.com/questions/37317427/unable-to-move-the-cache-error-in-selenium-webdriver".

We hope you find the script of utility. Reach out to us at naliniaggarwal1@gmail.com or lakshayarora7@gmail.com for any questions.
