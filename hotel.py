from operator import index
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pyodbc
import pandas as pd
from tabulate import tabulate


"""  
DB is connected to python


"""
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=CB-CH-L-0062;'
                      'Database=hotel_db;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()

data= pd.read_sql("select * from menu",con=connection)

connection.timeout = 60
connection.autocommit = True


print("**********************    Hi Welcome to Hotel xxxx       **********************")

print("       MENU           ")

print(tabulate(data, headers = 'keys', tablefmt = 'psql'))

print("    ******  Please order your food  *****     ")


name =input(" Enter Your Name :")

food_name = input("Hi {} Give the food name :".format(name))

food_list = food_name.split(',')


dict={}
for a in food_list:
    val=input(" Quantity of {} :".format(a))
    cursor.execute("Insert into order_details(food_name,qty,customer_name) values(?,?,?)",a,val,name)
    dict[a]=val

print("***********   Please Confirm Your Order      ***********")


order_query="select food_name as Food, qty as Quantity from Order_details where customer_name=''{}''".format(name)
order_display=pd.read_sql("select food_name as Food, qty as Quantity from Order_details where customer_name={}".format(name),con=connection)

print(tabulate(order_display, headers = 'keys', tablefmt = 'psql'))

print("************** PLEASE CONFIRM YOUR ORDER *************")

bill=pd.read_sql("select isnull(max(bill_no),0) as cnt from bill_table",con=connection)

bill_no=int(bill["cnt"])+1

amount=0
c_amount=0
m_amount=0
b_amout=0
l_amount=0
for key,value in dict.items():
    if key=="Chicken Biriyani":
        c_amount+=180*int(value)
        cursor.execute("insert into bill_table(bill_no,customer_name,foodname,quantity,bill_amount) values(?,?,?,?,?)",bill_no,name,key,value,c_amount)
    elif key=="Mutton Biriyani":
        m_amount+=250*int(value)
        cursor.execute("insert into bill_table(bill_no,customer_name,foodname,quantity,bill_amount) values(?,?,?,?,?)",bill_no,name,key,value,m_amount)
    elif key=="Black Forest":
        b_amout+=100*int(value)
        cursor.execute("insert into bill_table(bill_no,customer_name,foodname,quantity,bill_amount) values(?,?,?,?,?)",bill_no,name,key,value,b_amout)
    elif key=="Lassi":
        l_amount+=80*int(value)
        cursor.execute("insert into bill_table(bill_no,customer_name,foodname,quantity,bill_amount) values(?,?,?,?,?)",bill_no,name,key,value,l_amount)
    
amount=c_amount+m_amount+b_amout+l_amount

print("******************* Please Check Your Bill *******************")


query="select bill_no as [Bill Number], foodname as  Dish , quantity as Quantity, bill_amount as Amount from bill_table where bill_no={}".format(bill_no)
bill_data = pd.read_sql(query,con=connection)

print(tabulate(bill_data, headers = 'keys', tablefmt = 'psql'))

print("Your Bill Amount is : {}".format(amount))

