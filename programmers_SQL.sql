-- 강원도에 위치한 생산공장 목록 출력하기

-- 문제 설명

-- 다음은 식품공장의 정보를 담은 FOOD_FACTORY 테이블입니다. 
-- FOOD_FACTORY 테이블은 다음과 같으며 FACTORY_ID, FACTORY_NAME, ADDRESS, TLNO는 각각 공장 ID, 공장 이름, 주소, 전화번호를 의미합니다.

-- 문제

-- FOOD_FACTORY 테이블에서 강원도에 위치한 식품공장의 공장 ID, 공장 이름, 주소를 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 공장 ID를 기준으로 오름차순 정렬해주세요.

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID

-- 조건에 부합하는 중고거래 댓글 조회하기

-- 문제 설명

-- 다음은 중고거래 게시판 정보를 담은 USED_GOODS_BOARD 테이블과 중고거래 게시판 첨부파일 정보를 담은 USED_GOODS_REPLY 테이블입니다. USED_GOODS_BOARD 테이블은 다음과 같으며 BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.
-- USED_GOODS_REPLY 테이블은 다음과 같으며 REPLY_ID, BOARD_ID, WRITER_ID, CONTENTS, CREATED_DATE는 각각 댓글 ID, 게시글 ID, 작성자 ID, 댓글 내용, 작성일을 의미합니다.

-- 문제

-- USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.

SELECT
    B.TITLE,
    B.BOARD_ID,
    R.REPLY_ID,
    R.WRITER_ID,
    R.CONTENTS,
    DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') CREATED_DATE
FROM
    USED_GOODS_BOARD B INNER JOIN USED_GOODS_REPLY R
ON B.BOARD_ID = R.BOARD_ID
WHERE B.CREATED_DATE < '2022-11-01' AND B.CREATED_DATE >= '2022-10-01'
ORDER BY
    CREATED_DATE,
    TITLE