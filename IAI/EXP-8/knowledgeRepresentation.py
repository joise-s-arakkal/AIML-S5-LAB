def measles(a, b, c, d, e):
	if a == 'y' and b == 'y' and c == 'y' and d == 'y' and e == 'y':
		return "measles"
	else:
		return None

def flu(a, b, c, d, e, f, g, h):
	if a == 'y' and b == 'y' and c == 'y' and d == 'y' and e == 'y' and f == 'y' and g == 'y' and h =='y':
		return "flu"
	else:
		return None

def cold(c, j, k, d, h):
	if c == 'y' and j == 'y' and k == 'y' and d == 'y' and h == 'y':
		return "cold"
	else:
		return None

def chickenpox(a, h, g, b):
	if a == 'y' and h == 'y' and g == 'y' and b == 'y':
		return "chickenpox"
	else:
		return None

def run_diagnosis():
	name = input("Please enter your name: ")
	a = input("Do you have fever? (y/n): ").lower()
	b = input("Do you have rashes? (y/n): ").lower()
	c = input("Do you have headache? (y/n): ").lower()
	d = input("Do you have running nose? (y/n): ").lower()
	e = input("Do you have conjunctivitis? (y/n): ").lower()
	f = input("Do you have cough? (y/n): ").lower()
	g = input("Do you have ache? (y/n): ").lower()
	h = input("Do you have chills? (y/n): ").lower()
	i = input("Do you have swollen glands? (y/n): ").lower()
	j = input("Do you have sneezing? (y/n): ").lower()
	k = input("Do you have sore throat? (y/n): ").lower()

	diagnosis = []

	result = measles(a, f, e, d, b)
	if result:
		diagnosis.append(result)

	result = flu(a, c, g, e, h, k, f, d)
	if result:
		diagnosis.append(result)

	result = cold(c, j, k, d, h)
	if result:
		diagnosis.append(result)

	result = chickenpox(a, h, g, b)
	if result:
		diagnosis.append(result)

	if len(diagnosis) > 0:
		print(f"{name}, based on the symptoms provided, you may have: {', '.join(diagnosis)}.")
	else:
		print("No diagnosis could be made based on the given symptoms.")

run_diagnosis()
