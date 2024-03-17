from typing import Any
from datetime import datetime, timedelta
from os import system
from playsound import playsound

def timer_time (concentration_time, smal_break_time, large_break_time, cicles) -> print:
    to_break = 1
    while cicles > 0:
        cur_time = datetime.now()
        alarm_time = cur_time + timedelta(minutes=concentration_time)
        playsound('media/8bit.mp3',block = False)
        while alarm_time >= cur_time:
            cur_time = datetime.now()
            system('clear')
            print(f"Осталось циклов: {cicles}\nВремя концентрации. {concentration_time} минут.")
            print(alarm_time - cur_time)

        cur_time = datetime.now()
        alarm_smal_break_time = cur_time + timedelta(minutes=concentration_time)
        playsound('media/8bit.mp3',block = False)
        while alarm_smal_break_time >= cur_time:
            cur_time = datetime.now()
            system('clear')
            print(f"Осталось циклов: {cicles}\nНебольшой перерыв. {smal_break_time} минут.")
            print(alarm_smal_break_time - cur_time)

        if to_break == 3:
            cur_time = datetime.now()
            alarm_large_break_time = cur_time + timedelta(minutes=concentration_time)
            playsound('media/8bit.mp3',block = False)
            while alarm_large_break_time >= cur_time:
                cur_time = datetime.now()
                system('clear')
                print(f"Осталось циклов: {cicles}\nБольшой перерыв. {large_break_time} минут.")
                print(alarm_large_break_time - cur_time)
        to_break+=1
        cicles-=1
