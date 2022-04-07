from  db_context import Connect

with Connect() as obj:

    v1 = obj.fetch_one("select * from student")
    print(v1)

    v2 = obj.fetch_one("select * from student where sid =%(nid)s",nid=2)
    print(v2)