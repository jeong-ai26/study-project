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
fieldnames = ['id', 'content', 'cost', 'total']

while True:
    a = input("-"*50 + "\n원하시는 작업을 선택해주세요.\n1. 항목 추가\n2. 항목 삭제\n3. 잔액 조회\n4. 내역 조회\n5. 작업 종료\n번호 또는 작업을 입력해주세요.: ")
    if a == '1' or a == '항목 추가':
        # 항목 추가할 때 필요한 매개변수 초기화
        id = 0
        content = input("항목의 내용을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
        if content == 'q': continue
        cost = input("항목의 비용을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
        total = 0

        # cost를 정수 타입으로 잘 받기 위한 코드
        while True:
            if cost == 'q':
                break
            elif not cost.lstrip('-').isdigit():
                cost = input("잘못된 값이 입력되었습니다. 항목의 비용을 입력해주세요.: ")
            else:
                cost = int(cost)
                break
        if cost == 'q': continue
        
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
        # 항목 삭제 할 때 필요한 매개변수들
        id = input("삭제할 항목의 id를 적어주세요. 취소를 원한다면 q를 입력해주세요.: ")

        
        # 'id를 양의 정수 타입으로 받기'+'가계부의 길이 보다 짧은 id를 받기' 위한 코드
        with open('household-account.csv', 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    l = list(reader)[1:]
        
        while True:
            if id == 'q':
                break
            elif not id.isdigit():
                id = input("올바른 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
            elif not int(id) < len(l):
                id = input("값이 너무 큽니다. 올바른 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
            else:
                id = int(id)
                break
        if id == 'q': continue

        # 삭제하려는게 정말 id가 맞는지 항목을 보여주면서 재검토
        with open('household-account.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            yes_or_no = input(f'삭제하시려는 항목이 {list(reader)[id]}이 맞습니까? y 또는 n을 입력해주세요.: ')
        while True:
            if not yes_or_no == 'y' and not yes_or_no == 'n':
                yes_or_no = input('올바른 값을 입력해주세요. y 또는 n을 입력해주세요.: ')
            else:
                break

        # 답변이 n이면 다시 메뉴창으로 돌아가는 코드
        if yes_or_no == 'n': continue
        # 답변이 y면 id행을 지우는 코드
        else:
            with open('household-account.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                reader_list = list(reader)[1:]
            for x in reader_list:
                if int(x[0]) == id:
                    reader_list.remove(x)
            if id != len(reader_list):
                for x in reader_list[id:]:
                    x[0] = int(x[0])-1
            with open('household-account.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fieldnames)
                writer.writerows(reader_list)

    elif a == '3' or a == '잔액 조회':
        pass
    elif a == '4' or a == '내역 조회':
        pass 
    elif a == '5' or a == '작업 종료':
        break
    else:
        print("올바른 값을 입력해주세요.")