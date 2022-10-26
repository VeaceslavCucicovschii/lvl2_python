## HW1:
CLIENT TABLE:

| id (PK) |     fullName      |  vip  |         email          |
|---------+-------------------+-------+------------------------|
|    1    |   John Doe        | True  | JohnDoe@gmial.com      |
|    2    |   Marry Poppins   | False | MarryPoppins@gmial.com |
|    3    |   Harry Potter    | False | HarryPotter@gmial.com  |

| id (FK) |    phone (PK)     |
|---------+-------------------|
|    1    |  +373-604-23-132  |
|    1    |  +373-203-20-032  |
|    2    |  +373-794-20-132  |
|    3    |  +373-644-22-332  |


## HW2:
CLIENT_BAG TABLE:

| client_id (PK)  | total_cost  |
|-----------------+-------------|
|        1        |    850.00   |
|        2        |    900.00   |
|        3        |   1050.00   |

| product_id (PK) |  item_cost  |
|-----------------|-------------|
|      p-1        |    250.00   |
|      p-2        |    350.00   |
|      p-3        |    900.00   |

| client_id (FK)  | product_id (FK) | quantity |
|-----------------+-----------------+----------|
|        1        |      p-1        |    2     |
|        1        |      p-2        |    1     |
|        2        |      p-3        |    1     |
|        3        |      p-2        |    3     |
 
