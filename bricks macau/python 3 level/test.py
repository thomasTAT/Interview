

d={'Python编程挑战赛':0,'开源鸿蒙主题赛':0,'智慧物流挑战赛':0}

while True:

    num = int(input())

    if num ==1:
        d['Python编程挑战赛'] += 1

    elif num ==2:
        d['开源鸿蒙主题赛'] += 1

    elif num ==3:
        d['智慧物流挑战赛'] += 1

    elif num ==0:
        break
    else:
        print("wrong")
    
for key,value in d.items():
    print(key+str(value)+"人")