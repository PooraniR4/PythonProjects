import sqlite3

con = sqlite3.connect("Assignment.db")

create='''create table if not exists tab_assignment('Name','ID','Quantity','Price')'''
con.execute(create)

insert='''Insert into tab_assignment('Name','ID','Quantity','Price') Values('A','A01',3,500)'''
con.execute(insert)
con.commit()

insert_records=[('B','B01',4,250), ('C','C01',1,350), ('D','D01',2,450)]
con.executemany('Insert into tab_assignment values(?,?,?,?)',insert_records)
con.commit()

select='''select * from tab_assignment'''
con.execute(select)
con.commit()

con.close()