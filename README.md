# python-selenium-recurring-voter-in-online-contest-with-30-minutes-cooldown-period

Script to cast vote for a participant in a Cute Baby contest on www.cutebaby.in, every 30 minutes using Python and Selenium.

Author: Nalini & Lakshay

Inputs:
1. URL of the participant to cast vote on.
2. CSS selectors of all the button that need to be clicked to cast the vote.

A single user can re-vote after 30 minutes. In order to incorporate 
slow networks, the script waits for 31 minutes before running the function again.
The script maintains a counter of how many votes have been cast since the script
has been commenced. Also gives the timestamp for the next vote.
