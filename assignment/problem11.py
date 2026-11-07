movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]

print("평점이 8.5이상")
for i in movies:
    if i["rating"] >= 8.5:
        print('-',i["title"])
view=0
for i in movies:
    if i['genre']=='애니메이션':
        view+=i['views']
print('애니 총 조히수:',view)
max=0
for i in movies:
    if i['']>max: