data = input()
print(f"입력받은 데이터: '{data}'")  # 뭐가 들어왔는지 확인
print(f"split 결과: {data.split()}")  # 분리 결과 확인
A, B = map(int, data.split())
print(A + B)