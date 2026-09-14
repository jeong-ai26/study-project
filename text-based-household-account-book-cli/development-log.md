# 개발 일지 - 텍스트 기반 가계부 CLI

## 2026-09-13

### 오늘 한 일
- Git 공부 및 초기 세팅
- 기획
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
- 코드 작성
- csv 모듈 공부

### 배운 것 / 새로 안 것


### 막힌 것 / 헷갈렸던 것
- 문제 상황:
- 시도해본 것:
- 아직 해결 안 됐으면 → 다음에 시도할 것 적어두기

### 오늘의 코드/실험 스니펫 (선택)


### 느낀 점 / 메모


### 다음에 할 일


### 참고자료
- https://nerogarret.tistory.com/63
- https://devpouch.tistory.com/55


---