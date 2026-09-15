# 개발 일지 - 텍스트 기반 가계부 CLI

## 2026-09-13

### 오늘 한 일
- Git 공부 및 초기 세팅
- 프로젝트 기획
- 코드 작성(틀만 작성함)

### 배운 것 / 새로 안 것
- Git 초기 세팅법
  ```bash
  # 컴퓨터 단위
  git config --global user.name "이름"
  git config --global user.email "이메일"

  # 폴더 단위
  cd "원하는 폴더"
  git init
  git remote add origin <url>
  git add .
  git commit -m "first commit"
  git branch -M main
  git push -u origin main
  ```

- 초기 세팅 후 평소 작업 루틴
  ```bash
  git add <commit할 파일>
  git commit -m "작업 내용"
  git push
  ```
  다만 vscode를 쓸 때는 vscode의 commit/push 버튼을 사용하면 편하다.

- Github이랑 로컬이랑 로그가 달라서 오류 날 때
  ```bash
  git pull origin main --allow-unrelated-histories
  ```

- Git의 저장방식에 대한 직관적인 느낌: 역사나 변경 사항을 저장한다.

### 막힌 것 / 헷갈렸던 것
- 문제 상황:
- 시도해본 것:
- 아직 해결 안 됐으면 → 다음에 시도할 것 적어두기

### 오늘의 코드/실험 스니펫


### 느낀 점 / 메모


### 다음에 할 일
- [ ] 남은 코드 작성하기


### 참고자료

---

## 2026-09-14

### 오늘 한 일
- 전체 코드 작성
- csv 모듈 공부

### 배운 것 / 새로 안 것
- csv 모듈: 함수가 몇 개 없어서 쉬웠다.
  ```python
  import csv

  with open('main.txt', 'r') as f:
    reader = csv.reader(f)

  with open('main.txt', 'w') as f:
    writer = csv.writer(f)
  ```
  위 코드처럼 초기 세팅하고 이후에 원하는 작업을 한다. 자세한 내용은 참고 자료

- csv 모듈 dict-- 함수: `csv.DictReader()`, `csv.DictWriter()`함수가 있는데 csv를 딕셔너리로 읽어줘서 유용하다.
  자세한 내용은 참고 자료

- 2차원 리스트에서 안쪽 리스트를 바꿔도 원본 리스트에서 잘 바뀐다. 다음 코드 보는게 더 이해잘된다.
  ```python
  a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  for x in a:
    x[0] = 3
  print(a)

  # [[3, 2, 3], [3, 5, 6], [3, 8, 9]]
  ```
  아래 코드 처럼 가장 바깥 리스트(원본)을 안데려와도 된다는걸 짚고싶었다.
  ```python
  a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  for i, x in enumerate(a):
    a[i][0] = 3
  print(a)

  # [[3, 2, 3], [3, 5, 6], [3, 8, 9]]
  ```

### 막힌 것 / 헷갈렸던 것
- 문제 상황:
- 시도해본 것:
- 아직 해결 안 됐으면 → 다음에 시도할 것 적어두기

### 오늘의 코드/실험 스니펫 (선택)


### 느낀 점 / 메모
- **원하는 값이 입력이 안됐을 때**를 해결하는 코드가 엄청 들어갔고, 아마 다른 프로젝트에서도 그럴 것 같다.
- 정수만 받는 코드, 양의 정수만 받는 코드가 2번 정도 나왔다.
- 삭제 기능 코드 짜는게 제일 힘들었고, 그 다음은 추가 기능 코드, 내역 확인 코드, 잔액 확인 코드 순으로 힘들었다.
- 삭제 기능이 생각보다 생각해야할 게 많은 부분이였다.

### 다음에 할 일
- [ ] 코드 리뷰

### 참고 자료
- https://nerogarret.tistory.com/63
- https://devpouch.tistory.com/55


---

## 2026-09-15

### 오늘 한 일
- Claude한테 코드 리뷰 받기 및 피드백 반영
- 코드 리뷰 중 '삭제' 기능에서 최신화에 total은 반영안한걸 발견 -> 코드 추가 작성
- 코드 리뷰 중 가계부가 텅 비면 대부분의 기능이 오류나는걸 발견 -> 코드 추가 작성

