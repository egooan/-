num=[12,7,19,20,33,42,8,15,26,31]
a=0
count=0
for k in num:
    if num[a]%2==0:
        print("짝수:",num[a])
        count+=1
    a+=1
print("총 짝수의 개수:",count)