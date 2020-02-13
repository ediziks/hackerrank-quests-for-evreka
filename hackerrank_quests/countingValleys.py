n = 0
s = 'DUUDDUUDDUUDDUUDD'

ls = [s[i] for i in range(len(s))]

att, att2, level = 0, 0, 0

for step in ls:
	if step == 'U':
		att += 1
	elif step == 'D':
		att -= 1
	if att < 0:
		level = 1
	if level > 0 and att > 0:
		att2 = 1
	if att2 == 1 and att < 0:
		level += 1
		

print(level)
