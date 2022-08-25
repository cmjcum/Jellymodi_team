<p align="center"><img src="https://user-images.githubusercontent.com/104331479/185329655-95f41df4-dec5-4e94-b6b8-471a0ef2deba.png" width="80%" height="80%"></p>

# <img src="https://user-images.githubusercontent.com/104331479/185330319-86af99b3-0eb2-4a75-a0c4-2b36808a3734.png" width="30" height="30"/> Project Jellymodi

**머신러닝 사물인식 프로젝트 - 젤리모디(Jellymodi: Jelly mood diary)**

Python OpenCV 를 이용하여 얼굴 표정을 인식하고, 분석한 표정에 해당하는 젤리 이모티콘을 넣어 일기를 쓰는 웹사이트 제작
***

# ⭐Intro
* mood tracker 기법을 사용하는 일기 작성 서비스
* Python OpenCV 을 이용한 얼굴인식
* 한국인 얼굴 표정 데이터 분석을 학습시킨 모델 제작 (데이터셋 : <a href="https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=82">AIHub - 한국인 감정인식을 위한 복합 영상</a>)
* S.A(Starting Assignment) : https://typingmylife.notion.site/Jellymodi-5e43c9f96bb04da7b4de26aac6eceeca

<div>
   <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
   <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
   <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">
</div>

***

# 📌Project
* 시연영상 : https://ddongkim.tistory.com/37

<video width="100%" height="100%" controls="controls">
  <source src="젤리모디_시연영상.mp4" type="video/mp4">
</video>

* 목적 : backend 실력 향상 ( HTML, JavaScript, Ajax, Python, Flask, MongoDB )
* 1차 목표 : 인스타 페이지 기본기능 구현
  * 회원가입, 로그인, 로그아웃 기능 (JWT 사용)
  * 메인페이지 게시물(CRUD), 게시물 활동
  * 캠/사진을 통한 얼굴인식 → 머신러닝 사물인식 모델을 이용한 감정판별 → 해당 표정에 맞는 이모티콘 표시
* 2차 목표 : 부가기능 구현
  * 구글로그인 연동기능
***

# 👨‍👨‍👧‍👧TEAM Coumi
**팀 코우미 (코딩못하면 우는 미니언즈)**
| 팀원 | 이름 | 역할 | 깃허브 |
|:----------:|:----------:|:----------:|:----------:|
| 대장 미니언 (팀장) | **이정아** | 일기 조회 페이지 | <a href="https://github.com/zeonga1102"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a> |
| 디자이너 미니언 | **노을** | 메인 페이지 | <a href="https://github.com/minkkky"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a> |
| 기획자 미니언 | **이현경** | 로그인 및 회원가입 페이지 | <a href="https://github.com/LULULALA2"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a> |
| 막내 미니언 | **김동근** | 일기 작성 페이지 | <a href="https://github.com/cmjcum"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a> |
* 모델제작 - 팀 전체 참여

***

# ✏기획 및 일정
* 와이어프레임

![피그마 목업](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcoToUW%2FbtrCumtehoi%2FKCUpBnVBXOQhBOQnIMz4WK%2Fimg.png)

* 젤리티콘 제작

![젤리티콘제작](https://user-images.githubusercontent.com/104331479/185370310-7f77facf-19a5-43e2-8b67-f8bc4e62302d.PNG)

* 일정

![일정 관리](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdpoO9z%2FbtrCuVvoecp%2FV9ZiulP6KUSxxo8lWLfIG0%2Fimg.png)

***

# 실행화면
* 로그인 & 메인화면
![로그인-메인화면](https://user-images.githubusercontent.com/104331479/185368926-32a15726-98a1-47c1-a4a5-a5e025da8d36.png)

* 글작성
![글작성](https://user-images.githubusercontent.com/104331479/185368976-bee79add-1ff6-4aac-b344-394ab8a7ad08.png)

* 글 상세 & 메뉴
![글상세-모달](https://user-images.githubusercontent.com/104331479/185369005-ffd33b83-e248-4bb5-96ae-e0fc4d328218.png)
