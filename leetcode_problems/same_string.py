def same_strings(s, t):
	if s == t:
		return True
	s = list(s)
	t = list(t)
	for index, letter in enumerate(s):
		if letter == "#":
			s = s.pop(index-1)

	for index, letter in enumerate(t):
		if letter == "#":
			t = t.pop(index-1)
	if s == t:
		return True
	else:
		return False

s = "ab#c"
t = "ad#c"

print(same_strings(s,t))
