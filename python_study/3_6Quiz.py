'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예)http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + '!'로 구성
예 ) 생성된 비밀번호 : nav51!
'''


#site = 'http://naver.com'
# rule1 = site[7:]
# rule2 = rule1[:5]
# rule3_1 = rule2[:3]
# rule3_2 = len(rule2)
# rule3_3 = rule2.count('e')

# print(rule3_1 + str(rule3_2) + str(rule3_3) + '!')

url = 'http://google.com'

my_str = url.replace('http://','') # 규칙1
my_str2 = my_str[:my_str.index('.')] # 규칙2
password = my_str2[:3]+str(len(my_str2))+str(my_str2.count('e')) + '!' # 규칙3
print(f'{url}의 패스워드는 {password}입니다.')


