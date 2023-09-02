#Math solution tool for terminal
import os
import datetime
import time

def main():
    time.sleep(2)
    os.system('clear')
    print("[#] Choce what do you want\n\n")
    print("[01] For multiplication")
    print("[02] For addition")
    print("[03] For subtraction")
    print("[04] For devaid")
    print("[05] For multiple")
    print("[00] For Exit")
    
    
    
    def multiplication():
        os.system('clear')
        m1 = int(input("Enter Multiplicaton number: "))
        try:
            print("Ans:- \n")
            for i in range(1, 11):
                print(m1,"x",i,' = ',m1*i)
                i=i+1
            def m():
                print("\n\n[0] For back")
                print("[1] For continue")
                m1b = int(input("\nEnter your choice [0/1]: "))
                if m1b == 0:
                    main()
                else:
                    multiplication()
            m()
        except:
            os.system('clear')
            print("Invalid Input")
            time.sleep(2)
            main()
    def addition():
        os.system('clear')
        a1 = int(input("Enter your first number: "))
        a2 = int(input("\nEntr your second number: "))
        try:
            print("\n\nAns:- ",a1,"+",a2," = ",a1+a2)
        except:
            print("Invalid input")
            time.sleep(2)
            main()
        def ad():
            print("\n\n[0] For back")
            print("[1] For continue")
            adc = int(input("\nEnter your choice [0/1]: "))
            if adc == 0:
                main()
            else:
                addition()
        ad()
    def subtracton():
        os.system('clear')
        su1 = int(input("Enter your first number: "))
        su2 = int(input("Enter your second number: "))

        try:
            print("\n\nAns:- ",su1,"-",su2," = ",su1-su2)
        except:
            print("Invalid Input")
            time.sleep(2)
            main()
        def sud():
            print("\n\n[0] For back")
            print("[1] For continue")
            sub = int(input("\nEnter your choice [0/1]: "))
            if sub == 0:
                main()
            else:
                subtracton()
        sub()
    def devaid():
        os.system('clear')
        de1 = int(input("Enter your first number: "))
        de2 = int(input("\nEntr your second number: "))
        try:
            print("\n\nAns:- ",de1,"/",de2," = ",de1/de2)
        except:
            print("Invalid input")
            time.sleep(2)
            main()
        def deb():
            print("\n\n[0] For back")
            print("[1] For continue")
            adc = int(input("\nEnter your choice [0/1]: "))
            if adc == 0:
                main()
            else:
                devaid()
        deb()
    def multiple():
        os.system('clear')
        mul1 = int(input("Enter your first number: "))
        mul2 = int(input("\nEntr your second number: "))
        try:
            print("\n\nAns:- ",mul1,"x",mul2," = ",mul1*mul2)
        except:
            print("Invalid input")
            time.sleep(2)
            main()
        def mulb():
            print("\n\n[0] For back")
            print("[1] For continue")
            adc = int(input("\nEnter your choice [0/1]: "))
            if adc == 0:
                main()
            else:
                multiple()
        mulb()
    choice = int(input("\n\n\nEnter your choice: "))
    try:
        if choice == 1:
            multiplication()
        elif choice == 2:
            addition()
        elif choice == 3:
            subtracton()
        elif choice == 4:
            devaid()
        elif choice == 5:
            multiple()
        else:
            os.system('exit')
    except:
        os.system('clear')
        print("Invalid Input")
        time.sleep(2)
        main()
main()
