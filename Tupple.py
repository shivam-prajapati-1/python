# num = int(input("Enter a number: "))
# for i in range(1,n+1):
#    if  num % 3 == 0 or num % 5 == 0:
#        print(num)




num = int(input("Enter a number: "))
print("Numbers divisible by 3 or 5:")
for i in range(1, num + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
