#Chapter9 Fucntion
'''
def substract(n1,n2):
    print(n1-n2)

def run_func(f,arg1,arg2):
    f(arg1,arg2)

run_func(substract, 99, 98)'''


def substract(n1,n2):
    return n1-n2

def run_func(f,arg1,arg2):
    f(arg1,arg2)

print(run_func(substract, 99, 98))


#함수는 객체로 다뤄지고 매개변수로도 쓸 수 있고
#Return 용도로도 쓸 수 있다.


def caculate():
    x,y=1,2
    temp=0
    def add_sub(n):
        nonlocal temp
        #x=11
        temp = temp+x+n-y
        return temp

    return add_sub


c1=caculate()
for i in range(10):
    print(c1(i))


def outer(a,b):

    def inner(c,d):
        return c+d

    return inner(a,b)


print(outer(4,7))