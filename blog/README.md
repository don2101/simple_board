# 블로그 만들기

## I. 개발 환경
- 플랫폼 : c9
- RDMS : sqlite3
- 언어 : python


## II. 사용 기능

### (1) Flask
- flask를 사용하여 웹상에 블로그 글 정보를 출력
- POST방식으로 글 생성, 수정, 삭제 요청을 받고, request를 사용하여 요청 변수를 받음
- form태그를 사용하여 유저로 부터 title, content, author를 입력받고 datetime으로 현재 시간을 측정하여 DB에 저장
- 글 생성, 수정시 가장 최근에 생성된 글의 id번호를 가져와 생성, 수정된 글로 이동할 수 있는 경로 생성


### (2) Database
- CREATE문으로 table을 생성
- 사용자에게 글에 대한 정보를 입력받아 INSERT INTO 문으로 table에 저장
- 사용자 요청시에 UPDATE, DELETE문으로 글을 수정하거나 삭제