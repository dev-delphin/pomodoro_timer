import pomodoro

def inputs() -> None:
    variables = [0, 0, 0, 0]
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
    inputs()