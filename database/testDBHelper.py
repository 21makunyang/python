from DBHelper import db
v1=db.fetch_one("select * from student;")
print(v1)