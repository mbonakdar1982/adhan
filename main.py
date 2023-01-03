import pandas as pd
import requests
import funcs
import time
import datetime

prayTimes = pd.read_excel('assets/praytimes2023.xlsx').set_index('fullDate')
while True:
    now = datetime.datetime.now()
    todayDate = now.date().strftime("%d-%m-%Y")
    currentTime = now.time().strftime("%H:%M")
    hour = int(currentTime[0:2])
    dhuhrAdhan = prayTimes.loc[todayDate, 'dhuhr']
    maghribAdhan = prayTimes.loc[todayDate, 'maghrib']
    weekday = prayTimes.loc[todayDate, 'weekday']
   
    if currentTime == dhuhrAdhan:
        funcs.playAdhan()
        funcs.playdoa(doa=weekday)
        funcs.playdoa(doa='doa')
    if currentTime == maghribAdhan:
        funcs.playAdhan()
        funcs.playdoa(doa=weekday)
        funcs.playdoa(doa='doa_komeyl' if weekday == 'Friday' else 'doa')
    

    if (currentTime[-2:] == '30') & (hour < 22) & (hour >= 7):
        funcs.playsound('halfHour')    
        time.sleep(5)
    if (currentTime[-2:] == '00') & (hour < 22) & (hour >= 7):
        funcs.playsound('hourChime')
        if hour > 12:
            hour = hour - 12
        for i in range(hour):
            funcs.playsound('bell', 4)
        time.sleep(5)
    print(currentTime)
    print('Weekday: {}'.format(weekday))
    print('Maghrib: {}'.format(maghribAdhan))
    print('dhuhr: {}'.format(dhuhrAdhan))
    funcs.playsound('silence')
    time.sleep(55)
