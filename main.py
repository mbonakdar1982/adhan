#!/usr/bin/env python
import pandas as pd
import requests
import funcs
import time
import datetime
import alsaaudio

m = alsaaudio.Mixer()
current_volume = m.getvolume()
print('current volume: {}'.format(current_volume))
m.setvolume(45)
hijriMonth = {'01': 'Muharram', '02': 'Safar', '03': 'Rabi-al-Awwal', '04': 'Rabi-al-Thani', '05': 'Jumada-al-Awwal', '06': 'Jumada-al-Thani', '07': 'Rajab', '08': 'Shaban', '09': 'Ramadan', '10': 'Shawwal', '11': 'Dhu-al-Qadah', '12': 'Dhu-al-Hijjah'}
prayTimes = pd.read_excel('assets/praytimes2025.xlsx').set_index('fullDate')
funcs.playsound('halfHour')
while True:
    now = datetime.datetime.now()
    todayDate = now.date().strftime("%d-%m-%Y")
    currentTime = now.time().strftime("%H:%M")
    
    currentTime_advance = (now + datetime.timedelta(minutes=12, seconds=21)).strftime("%H:%M")
    hour = int(currentTime[0:2])
    hijriDate = prayTimes.loc[todayDate, 'hijriDate']
    [hijri_day, hijri_month, hijri_year] = hijriDate.split('-')
    dhuhrAdhan = prayTimes.loc[todayDate, 'dhuhr']
    maghribAdhan = prayTimes.loc[todayDate, 'maghrib']
    weekday = prayTimes.loc[todayDate, 'weekday']
    if hijri_month == '09' and currentTime_advance == maghribAdhan:
        funcs.playdoa(doa='rabbana')
        funcs.playdoa(doa='tawashih')
        funcs.playAdhan()
        funcs.playdoa(doa='ramezanDaily_{}'.format(hijri_day))
        funcs.playdoa(doa='somna')
        funcs.playdoa(doa='shahr')
        funcs.playdoa(doa='eftetah')

   
    if currentTime == dhuhrAdhan:
        funcs.playAdhan()
        funcs.playdoa(doa=weekday)
        if hijri_month == '07':
            funcs.playdoa(doa='Rajab')
        elif hijri_month == '08':
            funcs.playdoa(doa='shaaban')
        funcs.playdoa(doa='doa_eftetah' if weekday == 'Wednesday' else 'random')
    if currentTime == maghribAdhan:
        funcs.playAdhan()
        funcs.playdoa(doa=weekday)
        if hijri_month == '07':
            funcs.playdoa(doa='Rajab')
        elif hijri_month == '08':
            funcs.playdoa(doa='shaaban')
        funcs.playdoa(doa='doa_komeyl' if weekday == 'Thursday' else 'random')
    

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
    print(currentTime_advance)
    print('day: {}, month: {}'.format(hijri_day, hijriMonth[hijri_month]))
    print('Weekday: {}'.format(weekday))
    print('Maghrib: {}'.format(maghribAdhan))
    print('dhuhr: {}'.format(dhuhrAdhan))
    funcs.playsound('silence')
    time.sleep(55)
