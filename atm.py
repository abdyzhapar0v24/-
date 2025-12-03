while True:

    print ("Банкомат")
    money = 1000
    user = 123456
    pin = int(input("Введите пинкод :"))
    if pin == user:
        print("Вы вошли в систему.")

    elif pin != 12345:
        print("Ошибка")
        break
    
    def oper():
        print("Доступные операции .")
        print("1 - Посмотреть баланс")
        print("2 - Cнять деньги ")
        print("3 - Пополнить счет")

    oper()
    choice = input("ВЫберие операцию:")
        
    if choice == "1":
        
        print(" Ваш баланс", money)
        choice2 = input("Вы хотите продолжить? Да/Нет")
        if choice2 == "Да":
            oper()
        else:
            print("Вы вышли из системы.")
            break
    elif choice == "2":
        summa = int(input("Введите сумму которую хотите снять:"))
        if summa <= 1000:
            print("Идет обрободка")
            print("Возьмите свои деньги",summa)
        elif summa > 1000:
            print("У вас не достаточно средств.")
            choice5 = input("Вы хотите продолжить? Да/Нет")
            if choice5 == "Да":
                oper()
            else:
                print("Вы вышли из системы.")
                break


        choice3 = input("Вы хотите продолжить? Да/Нет")
        if choice3 == "Да":
            oper()
        else:
            print("Вы вышли из системы.")
            break
            
        
        
    elif choice == "3":
        pay = int(input("Внесите купюру"))
        money2 = money + pay
        print("Ваш баланс",money2)
        choice4 = input("Вы хотите продолжить? Да/Нет")
        if choice4 == "Да":
            oper()
        else:
            print("Вы вышли из системы.")
            break
    


   


