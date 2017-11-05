print('---------------------------------')
s = 'django'
# 'd'
s[0]
# 'o'
s[5]
# 'djan'
s[:4]
# 'go'
s[4:]
#Bonus: Use indexing to revers the string
s[::-1]

print('---------------------------------')
# Given this nested list:
l = [3, 7, [1,4, 'hello']]
print(l)
#Reassign "hello" to be "goodbye"
l[2][2] = 'goodbye'
print(l)

print('---------------------------------')
d1 = {'simple_key': 'hello'}
print(d1['simple_key'])
d2 = {'k1':['k2', 'hello']}
print(d2['k1'][1])
d3 = {'k1':[{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

print('---------------------------------')
my_list = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,34,4,4,4,4,5,5,5,5]
my_list = set(my_list)
print(my_list)

print('---------------------------------')
age = 4
name = 'Sammy'
print("hello my dog's name is {a} and he is {b} years old.".format(a=age, b=name))