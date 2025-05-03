"""
애완 동물을 소개해 주세요 ~
"""

animal = '강아지'
name = '연탄'
age = 4
hobby = '산책'
is_adult = age >= 3


print('우리집에는' + animal +'가 있는데 강아지 이름은 '+ name +'이예요')
print(name+'는 '+ str(age) +'살이며, '+  hobby+'을 아주 좋아합니다')
print('연탄이는 어른일까요 ?'+ str(is_adult))


print('-'*50)


print('우리집에는' + animal +'가 있는데 강아지 이름은 '+ name +'이예요')
hobby = '공놀이'
print(name+'는 '+ str(age) +'살이며, '+  hobby+'을 아주 좋아합니다')
print('연탄이는 어른일까요 ?'+ str(is_adult))

print('-'*50)
# 콤마(,)사용
# 한 칸씩 띄어쓴다.
# Ctrl + /
print('우리집에는',animal,'가 있는데 강아지 이름은 ', name,'이예요')
print(name,'는 ',str(age),'살이며, ',hobby,'을 아주 좋아합니다')
print('연탄이는 어른일까요 ?', str(is_adult))