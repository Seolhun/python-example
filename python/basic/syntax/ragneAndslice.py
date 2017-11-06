# ######## #######
# Rage Test ######
# ######## #######

for i in range(5):
    print(i)
print("----------------")
# Two parameters
for i in range(3, 6):
    print(i)
print("----------------")
# Three parameters
for i in range(4, 10, 2):
    print(i)
print("----------------")
# Going backwards
for i in range(0, -10, -2):
    print(i)
print("----------------")

# ######## #######
# Slice Example ##
# ######## #######

x = range(100)
print(x)
print("----------------")
print(x[::2])
print(x)
print("----------------")
print(x[::3])
print(x)
print("----------------")
print(x[10:40:6])
print(x)
print("----------------")

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
# Bonus: Use indexing to revers the string
s[::-1]
