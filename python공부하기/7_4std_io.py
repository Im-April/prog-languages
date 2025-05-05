import pickle

# profile_file = open('profile.pickle','wb')
# profile = {'이름':'최산','나이':25,'취미':['축구','골프','코딩']}
# print(profile)
# pickle.dump(profile,profile_file) # 프로필에 있는 정보를 프로필파일에 저장
# profile_file.close()

profile_file = open('profile.pickle','rb')

# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file) # 파일에 있는 내용을 가지고와서 데이터 형태로 불러옴
print(profile)
profile_file.close()