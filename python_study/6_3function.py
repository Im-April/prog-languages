def profile(name,age,main_lang):
    print(f'이름 : {name}\n 나이 : {age}\n 사용 언어 : {main_lang}')


profile('권하마루',2,'python')


# 기본값 설정

def profile(name,age=17,main_lang='python'):
    print(f'이름 : {name}\n 나이 : {age}\n 사용 언어 : {main_lang}')


profile('권마루')
profile('똥마루')