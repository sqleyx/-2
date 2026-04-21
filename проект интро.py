while True:
    a = input("Введите текст: ").lower()
    
    if a == "выход":
        break

    words = a.split()

    max_word = ""
    max_count = 0

    for word in words:
        count = words.count(word)
        if count > max_count:
            max_count = count
            max_word = word

    print("Самое частое слово:", max_word)
    
    again = input("Хотите продолжить (да/нет): ").lower()
    if again != "да":
        break
    
   