from typing import Any
from datetime import datetime, timedelta
from os import system
from playsound import playsound

def timer_time (variables) -> print:
    to_break = 1
    cicles = large_break_time = smal_break_time = concentration_time = 0
    for key, val in enumerate(variables):
        if key == 0: cicles = val
        if key == 1: large_break_time = val
        if key == 2: smal_break_time = val
        if key == 3: concentration_time = val
        
    while cicles > 0:
        data = [concentration_time, smal_break_time, large_break_time]
        texts = [f'Время концентрации. Минут: {concentration_time}.', f'Небольшой перерыв. Минут: {smal_break_time}.', f'Большой перерыв. Минут: {large_break_time}.']
        for date, text in zip(data,texts):
            if date == smal_break_time and to_break >= 3 and text == f'Небольшой перерыв. Минут: {smal_break_time}.':continue
            if date == large_break_time and to_break < 3 and text == f'Большой перерыв. Минут: {date}.': continue
            cur_time = datetime.now()
            date = cur_time + timedelta(seconds=date)
            playsound('media/8bit.mp3',block = False)
            while date >= cur_time:
                cur_time = datetime.now()
                system('clear')
                print(to_break)
                print(f"Осталось циклов: {cicles}\n{text}")
                print(date - cur_time)
            if to_break > 3: to_break=1
        to_break+=1
        cicles-=1
