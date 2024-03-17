import timer as t

if __name__ == "__main__":
    while True:
        try:
            concentration_time = int(input("Установите время таймера в минутах: "))
            if concentration_time > 45: 
                print("Рекомендуемое время концентрации не более 45 минут.")
                continue
            while True:
                try:
                    smal_break_time = int(input("Установите время короткого перерыва в минутах: "))
                    if smal_break_time > 10: 
                        print("Рекомендуемое время короткого перерыва не более 10 минут.")
                        continue
                    while True:
                        try:
                            large_break_time = int(input("Установите время большого перерыва в минутах: "))
                            if large_break_time > 30: 
                                print("Рекомендуемое время большого перерыва не более 30 минут.")
                                continue
                            while True:
                                try:
                                    cicles = int(input("Установите количество повторений: "))
                                    break
                                except ValueError:
                                    print(f"Некорректный ввод. Попробуйте снова.")
                            break
                        except ValueError:
                            print(f"Некорректный ввод. Попробуйте снова.")
                    break
                except ValueError:
                    print(f"Некорректный ввод. Попробуйте снова.")
            break
        except ValueError:
            print(f"Некорректный ввод. Попробуйте снова.")


    t.timer_time(concentration_time, smal_break_time, large_break_time, cicles)