print("******PREPOSITIONAL LOGIC INFERENCES FOR AI TASKS********")
def negation(p):
	return not p
print("\u0332".join("NEGATION"))
print("p result")
for p in [True, False]:
	a = negation(p)
	print(p, a)

def conjunction(p, q):
	return p and q
print("\u0332".join("CONJUCTION(AND OPERATION)"))
print("p q result")

for p in [True, False]:
	for q in [True, False]:
		a = conjunction(p, q)
		print(p, q, a)

def disjunction(p, q):
	return p or q
print("\u0332".join("DISJUNCTION(OR OPERATION)"))
print("p q result")
for p in [True, False]:
	for q in [True, False]:
		a = disjunction(p, q)
		print(p, q, a)

def exclusive_disjunction(p, q):
	return (p and not q) or (not p and q)
print("\u0332".join("EXCLUSIVE DISJUNCTION(XOR OPERATION)"))
print("p q result")
for p in [True, False]:
	for q in [True, False]:
		a = exclusive_disjunction(p, q)
		print(p, q, a)

def implication(p, q):
	return not p or q
print("\u0332".join("IMPLICATION"))
print("p q result")
for p in [True, False]:
	for q in [True, False]:
		a = not(p) or q
		print(p, q, a)
