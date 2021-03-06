def same_strings(s, t):
	if s == t:
		return True
	s = list(s)
	t = list(t)
	for index, letter in enumerate(s):
		if letter == "#":
			s.pop(index-1)
			s.pop(index-1)

	for index, letter in enumerate(t):
		if letter == "#":
			t.pop(index-1)
			t.pop(index-1)

	if s == t:
		return True
	else:
		return False

s = "ab#c"
t = "ad#c"
a = 'ab##'
b = 'c#d#'
c = 'a##c'
d = '#a#c'
e = 'a#c'
f = 'b'

print(same_strings(s,t))

print(same_strings(a,b))

print(same_strings(c,d))

print(same_strings(e,f))


def same_strings_stack(s, t):
	s_list = []
	t_list = []
	for letter in s:
		if letter != "#":
			s_list.append(letter)
		elif len(s_list) == 0:
			continue
		else:
			s_list.pop()

	for letter in t:
		if letter != "#":
			t_list.append(letter)
		elif len(t_list) == 0:
			continue
		else:
			t_list.pop()

	if s_list == t_list:
		return True
	else:
		return False

s = "ab#c"
t = "ad#c"
a = 'ab##'
b = 'c#d#'
c = 'a##c'
d = '#a#c'
e = 'a#c'
f = 'b'

print(same_strings_stack(s,t))

print(same_strings_stack(a,b))

print(same_strings_stack(c,d))

print(same_strings_stack(e,f))
