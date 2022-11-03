import sqlite3
conn = sqlite3.connect('q1.db')
print('Connected to SQLite')


c = conn.cursor()
c.execute("SELECT COUNT(*) FROM customers where grade>200 order by id")
rows_num = c.fetchone()
print('Total rows are:   '+str(rows_num[0]))
print('Printing each row')
c.execute("select * from customers where grade>200 order by id")
rows = c.fetchall()
for row in rows:
    print('Id:  ' + str(row[0]) +
          '\nName:  ' + str(row[1]) +
          '\nCity:  ' + str(row[2]) +
          '\nGrade:  ' + str(row[3]) +
          '\nSeller:  ' + str(row[4])+'\n\n')


c.close()
conn.close()
print('The SQLite connection is closed')
