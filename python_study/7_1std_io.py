print('python','java')
print('python'+'java')

print('python','java',sep=",")
print('python','java',sep=" vs ")
print('python','java','javascript',sep=" vs ")
print('python','java','javascript',end='?') # 문장의 끝 부분을 ?로 바꿔라
print('무엇이 더 재밌을까요?')
print('-'*30)

import sys
print('python','java',file=sys.stdout) # 표준출력으로 처리
# print('python','java',file=sys.stderr) # 표준에러로 처리

print('-'*30)
score = {'수학':0, '영어':50, '코딩':100}
for subject, score in score.items():
	print(subject.ljust(8), str(score).rjust(4), sep=':')
print('-'*30)

for num in range(1,21):
	print('대기번호 : '+ str(num).zfill(3))

print('-'*30)

# 표준 입력
answer = input('아무 값이나 입력하세요 : ')
print(type(answer)) # input은 항상 문자열 형태로 저장됨
print(f'입력하신 값은 : {answer} 입니다.')