-- Creating Menu table ---

create table menu 
(
id int identity(1,1),
food_name varchar(60),
price decimal
)



-- inserting the table with data ---

begin
insert into menu 
(food_name,price)
values('Mutton Biriyani',250.0);
insert into menu 
(food_name,price)
values('Chicken Biriyani',180.0);
insert into menu 
(food_name,price)
values('Black Forest',100.0);
insert into menu 
(food_name,price)
values('Lassi',80.0);


end;


--- select the menu table---


select * from menu

--- Order details ---


create table Order_details
( id int identity(1,1),
food_name varchar(50),
qty int,
customer_name varchar(70))


select food_name,qty from Order_details where customer_name='Azar'

select * from Order_details


truncate table Order_details 


--- Billing Table---

create table bill_table
(
id int identity(1,1),
bill_no int,
customer_name varchar(60),
foodname varchar(60),
quantity int,
bill_amount decimal)


drop table bill_table;

select isnull(max(bill_no),0) from bill_table

truncate table bill_table;

select bill_no as [Bill Number], foodname as  Dish , quantity as Quantity, bill_amount as Amount from bill_table where bill_no=1

select food_name as Food, qty as Quantity from Order_details where customer_name='Azar'