# 텍스트 기반 가계부 CLI
'''
## 기획
### 기능
- 항목 추가/삭제 : 입력값을 토대로 항목 추가/삭제하기
└ 추가 : 내용, 가격, [인덱스는 자동으로 추가됨], [현재 잔액은 자동으로 계산됨]
└ 삭제 : 내용 또는 인덱스를 받아서 삭제하기.
- 잔액 자동 계산 : 항목에 따라서 전체 잔액 바로바로 계산하기
- 잔액 조회 : 그냥 현재 잔액 보여주기
- 가계부 조회 : 원하는 길이 만큼 조회하고, 입력값이 길이를 넘으면 모든 걸 보여주기.
최대 길이는 30줄로 제한

### 조건
- 항목은 파일에 저장하고 불러와야함(csv)
'''
import csv


while True:
    a = input("-"*50 + "\n원하시는 작업을 선택해주세요.\n1. 항목 추가\n2. 항목 삭제\n3. 잔액 조회\n4. 내역 조회\n5. 작업 종료\n번호 또는 작업을 입력해주세요.: ")
    if a == '1' or a == '항목 추가':
        # 항목 추가할 때 필요한 매개변수들
        id = 0
        content = input("항목의 내용을 입력해주세요.: ")
        cost = input("항목의 비용을 입력해주세요.: ")
        total = 0

        # cost를 정수 타입으로 잘 받기 위한 코드
        b = True
        while b:
            try:
                cost = int(cost)
                b = False
            except ValueError:
                cost = input("항목의 비용을 입력해주세요.: ")

        # id와 total을 얻기 위한 코드
        with open("household-account.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            l = list(reader)[-1]
            id = int(l[0]) # 단순히 마지막 줄을 보고 싶을 뿐인데 모든 값을 리스트로 만드는게 맞나?
            total = int(l[3])

        # 모든 매개변수들을 csv의 마지막 줄에 추가하는 코드
        with open("household-account.csv", "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([id+1, content, cost, total+cost])

        print("항목이 작성 되었습니다.")
    elif a == '2' or a == '항목 삭제':
        pass
    elif a == '3' or a == '잔액 조회':
        pass
    elif a == '4' or a == '내역 조회':
        pass 
    elif a == '5' or a == '작업 종료':
        break
    else:
        print("올바른 값을 입력해주세요.")