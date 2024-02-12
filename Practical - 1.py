principle = int(input("Enter Principal Amount : ")) 
roi = 5.4
time = int(input("Enter Time Period : "))
si = principle*roi*time/100
print("Simple Interest : ",si)
ci = principle*((1 + (roi/100))**time)
print("Compound Interest : ",ci-principle)