n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        print(i)
        count+=i
if count==n:
    print("perfect number")
else:
    print("not a perfect number")