### 배운 것 / 새로 안 것
- 중간에 있는 항목을 삭제할 때 remove()로 삭제하는 것 보단 리스트 컴프리헨션으로 새로 만드는게 좋다. 인덱스를 건너뛰는 버그가 생기기 쉬움.
  내가 짠 코드:
  ```python
  with open('household-account.csv', 'r', encoding='utf-8') as f:
      reader = csv.reader(f)
      reader_list = list(reader)[1:]
  for x in reader_list:
      if int(x[0]) == id:
          reader_list.remove(x)
  ```
  권장 코드:
  ```python
  with open('household-account.csv', 'r', encoding='utf-8') as f:
      reader = csv.reader(f)
      reader_list = [x for x in list(reader)[1:] if x[0] != id]
  ```

- '삭제' 코드에서 필요 이상으로 4번이나 파일을 열었는데 처음 한 번 열었을 때 메모리에 저장해두고 재사용하는게 좋다.
  아래 코드 처럼 한 번 변수에 담고 그걸 계속 재사용하기.
  ```python
  with open('household-account.csv', 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    reader_list_original = list(reader)[1:]
  ```

- 리스트 슬라이싱 할 때 시작 인덱스를 리스트 길이보다 크게해도 오류가 나는게 아니라 빈리스트가 출력되서 굳이 예외처리 안해도 된다.
  내가 쓴 코드(굳이 안해도 되는 예):
  ```python
  if id != len(reader_list):
      if id != len(reader_list):
          for x in reader_list[id:]:
              x[0] = int(x[0])-1
  ```
  권장 코드:
  ```python
  if id != len(reader_list):
      for x in reader_list[id:]:
          x[0] = int(x[0])-1
  ```

- 정수만을 받고 싶은 코드를 짤 때 lstrip() 함수를 쓰면 '--10000'같은, replace() 함수를 쓰면 '5-5'같은 잘못된 값을 받는 오류가 있다. 그래서 int()함수를 try/except으로 감싸는게 실무에서도 가장 안전하고 표준적인 방법이다.
  옳지 않은 예:
  ```python
  elif not cost.lstrip('-').isdigit():
  ```
  옳지 않지 예:
  ```python
  elif not cost.replace('-', '', 1).isdigit():
  ```
  ```python
  try:
    cost = int(cost)
    break
  except ValueError:
    cost = input("...")
  ```

- 변수 이름을 id로 쓰면 내장 함수 id()랑 이름이 똑같아서 나중에 만약 오류가 난다면 디버깅하기 어려워진다. item_id, idx 같은걸 쓰는걸 권장한다.

- 파일이 같은 디렉터리에 있는지 확인하고 싶을 때 pathlib 내장 모듈을 사용하면 된다. <- 좋은 거라고 칭찬받음
  ```python
  from pathlib import Path
  file_path = Path("file_name")
  if file_path.existis():
    print("파일이 존재합니다.")
  ```

- 나는 항목 삭제를 하면 그 뒤에 있는 항목들의 id를 재넘버링 해줬는데 실제로는 그냥 고윳값처럼 냅둔다고 한다.
- total 값을 매 행에 저장하기 보다는 필요할 때 계산하는게 안전하다고 한다.
- 파일을 통째로 열어서 'w'로 덮어쓰는 방식보다는 임시 파일을 만들어서 거기에 쓰고 os.replace 함수로 원본 이름으로 교체하는게 안전하다. 기존 방법이라면 파일을 쓰다가 꺼졌을 때 나머지 모든 내용이 사라진다.
- 나는 컬럼을 대괄호로 많이 불러왔는데 실무에서는 csv.DictReader, csv.DictWriter로 이름 기반 접근을 하는게 좋다.
- 타입 힌트는 실무에서 거의 기본이지만 나는 하나도 사용하지 않았다.



### 막힌 것 / 헷갈렸던 것
- 문제 상황:
- 시도해본 것:
- 아직 해결 안 됐으면 → 다음에 시도할 것 적어두기

### 오늘의 코드/실험 스니펫


### 느낀 점 / 메모
- 코드 리뷰 중 함수 분리가 전혀 안되있다고 지적받았다. 이번 프로젝트는 시간이 너무 많이 들거 같아서 다음 프로젝트부터 함수 분리를 꼼꼼하게 하기로 판단했다.
  이번 코드에서 함수로 만들면 좋았던거: 추가, 삭제, 잔액확인, 내역확인, 파일 읽고 list로 만들기, 파일 쓰기, 입력값 정수로 받기

### 다음에 할 일


### 참고자료

---