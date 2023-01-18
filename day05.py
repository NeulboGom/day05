#Chapter8 Set

test_str=set("letters")
print(test_str)

test_dict={"apple":'red','oragne':'oragne'}
test_set=set(test_dict)
print(test_set)

drinks={"martini":{'vodka','vermouth'},
        'black russian':{"vodka",'kahlua'},
        "white russian":{"cream","kahlua","vodka"},
        "manhattan":{"rye","vermouth","bitters"},
        "screwdriver":{"orange juice","vodka"}}
'''
for name, contents in drinks.items():
        if 'vodka' in contents and not ("vermouth" in contents or 'cream' in contents):
                print(name)

for name, contents in drinks.items():
        if contents & {'vermouth','orange juice'}:
                print(name)
'''

for name, contents in drinks.items():
        if 'vodka' in contents and not contents & {"vermouth","cream"}:
                print(name)


bruss=drinks["black russian"]
wruss=drinks["white russian"]

#교집합 구하기 & 와 .intersection()
print(bruss & wruss)
print(bruss.intersection(wruss))
print("="*80)

#합집합 구하기
print(bruss|wruss) #'shift+\'=|
print(bruss.union(wruss))
print("="*80)

#차집합
print(bruss-wruss)
print(wruss-bruss)
print(wruss.difference(bruss))
print("="*80)

#대칭 차집합 구하기: 한 셋에는 포함할 수 있지만 두 셋 모두에는 포함되지 않는 항목 // 교집합의 여집합
print(bruss^wruss)
print(bruss.symmetric_difference(wruss))
print("="*80)

#부분집합 확인   부분집합<=상위집합 형태 // 부분집합.issubset(상위집합) 형태
#상위 집합은 부분집합의 반대.
print(wruss<=bruss)
print(bruss.issubset(wruss))
print("="*80)

#진부분집합: 한 셋이 다른 셋의 모든 contents를 포함하고 있어야 한다.
print(bruss<wruss)
print(wruss<bruss)
print("="*80)

#Set Comprehension
a_set={number for number in range(1,6) if number%3 == 1}
print(a_set)
print("="*60)

#불변 셋 생성하기:frozenset()
list_frozen=frozenset([3,2,1])
print(list_frozen)
