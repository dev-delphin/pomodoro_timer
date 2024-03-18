import pomodoro

def inputs(concentration_time, smal_break_time, large_break_time, cicles) -> any:
    variables = [concentration_time, smal_break_time , large_break_time, cicles]
    ifs = [45, 10, 30, 100]
    input_texts = ["время таймера в минутах: ", "время короткого перерыва в минутах: ", "время большого перерыва в минутах: ", "количество повторений: "]
    information_texts = ["концентрации не более 45 минут.", "короткого перерыва не более 10 минут.", "большого перерыва не более 30 минут.", ""]
    for val, ifss, input_text, information_text in zip(variables, ifs, input_texts, information_texts):
        while True:
            try:
                variables.remove(0)
                variables.insert(val, int(input(f"Установите {input_text}")))
                if val > ifss: 
                    print(f"Рекомендуемое время {information_text}")
                    continue
                break
            except ValueError:
                print(f"Некорректный ввод. Попробуйте снова.")
    pomodoro.timer_time(variables)

if __name__ == "__main__":
    inputs(concentration_time = 0, smal_break_time = 0, large_break_time = 0, cicles = 0)