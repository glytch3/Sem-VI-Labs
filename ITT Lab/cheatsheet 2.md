sqlite:
create db
import sqlite3
conn=sqlite3.connect('student.db')
conn.execute("CREATE TABLE bank_customer (acc_no INT, name VARCHAR(255), balance float)")


insert
bankdetail = [
  (1001001, "Vidushi" ,1002.56 ),
  (1001002,  "Shreeyanka",50000.2),
  (1001003, "Ravi", 256.35),
  (1001004, "Hardik",100000.0),
  (1001005, "Avika",99956.56)
]
conn.executemany("INSERT INTO bank_customer VALUES (?,?, ?)", bankdetail)
conn.commit()
conn.close()


select
c = conn.execute('SELECT * FROM customer')
customers = c.fetchall()<----------------
for customer in customers:
    customer_id = customer[0]
    name = customer[1]
    phone_number = str(customer[2])
    email = customer[3]


delete
DELETE FROM table_name WHERE condition;


update
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")


join 2 tables based on something
SELECT * FROM table1 JOIN table2 ON table1.common_column = table2.common_column;


groupby
SELECT region, SUM(sales_amount) as total_sales
FROM sales
GROUP BY region;


find max
SELECT MAX(column_name) FROM table_name;


primary key
CREATE TABLE table_name (column1 datatype PRIMARY KEY, column2 datatype, ...);

not null
CREATE TABLE table_name (column1 datatype NOT NULL, column2 datatype, ...);


where
c = conn.execute('UPDATE student_records SET CGPA = ? WHERE student_id = ?', (new_cgpa, student_id))

complex
SELECT c.customer_name, c.customer_email, SUM(o.order_total) AS total_orders
FROM orders AS o
JOIN customers AS c ON o.customer_id = c.customer_id
WHERE o.order_date >= DATE('now', '-1 month')
GROUP BY c.customer_id;



python:
input
a = []
a.append(str(b))<----------------
a.reverse()
return "".join(a)
m = int(input("Enter the value of m: "))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union = set_a.union(set_b)
print("Union:", union)


print
print(”number is {m}”)
print(num1,"+",num2,"=", add(num1,num2))


array - insert delete
my_list = []
my_list.append(1)<----------------
my_list.insert(pos, 4)<----------------
my_list.remove(num)<----------------
my_list.pop(pos)<----------------


array of array
my_2d_list = []
new_row = [1, 2, 3]
my_2d_list.append(new_row)
my_2d_list.pop(listpos)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rows = len(matrix)
cols = len(matrix[0])
transposed = [[0 for j in range(rows)] for i in range(cols)]
def print_matrix(matrix):
    for row in matrix:
        print(row)


string - loop every character, substring
for char in string:
    reversed_string = char + reversed_string

num_str = str(num)

substring2 = my_string[0:5]


tab between print
print("First Name:\tJohn")

new line between print
print("First Name: John\nLast Name: Smith")


function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**(0.5))+1):<----------------
        if num % i == 0:
            return False
    return True

if-elseif
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")


while
while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1


loop using array, value, even numbers
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:<----------------
    print(fruit)

for num in range(m, n+1):
     if is_prime(num):
          print(num)

for i in range(10):
    if i == 5:
        break

for i in range(0, 10, 2):<----------------
    print(i)


regex
import re
pattern = r'^\d{10}$'<----------------
return bool(re.match(pattern, phone_number))

pattern = r"apple"
pattern = r"a.b"<----------------
pattern = r"[a-z][A-Z]"
pattern = r"a+"
pattern = r"colou?r"<----------------
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'<----------------
pattern = r'^\d{10}$'
pattern = r'^.{10}$'
match = re.search(pattern, text)<----------------
print(bool(match))  <----------------


ord('a')<----------------
chr(56)
reversed_string = string[::-1]<----------------
capitalized_string = my_string.capitalize()
titlecased_string = my_string.title()
decapitalized_string = string.lower()



Data base connection, insertion , display, update, add columns, sum up the columns, column wise sum, 2d display in 2 list, salary insertion, employee, 5% salary, total salary sum. alag se column print karna hai. displaying and adding up. 2d matrix list cheyali anta. (id name, age , salary, da salary(5%))