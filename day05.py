#Chapter9 Fucntion

def commentary(color):
    if color=='red':
        return "It's a tomato."
    else:
        return f"I've never heard of the color {color}"

comment1=commentary("red")
comment2=commentary("blue")

print(comment1)
print(comment2)


#None(중요)
mamamoo=['화사','솔라','휘인','문별']

# print(mamamoo.pop())  #삭제할 값 return 후 삭제
print(mamamoo.remove("문별"))  #삭제만 함. 따라서 return 값이 없으므로 print 함수는 출력할 값이 없다 => None 출력
print(mamamoo.pop())

#위치인수와 키워드 인수
#위치에 따라서 들어가는 자리가 달라지는게 위치 인수
#키워드를 지정해서 들어가는 키워드 인수

def menu(wine, entree, dessert):
    return {"wine":wine,"entree":entree,"dessert":dessert}

print(menu("chardonnay","chicken","cake"))
print(menu("chicken","cake","chardonnay"))

#Default 인수 - 기본값이 정해져있는 인수
def menu_2(wine, entree,dessert='pudding'):
    return {"wine":wine,"entree":entree,"dessert":dessert}
print(menu_2("chardonnay","chicken"))
print(menu_2("dunelfelder","duck","doughnut"))

#   *(애스터리스크)  던져지는 parameter의 갯수가 가변적일 때 좋음

def print_args(*args):
    print(f"Positional tuple: {args}")

print_args()
print_args(3,2,1,"wait!","uh...")




#
# def calculate_fee(*args):
#     '''
#     놀이공원 요금 계산 함수
#     :param args:ages
#     :return: 지불할 총 입장료
#     '''
#     number_of_people=int(input("방문 인원수를 말씀해주세요:"))
#     total = 0
#     for age in args:
#         age=random.randrange(1,101)
#         if age>=19:  #adult
#             total+=10000
#         else:
#             total+=3000
#     return total




number_of_people = int(input("방문 인원 수를 말씀해 주세요:"))
def cal_fee(args):     #-><type>: 타입 힌트
    '''
    놀이공원 요금 계산 프로그램
    args: input에서 받은 인원수
    count_adult: 성인 인원 수
    count_child: 아동 인원수
    totla: 총 요금
    '''
    import random
    total = 0
    count_adult = 0
    count_child = 0
    ages=[random.randint(1,101) for age in range(number_of_people)]
    for age in ages:
        if age>=19:
            total+=10000
            count_adult+=1
        else:
            total+=3000
            count_child+=1
    return f"인원수는 {len(ages)}명이고, 그 중 어른은 {count_adult}명, 아동은 {count_child}명입니다. 총 요금은 {total}원 입니다."


print(cal_fee(number_of_people))