import random
s1 = ["banana", "lion", "watermelon", "monkey", "apple", "cat", "dog", "orange", "strawberry", "kiwi"]
def main():
    a = input("Калимаи нав ворид кунед: ")
    s1.append(a)
    print(f"Калимаи {a} ба рӯйхат илова шуд.")
def main1(d):
    if (i in d.lower() for i in ["cat", "dog", "lion", "monkey"]):
        print("Ин калима номи ҳайвон аст.")
    elif (i in d.lower() for i in ["banana", "watermelon", "orange", "strawberry", "kiwi","apple"]):
        print("Ин калима номи меваи дарахтӣ аст.")
    else:
        print("Ин калима номи ҳайвон ё меваи дарахтӣ аст.")
def main2():
    d1 = random.choice(s1)
    d2 = ["*"] * len(d1)
    cnt = 5
    while True:
        print(" ".join(d2))
        print(f"Шумо {cnt} имконият доред.")
        ss = input("Ҳарфро ворид кунед: ").lower()
        if ss in d1.lower():
            for i in range(len(d1)):
                if d1[i].lower() == ss:
                    d2[i] = ss
        else:
            print("Ҳарф дар калима нест!")
            cnt -= 1
            if cnt == 0:
                print(f"Афсӯс! Калима {d1} буд.")
                break
        if "*" not in d2:
            print(f"Табрик! Калима {d1} аст.")
            break
        if cnt == 4 and input("Оё шумо мехоҳед ёрӣ гиред? (Yes/No) ").lower() == "yes":
            main1(d1)
while True:
    print("\nМеню:")
    print("1. Калимаи нав илова кардан")
    print("2. Оғози бозӣ")
    print("3. Хориҷ шудан")
    ch = input("Вариантро интихоб кунед: ")
    if ch == "1":
        main()
    elif ch == "2":
        main2()
    elif ch == "3":
        print("Хайр!")
        break
    else:
        print("Вариант нодуруст. Лутфан, дубора кӯшиш кунед.")