num1 = int(input("첫 번째 숫자:"))
num2 = int(input("두번째 숫자:"))
cal = input("연산자:")

if cal== "+":
    print(num1+num2)
elif cal== "*":
    print(num1*num2)
elif cal== "/":
    print(num1/num2)
elif cal== "-":
    print(num1-num2)
else:
    print("잘못된 연산자입니다")


