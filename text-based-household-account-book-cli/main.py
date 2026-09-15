# 텍스트 기반 가계부 CLI
'''
## 기획
### 기능
- 항목 추가/삭제 : 입력값을 토대로 항목 추가/삭제하기
└ 추가 : 내용, 가격 [인덱스는 자동으로 추가됨], [현재 잔액은 자동으로 계산됨]
└ 삭제 : 인덱스를 받아서 삭제하기.
- 잔액 자동 계산 : 항목에 따라서 전체 잔액 바로바로 계산하기
- 잔액 조회 : 그냥 현재 잔액 보여주기
- 내역 조회 : 원하는 길이 만큼 최근 내역부터 조회하고, 입력값이 길이를 넘으면 모든 걸 보여주기.

### 조건
- 항목은 파일에 저장하고 불러와야함(csv)
'''

if __name__ == "__main__":
    import csv
    from pathlib import Path

    # 매개변수
    fieldnames = ['idx', 'content', 'cost', 'total']
    CSV_PATH = "household-account.csv"

    # 가계부 csv를 리스트로 리턴하는 함수
    def get_csv_list_reader():
        with open(CSV_PATH, "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    return list(reader)[1:]

    # 가계부 파일이 없을 때 새로 만드는 코드
    file_path = Path("household-account.csv")
    if not file_path.exists():
        with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)

    # 메뉴창
    while True:
        choice = input("-"*50 + "\n원하시는 작업을 선택해주세요.\n1. 항목 추가\n2. 항목 삭제\n3. 잔액 조회\n4. 내역 조회\n5. 작업 종료\n번호 또는 작업을 입력해주세요.: ")
        if choice == '1' or choice == '항목 추가':
            # 혹시 몰라서 넣은 매개변수 초기화
            idx = 0
            total = 0

            # content와 cost를 입력받는 코드
            content = input("-"*50 + "\n항목의 내용을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
            if content == 'q': continue
            cost = input("-"*50 + "\n항목의 비용을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
            
            # cost를 정수 타입으로 잘 받기 위한 코드
            while True:
                if cost == 'q':
                    break
                try:
                    cost = int(cost)
                    break
                except ValueError:
                    cost = input("-"*50 + "\n잘못된 값이 입력되었습니다. 항목의 비용을 입력해주세요.: ")
            if cost == 'q': continue
            
            # idx와 total을 csv에서 얻는 코드
            reader_list_original = get_csv_list_reader()
            if len(reader_list_original) > 0:
                idx = int(reader_list_original[-1][0]) # 단순히 마지막 줄을 보고 싶을 뿐인데 모든 값을 리스트로 만드는게 맞나?
                total = int(reader_list_original[-1][3])
            else:
                idx = -1
                total = 0

            # 모든 매개변수들을 가계부에 추가하는 코드
            with open(CSV_PATH, "a", newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([idx+1, content, cost, total+cost])

            print("-"*50 + "\n항목이 작성 되었습니다.")
        elif choice == '2' or choice == '항목 삭제':
            # 가계부가 비어있을 때 삭제할 게 없다고 안내하는 코드
            reader_list_original = get_csv_list_reader()
            if not reader_list_original:
                is_yes = input("-"*50 + '\n삭제할 항목이 없습니다. 메뉴창으로 돌아가시겠습니까? y를 입력해주세요.: ')
                while True:
                    if is_yes == 'y':
                        break
                    else:
                        is_yes = input("-"*50 + '\n잘못된 값이 입력되었습니다. y를 입력해주세요.: ')
                continue
            
            # 삭제할 id를 받는 코드
            idx = input("-"*50 + "\n삭제할 항목의 id를 적어주세요. 취소를 원한다면 q를 입력해주세요.: ")

            
            # 'id를 양의 정수 타입으로 받기'+'가계부의 길이 보다 긴 id를 받았을 때 처리하기' 위한 코드
            while True:
                if idx == 'q':
                    break
                try:
                    idx = int(idx)
                    if idx < 0:
                        idx = input("-"*50 + "\n0보다 크거나 같은 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
                        continue
                    elif idx >= len(reader_list_original):
                        idx = input("-"*50 + f"\n값이 너무 큽니다. {len(reader_list_original)} 보다 작은 수를 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
                        continue                        
                    break
                except ValueError:
                    idx = input("-"*50 + "\n올바른 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
            if idx == 'q': continue

            # 삭제하려는게 정말 id가 맞는지 항목을 보여주면서 재검토
            yes_or_no = input(f'삭제하시려는 항목이 "{', '.join(f'{x}: {y}' for x, y in zip(fieldnames, reader_list_original[idx]))}"이 맞습니까? y 또는 n을 입력해주세요.: ')
            while True:
                if not yes_or_no == 'y' and not yes_or_no == 'n':
                    yes_or_no = input("-"*50 + '\n올바른 값을 입력해주세요. y 또는 n을 입력해주세요.: ')
                else:
                    break

            # 답변이 n이면 다시 메뉴창으로 돌아가는 코드
            if yes_or_no == 'n': continue
            # 답변이 y면 id행을 지우는 코드
            else:
                # idx 행을 지우는 코드
                reader_list = [x for x in reader_list_original if int(x[0]) != idx]

                # idx 행보다 큰 행들의 id를 1씩 빼는 코드
                for x in reader_list[idx:]:
                    x[0] = int(x[0]) - 1
                    x[3] = int(x[3]) - int(reader_list_original[idx][2])

                # 삭제한 리스트로 csv에 다시 쓰는 코드
                with open('household-account.csv', 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fieldnames)
                    writer.writerows(reader_list)

        elif choice == '3' or choice == '잔액 조회':
            # 가계부가 비어있을 때 조회할 게 없다고 안내하는 코드
            reader_list_original = get_csv_list_reader()
            if not reader_list_original:
                is_yes = input("-"*50 + '\n등록된 항목이 없습니다. 메뉴창으로 돌아가시겠습니까? y를 입력해주세요.: ')
                while True:
                    if is_yes == 'y':
                        break
                    else:
                        is_yes = input("-"*50 + '\n잘못된 값이 입력되었습니다. y를 입력해주세요.: ')
                continue

            # 잔고 출력하는 코드
            recently_total = reader_list_original[-1][3]
            print(f'현재 잔고는 {recently_total}원 입니다.')

            # 현재 잔고 볼 시간을 만드는 코드
            is_yes = input('메뉴창으로 돌아가시겠습니까? y를 입력해주세요.: ')
            
            while True:
                if is_yes == 'y':
                    break
                else:
                    is_yes = input('잘못된 값이 입력되었습니다. y를 입력해주세요.: ')

        elif choice == '4' or choice == '내역 조회':
            # 가계부가 비어있을 때 조회할 게 없다고 안내하는 코드
            reader_list_original = get_csv_list_reader()
            if not reader_list_original:
                is_yes = input("-"*50 + '\n등록된 항목이 없습니다. 메뉴창으로 돌아가시겠습니까? y를 입력해주세요.: ')
                while True:
                    if is_yes == 'y':
                        break
                    else:
                        is_yes = input("-"*50 + '\n잘못된 값이 입력되었습니다. y를 입력해주세요.: ')
                continue

            line_count = input('최근 몇 개의 내역을 보시겠습니까? 0보다 큰 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ')

            # line_count를 0보다 큰 정수를 받는 코드
            while True:
                if line_count == 'q':
                    break
                elif not line_count.isdigit():
                    line_count = input("올바른 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
                elif not int(line_count) < len(reader_list_original):
                    print('입력 값이 내역의 길이보다 커서 내역 전체를 출력합니다.')
                    line_count = len(reader_list_original)
                    break
                elif line_count == '0':
                    line_count = input("0보다 큰 값을 입력해주세요. 취소를 원한다면 q를 입력해주세요.: ")
                else:
                    line_count = int(line_count)
                    break
            if line_count == 'q': continue

            # line_count개의 항목을 인출하는 코드
            for i in reader_list_original[-line_count:]:
                print(', '.join(f'{x}: {y}' for x, y in zip(fieldnames, i)))

            # 내역 아래 바로 메뉴가 떠서 내역이 가려져서 한 번 선택지를 둬서 볼 시간을 두는 코드
            is_yes = input('메뉴창으로 돌아가시겠습니까? y를 입력해주세요.: ')
            while True:
                if is_yes == 'y':
                    break
                else:
                    is_yes = input('잘못된 값이 입력되었습니다. y를 입력해주세요.: ')

        elif choice == '5' or choice == '작업 종료':
            print('감사합니다. 다음에 또 이용해주세요.')
            break
        else:
            print("!!!올바른 값을 입력해주세요.!!!")