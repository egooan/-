menu= {
    "삼각김밥":1200,
    "바나나우유":1700,
    "컵라면":1500,
    "샌드위치": 2500
}
ord=input()
for item in menu:
    if ord==item:
        print(menu[item])
    else:
        print("해당 메뉴는 판매하지 않는다")
        break