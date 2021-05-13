def SetAnnual():
  global annual
  annual=12000

# Here below the Local value gets calculated and then printed - If I remove annual = 24000 the Global value gets calculated and then printed 
def PrintMonthly():
    annual=24000
    print("Your monthly payment is "+str(annual/12)+" USD.")
SetAnnual()
PrintMonthly()

# Here below the Global value gets calculated and then printed
print("No Function - Your monthly payment is "+str(annual/12)+" USD.")