def compare_str (a, b):
	if a==b:
		return 1
	else:
		if len(a) > len(b):
			return 2
		elif b=="learn":
			return 3
	return 0


print (compare_str("local", "local"))
print (compare_str("local", "glob"))
print (compare_str("glob", "local"))
print (compare_str("local", "learn"))
print (compare_str("learn", "local"))