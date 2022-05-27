from Product import *
import sqlite3 as sql
from typing import List

# 샘플 데이터 로드 함수, 처음에 한번만 호출할 것.
def loadSample():
    conn = sql.connect("../database/test.db")
    
    # 동일 쿼리에 여러 데이터를 동시에 입력
    with conn:
        cur = conn.cursor()
        query = 'INSERT INTO product(name, price) VALUES (?, ?)'
        cur.executemany( query, 
            [ ('삼성 갤럭시 Z플립', 1500000),
            ('애플 아이폰 13 프로맥스', 2000000),
            ('애플 아이폰 13 미니', 1200000)
            ]
        )

# 전체 상품 목록 제공 함수
def getAll() -> List[Product]:
    conn = sql.connect("test.db")
    list: List[Product] = []

    with conn:
        cur = conn.cursor()

        # 전체 데이터 가지고 오기
        cur.execute('select * from product')

        rows = cur.fetchall()
        
        for row in rows:
            p = Product(row[0], row[1], row[2])
            list.append(p)
    return list

# 선택한 상품 객체를 찾아서 리턴
def get(id) -> Product:
    conn = sql.connect("../database/test.db")
    with conn:
        cur = conn.cursor()
        query = 'select * from product where pid=?'
        cur.execute(query, id)

        # 하나를 가지고 와라
        row = cur.fetchone()

    return Product(row[0], row[1], row[2])