#Chapter8 Set

#두 수 사이의 소수를 전부 나열하는 코드

def isprime(n):
        '''
        매개변수로 받은 정수가 prime number인지 판정하는 함수입니다.
        parameter n: integer number
        return: True or False
        '''
        if n <= 1:
                return False
        elif n > 1:
                for k in range(2, n):
                        if n % k == 0:
                                return False
                else:
                        return True

print(isprime(19))
help(isprime)

num1=int(input("number1:"))
num2=int(input("number2:"))

if num1>num2:
    num1,num2=num2,num1

for i in range(num1,num2+1):
   if isprime(i):
       print(i,end=' ')