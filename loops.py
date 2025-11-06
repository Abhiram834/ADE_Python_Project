# loops in python

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# 1. for loop
# 2. while loop

# for i in range(start, stop, step=1)
  
# for i in range(1, 11, 3):
#     print(i)

# when to use for loop : when we know about end point then for loop is used
 

# for j in range(21,31,1):
#     print(j)

# if you don't know the end point in that case while loop will used. 
# ex: api will continuesly keep on requesting their know end for that.

# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1

# k=20
# while k >10:
#     print(k)
#     k = k-1


# strings, lists, set, tuple, dict

name = "python"
# for i in name:
#     print(i)

# fruits = ["apple", "banana", "mango"]
# # for fruit in fruits:
# #     print(fruit)
    
# stu_info = {
#     "name": "Sandeep",
#     "age": 29,
#     "course": "M.sc"
# }

# for stu in stu_info:
#     print(stu)

# for key, value in stu_info.items():
#     print(value)
    

name = input("Enter the name: ")
# print(type(name))

# count the noOf vowels in the name variable
# [a, e, i, o, u]
vowels = ['a', 'e', 'i', 'o', 'u']
# vowels2 = ['A', 'E', 'I', 'O', 'U']
# count=0
# for ch in name:
#     if ch in vowels1:
#         count=count+1
#     elif ch in vowels2:
#         count=count+1
# print(count)

cnt = 0
special_chars = ['!', '@', '#', '$', '%']

char_cnt = 0
for i in name:
    if i in special_chars:
        char_cnt = char_cnt+1
        
# conditional operators
if name.isnumeric():
    print("You have entered a numeric value. Pls enter a string!")
    
elif char_cnt > 0:
    print("Entered string contains special chars!!")

else:
    for ch in name.lower():
        if ch in vowels:
            cnt = cnt + 1
    print(cnt)
        


# if condition:
#     code
# elif condition2:
#     code
# elif condition3:
#     code
# else:
#     code