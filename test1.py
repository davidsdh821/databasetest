from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작
#insert: 데이터 넣기
# find: 찾기
# update: 업뎃
#delete: 삭제
doc = {'name':'jane','age':21}
db.users.insert_one(doc)
#몽고 db는 계속해서 쌓이는 형태, doc의 값을 바꿔 실행하면 이전에 데이터 위에 쌓인다.