#DAVID BOYD
#CSC 500
#Project 2

#Below will calculate all the possible calculation for two int values

fst=float(input("Please enter an integer: "))

snd=float(input("Please enter an integer: "))

print(fst, "+", snd, "=", "{:,.2f}".format(fst+snd))
print(fst, "-" , snd, "=", "{:,.2f}".format(fst-snd))
print(fst, "*" , snd, "=",  "{:,.2f}".format(fst*snd))
print(fst, "/" , snd, "=", "{:,.2f}".format(fst/snd))
print(fst, "//" , snd, "=", "{:,.2f}".format(fst//snd))
print(fst, "%" , snd, "=",  "{:,.2f}".format(fst%snd))
print(fst, "**" , snd, "=", "{:,.2f}".format(fst**snd))

