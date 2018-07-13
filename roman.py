n=input()
k=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX"]
for i in range(0,20):
	if n in k[i]:
		chk=i+1
		break
print(chk)
