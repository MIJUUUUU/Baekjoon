import sys  # 표준 입력을 읽기 위해 sys 모듈을 임포트
answer=[]# 결과를 저장할 빈 리스트를 초기화

for line in sys.stdin:# 표준 입력에서 추가 입력 줄을 읽어들이는 루프를 시작
    a, b = map(int, line.split()) # 입력 줄에서 정수 두 개를 읽어옵니다. 공백으로 구분
    if a == 0 and b == 0:
        break
    answer.append(a+b)

for i in answer:
    print(i)
