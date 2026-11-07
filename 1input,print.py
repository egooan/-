if True:
    print("always")
    print("트루라면 무조건 수행")
if False:
    print("false")
    print("false라면 수행하지 않음")

if False:
    print("True")
    print("True라면 내부는 모두 수행합니다")

else:
    print("False")
    print("위조건들이 모두 false라면 실행.")

print("Always")

var1 = 1
var2 = 2

if var1 > var2:
    print("var1이 더 큽니다.")
if var1 == var2:
    print("var1과 var2가 같습니다.")
if var1 < var2:
    print("var2가 더 큽니다")



print("=====================")
score = 70

if score > 80:
    print("A학점입니다.")
elif score > 60:
    print("B학점입니다.")
elif score > 40:
    print("C학점입니다.")
elif score > 20:
    print("D학점입니다.")
elif score > 0:
    print("낙제입니다.")
print("=====================")
print("=====================")
print("1. 게임 시작")
print("2. 랭킹 확인")
print("0. 게임종료")
print("=====================")
user_input = input("원하는 동작을 입력하세요")

if user_input == "1":
    print("게임을 시작합니다.")
elif user_input == "2":
    print("1위 뚜땡스 제현")
    print("2위 뚜땡스 제현")
    print("3위 뚜땡스 제현")
else :
    print("게임종료")

number1 = int(input("첫번째 숫자를 입력하세요"))
number2 = int(input("두번째 숫자를 입력하세요"))
operator = input("연산자를 입력하세요 ")
if number1.isdigit() and number2.isdigit():
    if(operator == "+"):
        print(number1 + number2)
    elif(operator == "-"):
        print(number1 - number2)
    elif(operator == "*"):
        print(number1 * number2)
    elif(operator == "/"):
        print(number1 / number2)
    else:
        print("잘못된 입력입니다")
else:
    print("숫자가 아닌 입력입니다")