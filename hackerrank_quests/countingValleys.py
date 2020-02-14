n = 0
s = 'UDDDUDUU'

ls = [s[i] for i in range(len(s))]

att, level = 0, 0

for step in range(len(ls)):
	if ls[att:step+1].count('D') + ls[att:step+1].count('U') == 0:
		att = step
		if ls[att:step+1].count('D') > ls[att:step+1].count('U'):
			level += 1 

	# if att < 0:
	# 	level += 1
	# if level > 0 and att > 0:
	# 	att2 = 1
	# else:
	# 	att2 == 0
	# if att2 > 0 and att < 0:
	# 	level += 1
		

print(level)
