# ######## #######
# Lambda Example ##
# ######## #######

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print under 5 from 0 ~ 9
print(list(filter(lambda x: x < 5, range(10))))

# print even number from 0~50
print(list(filter(lambda x: x % 2 == 0, range(51))))

# print odd number from 0~50
print(list(filter(lambda x: x % 2 != 0, range(51))))
