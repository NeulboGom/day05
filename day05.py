#Chapter9 Fucntion

number_of_people = int(input("방문 인원 수를 말씀해 주세요:"))
def cal_fee(args):     #-><type>: 타입 힌트
    '''
    놀이공원 요금 계산 프로그램z
    args: input에서 받은 인원수
    count_adult: 성인 인원 수
    count_child: 아동 인원수
    totla: 총 요금
    '''
    import random
    total = 0
    count_adult = 0
    count_child = 0
    ages=[random.randint(1,100) for age in range(number_of_people)]
    for age in ages:
        if age>=19:
            total+=10000
            count_adult+=1
        else:
            total+=3000
            count_child+=1
    return {"총 인원": len(ages),"어른":count_adult,"아동":count_child,"총 금액":total}

        #f"인원수는 {len(ages)}명이고, 그 중 어른은 {count_adult}명, 아동은 {count_child}명입니다. 총 요금은 {total}원 입니다."


results=cal_fee(number_of_people)
print(results)
print(f"총 인원은 {results['총 인원']}명이고, 그 중 어른은 {results['어른']}명, 아동은 {results['아동']}명입니다. 총  요금은 {results['총 금액']}원 입니다.")
