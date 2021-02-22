## 🗓 프로젝트 기간

- 2021.02.19 - 2021.02.22 (총 4일)

  

## 🌊 프로젝트 플로우

1. Project modeling (AQuery Tool)

2. Project setting (용도별 세팅 분리 /  시크릿키, 데이터베이스 정보 json으로 관리)

3. User 앱 작성 (Test → Model → Serializer → View → Url)

4. Product 앱 작성 (Test → Model → Serializer → View → Url)

5. Order 앱 작성 (Test → Model → Serializer → View → Url)

6. 회고록 (Private)

   

## 🪧 모델링

**User**

- 유저 테이블 가이드라인 따라서 생성

**Product**

- 상품 테이블 가이드라인 따라서 생성

**Order**

- 주문 테이블 가이드라인 따라서 생성
- 주문 상품(장바구니 역할) 테이블 생성 / 정규화해서 테이블 분할
- 상품 상태 추가 / 정규화해서 테이블 분할

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b17590ff-4eb4-40cd-ad47-e0d9f4376529/Screen_Shot_2021-02-21_at_4.53.11_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210221T082047Z&X-Amz-Expires=86400&X-Amz-Signature=1e0726137947ad343613c881708244d0cf94087cc1d16245e743107c9030a9be&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Screen_Shot_2021-02-21_at_4.53.11_PM.png%22)



## ⚡️ 구현 기능

**Project Setting**

- AQuery Tool 사용 모델링
- 용도별 세팅 분리 /  시크릿키, 데이터베이스 정보 json으로 관리
- drf-yasg(Swagger) 이용해 API 문서화

**Core**

- Django User 모델 AbstractUser 모델로 확장
- 유저 생성시 자동 토큰 발급 구현
- Admin 페이지 모델에 맞게 구현 (유저 정보 생성, 조회, 수정, 삭제 및 앱 별 관리 가능)
- 테스트 코드 작성

**User**

- 회원가입 / 로그인 API
- 유저 본인 정보 조회 가능 (관리자는 모든 회원 정보 조획 가능)
- 유저 본인 정보만 수정 가능 (관리자는 모든 정보 수정 가능)
- 테스트 코드 작성

**Product**

- 상품 기능은 관리자만 접근 가능
- 상품 CRUD (등록/조회/수정/삭제)
- 상품 리스트 API / 상세 API
- 상품 최신 순 정렬 및 필터링 구현
- 오버라이딩 함수로 유저 상품 조회(list, retrieve) 구현

**Order**

- 유저 본인의 주문 확인과 관리자의 모든 접근 허용을 위한 IsUserOrAdmin(custom permission) 구현
- Get(list) 접근 피하기 위해 ModelViewSet이 아닌 mixins & GenericViewSet 활용
- ForeignKey id가 아닌 적절한 속성을 가져오기 위한 source attribute 사용
- 주문 API에서 상품 확인할 수 있도록 reverse relationship 구현