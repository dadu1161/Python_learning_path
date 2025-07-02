
def reverse(s):
    if s > 0:
        sign= 1
    else :
        sign =- 1


    s=abs(s)
    newstr=str(s)[::-1]


    return sign*int(newstr)



for i in range(1,50):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0 and i%7==0:
        print("fizzbazz")

    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    elif i % 7 == 0:
        print("bazz")
