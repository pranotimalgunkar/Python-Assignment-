#Q 1.Declare an int value and store it in a variable. Check the type and print the id of the same.
# Solution 1
a = 10 
print(a , type(a))
print(id(a))
# ans : <class 'int'>
#     140711090133720

# Q.2 Take one int value between 0 - 256.
#  Assign it to two different variables.Check the id of both the variables. It should come the same. Check why?
# Solution 2
a = 150
b = 150
print(id(a))   # Ans : 140711090138200
print(id(b))   #      140711090138200
print(a is b)  #True : id of a and b will be same because 0 - 256 is object reusability in python.



# Q3. Take one int value between 0 - 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come the same. Check why?

# Solution 3
a = 350
b = 350
print(id(a))
print(id(b)) 
print(a is b ) # False :id of a and b will be different because 0 - 256 is object reusability in python.

a = -6
b = -6
print(id(a))
print(id(b)) 
print(a is b ) # False :id of a and b will be different because 0 - 256 is object reusability in python.


# Q4. Arithmetic Operations on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
# Find sum of both numbers
# Find difference between them
# Find the product of both numbers.
# Find value after dividing first num with second number
# Find the remainder after dividing first number with second number
# Find the quotient after dividing first number with second number
# Find the result of the first num to the power of the second number.

# Solution 4
a = 12
b = 2
print(a+b) # 14
print(a-b) # 10
print(a*b) # 24
print(a/b) # 6.0
print(a//b) #6
print(a%b) #0
print(a**b) #144


# Q5. Comparison Operators on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
# Compare se two numbers with below operator:-
# Greater than, '>'
# Smaller than, '<'
# Greater than or equal to, '>='
# Less than or equal to, '<='
# Observe their output(return type should be boolean)

# Solution 5
a = 20
b = 15
print(a>b)  #True 
print(a<b)  #False 
print(a>=b) #True 
print(a<=b) #False


# Q6. Equality Operator
# Take two different integer values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)

# Solution 6
a = 20
b = 10
print(a==b) #False 
print(a!=b) # True


# Q7. Logical operators
# Observe the output of below code
# Cross check the output manually
# print ( 10 and 20 )
# #----------------------------------------->Output is 20
# print ( 0 and 20 )
# #----------------------------------------->Output is 0
# print ( 20 and 0 )
# #----------------------------------------->Output is 0
# print ( 0 and 0 )
# #----------------------------------------->Output is 0
# print ( 10 or 20 )
# #----------------------------------------->Output is 10
# print ( 0 or 20 )
# #----------------------------------------->Output is 20
# print ( 20 or 0 )
# #----------------------------------------->Output is 20
# print ( 0 or 0 )
# #----------------------------------------->Output is 0
# print ( not 10 )
# #----------------------------------------->Output is False
# print ( not 0 )
# #----------------------------------------->Output is True

# Solution 7
print ( 10 and 20 )
print ( 0 and 20 )
print ( 20 and 0 )
print ( 0 and 0 )
print ( 10 or 20 )
print ( 0 or 20 )
print ( 20 or 0 )
print ( 0 or 0 )
print ( not 10 )
print ( not 0 )


# Q8. Bitwise Operators
# Do below operations on the values provided below:-
# Bitwise and(&) -----------------------------------------> 10, 20
# -------> Output is 0
# Bitwise or(|) -----------------------------------------> 10, 20
# -------> Output is 30
# Bitwise(^) -----------------------------------------> 10, 20
# -------> Output is 30
# Bitwise negation(~) ------------------------------------> 10
# -------> Output is -11
# Bitwise left shift ------------------------------------> 10,2
# -------> Output is 40
# Bitwise right shift ------------------------------------> 10,2
# -------> Output is 2
# Cross check the output manually

# Slution 8
print(10&20)
print(10|20)
print(10^20)
print(~10)
print(10<<2)
print(10>>2)


# Q9. What is the output of expression inside print statement. Cross check
# before running the program.
# a = 10
# b = 10
# print(a is b) #True or False?
# print(a is not b) #True or False?
# a = 1000
# b = 1000
# print(a is b) #True or False?
# print(a is not b) #True or False?

# Solution 9
a = 10
b = 10
print(a is b) #True
print(a is not b) #False
a = 1000
b = 1000
print(a is b) #True
print(a is not b) #True


# Q10. What is the output of expression inside print statement. Cross check
# before running the program.
# print ( 10 +( 10 * 32 )// 2 ** 5 & 20 +(~( -10 ))<< 2 )

# Solution 10
print( 10 +( 10 * 32 )// 2 ** 5 & 20 +(~( -10 ))<< 2 ) 
# Ans : 20


# Q11. Membership operation
# in, not in are two membership operators and it returns boolean value
# print ( '2' in 'Python2.7.8' )
# print ( 10 in [ 10 , 10.20 , 10 + 20j , 'Python' ])
# print ( 10 in ( 10 , 10.20 , 10 + 20j , 'Python' ))
# print ( 2 in { 1 , 2 , 3 })
# print ( 3 in { 1 : 100 , 2 : 200 , 3 : 300 })
# print ( 10 in range ( 20 ))

# Solution 11
print ( '2' in 'Python2.7.8' )
print ( 10 in [ 10 , 10.20 , 10 + 20j , 'Python' ])
print ( 10 in ( 10 , 10.20 , 10 + 20j , 'Python' ))
print ( 2 in { 1 , 2 , 3 })
print ( 3 in { 1 : 100 , 2 : 200 , 3 : 300 })
print ( 10 in range ( 20 ))

# O/P :True
# True
# True
# True
# True
# True


# Q12. An integer can be represented in binary, octal or hexadecimal form.
# Declare one binary, one octal and one hexadecimal value and store them
# in three different variables.
# Convert 9876 to its binary, octal and hexadecimal equivalent and print
# their corresponding value.

# Solution 12
a = 200
b = 200
c = 200
x = print(bin(a))
y = print(oct(b))
z = print(hex(c))
d = 9876
print(bin(d))
print(oct(d))
print(hex(d))

#O/p :0b11001000
#0o310
#0xc8
#0b10011010010100
#0o23224
#0x2694


# Q13. What will be the output of following:-
# a = 0 b1010000
# print (a)
# b = 0 o7436
# print (b)
# c = 0x fade
# print (c)
# print ( bin ( 80 ))
# print ( oct ( 3870 ))
# print ( hex ( 64222 ))
# print ( bin ( 0 b1010000))
# print ( bin ( 0x fade ))
# print ( oct ( 0x fade ))
# print ( oct ( 0 o7436))
# print ( hex ( 0 b1010000))
# print ( hex ( 0x fade ))

# Solution 13
a = 0b1010000
print (a)
b = 0o7436
print (b)
c = 0xfade
print (c)
print ( bin ( 80 ))
print ( oct ( 3870 ))
print ( hex ( 64222 ))
print ( bin ( 0b1010000))
print ( bin ( 0xfade ))
print ( oct ( 0xfade ))
print ( oct ( 0o7436))
print ( hex ( 0b1010000))
print ( hex ( 0xfade ))
#O/p : 80
# 3870
# 64222
# 0b1010000
# 0o7436
# 0xfade
# 0b1010000
# 0b1111101011011110
# 0o175336
# 0o7436
# 0x50
# 0xfade