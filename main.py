import time
from datetime import datetime
from datetime import date
import pandas as pd

zero=0

colnames=['ActivityDate','ActivityTime','Activity']
df = pd.read_csv("C:\\Users\\sachi\\OneDrive\\Desktop\\Whitehat\\HW 102\\Read.csv",names=colnames, header=None)

second=0
seconds=0

while(second==0):
    for i in range(len(df)):
        # Checking for activities in next one hour
        if((datetime.strptime(df['ActivityDate'][i] + ' '+df['ActivityTime'][i], '%d-%m-%Y %H:%M')-datetime.now()).seconds <=3600 ):
        #    #if((datetime.strptime(df['ActivityTime_s'][i],'%d-%m-%Y %H:%M')-(today))<=60 ):
            print(df['Activity'][i])
    ## Reminder after every 15 minutes
    while(seconds<900):
        seconds+=1
        time.sleep(1)

    seconds=0






def check():
    # while(current_hour_int==15):
        print("Chess time")


check()