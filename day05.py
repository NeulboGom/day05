#Chapter9 Fucntion

#Lamda Function 익명함수
stairs=["thud","meow","thud","hiss"]

def edit_story(words, func):
    for word in words:
        print(func(word))


def enliven(word):  # 첫 글자를 대문자로 만들고 느낌표 붙이기
    return word.capitalize() + '!'


edit_story(stairs,enliven)




#rnadint로 100까지의 수 중에 제곱을 하는 것 5개의 수를 만들어보자..

"""
def squares(n):
    '''
    정수를 제곱하는 함수
    :param n: integer
    :return: integer
    '''
    return n*n

import random

def process(n_list, function):
    for n in n_list:
        print(function(n))

numbers=[random.randint(1,100) for number in range(5)]
print(numbers)
process(numbers,squares)
"""

import random

def process(n_list, function):
    for n in n_list:
        print(function(n))

numbers=[random.randint(1,100) for number in range(5)]
print(numbers)
process(numbers,lambda x: x * x)    #Lambda는 굳이 함수를 안 만들고, 익명의 함수를 만들어서 일시적으로 처리
                                    #Lambda가 process함수 중 function에 할당되고, Lambda의 x에 numbers의 n이 대입