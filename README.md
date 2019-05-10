# AWW - Another Web Watchdog

Python script that monitors the availability of 
a given web page and sends an email with smtp from a 
Google account in case the page is down, or too slow. 

The script requires the following three environment variables:

* WATCHDOG_EMAIL = the email from which the notification should be sent; 
assumes gmail since it's easier than setting up a local mail server
* WATCHDOG_PASS = the password for the afore-mentioned email
* THE_WOLF_EMAIL = the email to which to send the notifications; The Wolf in Pulp Fiction solves problems :)



# Running With Crontab

To run from crontab use something like: 

    * * * * * env WATCHDOG_EMAIL="" WATCHDOG_PASS="" THE_WOLF_EMAIL="" /usr/local/bin/python3.6 $HOME/zee/watchdog/email_if_down.py >> $HOME/.watchdog_log 2>&1
