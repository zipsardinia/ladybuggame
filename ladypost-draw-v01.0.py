import random
import csv
import time


prize = float(input ("Prize - SBD "))
jackpot = float(input ("Jackpot - SBD "))


with open('lp04018.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    dates = []
    for row in readCSV:
        date = row[0]
        dates.append(date)
print ()
print (str("Prize Pool | Montepremi: ") + str(prize) + str(" SBD"))
print ()
print ("These are the winners | I vincitori sono:")
prize1 = round(prize * 0.50,3)
prize2 = round(prize * 0.25,3)
prize3 = round(prize * 0.15,3)
jackpot = jackpot + round(prize * 0.10,3)

premi = [prize1,prize2,prize3]

x=1
while x <= 3:
    l = []
    while len(l) < 3:
        numero = random.randint(1,len(dates))
        if numero not in l:
            l.append(numero)
            p=x
            print 
            print (str(x) + (". Lucky Number N.") + str((numero)), ("@") + (dates[numero-1]) , str(premi[p-1]))
            x=x+1

print (str("Jackpot - ") + str(jackpot))
print ()
print ("DRAW TIME:", (time.strftime("%d/%m/%Y")) , (time.strftime("%H:%M:%S")))
