import timer as t

def inputs(concentration_time, smal_break_time, large_break_time, cicles) -> t.timer_time:
    variables = [concentration_time, smal_break_time, large_break_time, cicles]
    ifs = [45, 10, 30, 100]
    input_texts = ["время таймера в минутах: ", "время короткого перерыва в минутах: ", "время большого перерыва в минутах: ", "количество повторений: "]
    information_texts = ["концентрации не более 45 минут.", "короткого перерыва не более 10 минут.", "большого перерыва не более 30 минут.", ""]
    for (key, vari), ifss, input_text, information_text in zip(enumerate(variables), ifs, input_texts, information_texts):
        while True:
            try:
                # разобраться со списками
                print(key, vari)
                #print (variables[vari])
                variables[key] = int(input(f"Установите {input_text}"))
                print (vari)
                if vari > ifss: 
                    print(f"Рекомендуемое время {information_text}")
                    continue
                break
            except ValueError:
                print(f"Некорректный ввод. Попробуйте снова.")
    #for key, val in enumerate(variables):
    #    print (key)
    print(concentration_time, smal_break_time, large_break_time, cicles)
    #t.timer_time(concentration_time, smal_break_time, large_break_time, cicles)

#variables[variables.index(vari)]
if __name__ == "__main__":
    inputs(concentration_time = 0, smal_break_time = 0, large_break_time = 0, cicles = 0)