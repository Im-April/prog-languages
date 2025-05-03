jumin = '990120-1234567'

print('성별 : '+ jumin[7]) # 1
print('연도 : '+ jumin[0:2]) # 99 , jumin[:2]도 가능
print('월 : ' + jumin[2:4]) # 01
print('일 : ' + jumin[4:6]) # 20
print('생년월일 : ' + jumin[:6]) # 990120
print('주민 뒤 7자리 : ', jumin[7:]) # = jumin[7:14] 
print('뒤 7자리 (뒤에서부터) ' + jumin[-7:])