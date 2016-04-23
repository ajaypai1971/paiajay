# interview questions from https://www.codementor.io/python/tutorial/essential-python-interview-questions

#**************
#  def foo(i, x=[]):
#     x.append(x.append(i))
#     return x
#
#
# for i in range(3):
#     y = foo(i)
#     print(y)
# print(y)
#**************
#http://stackoverflow.com/questions/36682910/none-value-appended-in-the-list-output?noredirect=1#comment60956231_36682910

# #**************
# def add(num, x=[]):
#     x.append(num)
#     print(x)
#
# add(4)
# add(5)
#************

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)
#***************************************************************


#list comprehensions
#*********************************
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
#*********************************



# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)

#interview question from https://techmyway.wordpress.com/2011/06/17/python-interview-questions/

# Iterate over a list of words and use a dictionary to keep track of the frequency(count) of each word. for example
# {‘one’:2, ‘two’:2, ‘three’:2}

#variable swap
# a,b = 1,2
# print(a)
# print(b)
#
# a,b = b,a
# print(a)
# print(b)

#*****************
## fizbuzz problem: my implementation
# def fizbuz(num):
#     fizbuzz = []
#     for x in range(1,num+1):
#
#         if x%3 == 0 and x%5 ==0:
#             fizbuzz.append("fb")
#         elif x%5 == 0:
#             fizbuzz.append("b")
#
#         elif x%3 == 0:
#             fizbuzz.append("f")
#         else:
#             fizbuzz.append(x)
#     return(fizbuzz)
#
# num =100
# res = fizbuz(num)
# print(res)
#
# #in one line,, the most pythonic way:
# print(["FizzBuzz" if x%5 == 0 and x%3 == 0 else "Fizz" if x%3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(1,101)])
#*****************

#*****************
# list comprehensions http://stackoverflow.com/questions/36743765/list-comprehension-fill-arbitrary-value-if-list-is-empty

# values = [1.4,1.5,1.6,1.8]
# indices = [0,1]
# newvalues = [values[i] for i in indices] if indices else [-1]
# print(newvalues)

