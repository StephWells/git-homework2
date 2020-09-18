#Solutions
#Solution 1

#practicing f-string for headers
#practicing right adjust to right align numbers
print(f"{'Number':>20}{'Square':>20}{'cube':>20}")
for x in range (0,6):
   print(repr(x).rjust(20), repr(x*x).rjust(20), end= ' ')
   print(repr(x*x*x).rjust(20))
    

#Solution 2


