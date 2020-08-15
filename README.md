# Remote KeyLogger

Its a simple remote keylooger built in python which when runs logs the keystroke and can either save it in the ile or simply mail the keystroke logs to the provided mail id.

## Usage

First Install the required modules using
`pip install -r requirement.txt`

Then simply run the script
`python3 logger.py`

## Configuring

By default this script saves the log in log.txt file in the same folder of the script to change the location change the
fs=open("./log.txt","a+) to fs=open("YOUR_LOCATION_HERE","a+")
or to disable saving the log on same computer
delete or comment out the lines as mentioned in script

To enable Remote logging Mention your email ID and PASS in the Variables (It is recommended to use a secondary account for this purpose, Less secure app access for that account must be enabled and 2 step verification must be off to easily use through smtplib)
uncomment the functions as mentioned in script