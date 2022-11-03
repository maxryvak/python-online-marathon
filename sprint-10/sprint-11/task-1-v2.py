import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('sqlite:///q1.db')

metadata = MetaData(engine)
customer_table = Table('customers', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String),
                       Column('city', String),
                       Column('grade', Integer),
                       Column('salesperson_id', String)
                       )
Session = sessionmaker(bind=engine)
session = Session()


class Customer:
    def __init__(self, id, name, city, grade, salesperson_id):
        self.id = id
        self.name = name
        self.city = city
        self.grade = grade
        self.salesperson_id = salesperson_id

    def __repr__(self):
        return (f'Id:  {self.id}\nName:  {self.name}'
                f'\nCity:  {self.city}\nGrade:  {self.grade}'
                f'\nSeller:  {self.salesperson_id}\n\n')


mapper(Customer, customer_table)
print('Connected to SQLite')
count = session.query(Customer).filter(Customer.grade > 200).count()

print('Total rows are:   ' + str(count))
print('Printing each row')
for row in session.query(Customer).filter(Customer.grade > 200).order_by(Customer.id):
    print(str(row))

print('The SQLite connection is closed')
