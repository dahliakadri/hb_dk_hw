a = 25
b = 10
c = 5
d = 1

def coin_machine(cents):
#Given a certain amount of money of $.87 return quarters dimes nickles and pennies that amount to that.
#return optimal solution with least number of coins

#cents / % a = 0 then w = cents/ a

	if cents % a == 0:
		w = (cents / a)
		x , y , z = 0, 0 , 0
	else:
		w = (cents // a)
		cents = cents - (w*a)
		if cents % b  == 0:
			x = (cents / b)
			y, z = 0, 0
#TODO while loop and recursion
#email or phone 
#and recursion 

#else  take remainder of w and check % b


	return w, "quarters", x, "dimes", y, "nickles", z , "pennies"

print(coin_machine(85))