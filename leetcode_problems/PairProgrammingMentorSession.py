# def prince(rose):
# 	def rose(rose):
# 		return lambda x: print(f'{x} {rose}')
# 	return rose('a thorn')

# def fox():
# 	print('in my side')

# def tame(f, g):
# 	return f(g())

# tame(prince, fox)('Antoine')
# print(4 + 5) + 2 - unsupported operand type(s) for +: 'NoneType' and 'int'

# print(3) or 1/0 - ZeroDivisionError: division by zero print3 returns none,
#which is falsey and moves onto 1/0 becaue of "or" and 1/0 cannot compute

# def return_or_print(option, x):
# 	if option == "print":
# 		print(x)
# 	elif option == "return":
# 		print(x)
# 		return x + 1

# print(return_or_print("return", 6))
# a = return_or_print("return", 6)

# return_or_print("print", return_or_print("return", 7 + 5))
# print 12
# print 13
# return None
# 6 or 3
# print(1, print(print(8), 6 or 3))


# prints 8
# prints None, 6
# prints 1 
# prints None

# What would Python output? #0
# a = 10
# b = 5
# n = 7

# def foo(x):
#     return lambda y: x(y)
# def cool(x):
#     return 3

# w = foo(cool)

# def cool(x):
# 	return x

# def quickMath(a, b):
# 	a = a + b
# 	b = 2 * b
# 	return a, b

# def swap(x, y):
#     temp = x
#     x = y
#     y = temp
#     return x, y
# What would Python output? #1
# def funny(joke):
#     hoax = joke + 1
#     return funny(hoax)

# def sad(joke):
#     hoax = joke - 1
#     return hoax + hoax
# funny, sad = sad, funny
# result = funny(sad(1))
# print(result)
# print(sad(1))
# print(funny(2))
# What would Python output? #2
# team = "warriors"
# games = 3

# def game(result):
#     games = 4
#     if result == "win":
#         return "hooray"
#     def noWinner(moreGames):
#             return games + moreGames
#     return noWinner

# def play(time):
#     team = "raptors"
#     lose = time()
#     def lost():
#         return 'lose'
#     if not lose(games):
#         return game("win")
#     else:
#         return lost()

# def match():
#     return game(team)
        
# result = play(match)
# print(print(result, result))

# Finish the definition such that the doctests are true.
# def sum_digits(n):
# 	""" Sum all the digits of n.

# 	>>> sum_digits(10) # 1 + 0 = 1
# 	1
# 	>>> sum_digits(2019) # 2 + 0 + 1+ 9 = 12
# 	12
# 	>>> x = sum_digits(123)
# 	>>> x
# 	6
# 	"""
# 	n = str(n)
# 	i = 0
# 	for num in n:
# 		num = int(num)
# 		i = i + num
# 	return i

# print(sum_digits(123))

# Define cond, true and false such that the follow doctests are true.
# def cond():
# 	return False
# def true():
# 	print('Tahoe')
# def false():
# 	print('Yosemite')
# def with_if_statement():
# 	""" 
#      >>> result = with_if_statement”
#      Yosemite
#      >>> print(result)
#      None
#     """
# 	if cond():
# 		return true()
# 	else:
# 		return false()

# result = with_if_statement()
# print(result)
# def with_if_function():
# 	"""
#      >>> result = with_if_statement”
#      Tahoe
#      Yosemite
#      >>> print(result)
#      None
#      """
# 	return (cond(), true(), false())

# result = with_if_function()
# print(result)