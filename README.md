# 방탈출 카페 크롤러

## 실행 방법

1. 파이썬 설치

   ```bash
   # Mac OS
   $ brew install pyton3
   ```

2. 가상 환경 구성

   ```bash
   $ python3 -m venv .venv
   ```

3. 가상 황경 실행

   ```bash
   $ source .venv/bin/activate
   ```

4. 가상 환경에 패키지 설치

   ```bash
   # requests
   $ pip install requests
   ```

   ```bash
   # BeautifulSoup4
   $ pip install bs4
   ```

5. 크롤러 실행

   ```bash
   python colory_room_escape_crawler.py
   ```

## 실행 종료

1. 가상 환경 비활성화

   ```bash
   $ deactivate
   ```

## 의존성 요구사항

- python3
- requests
- bs4
