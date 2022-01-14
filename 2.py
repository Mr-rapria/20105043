std_ded = 10000
add_ded = 3000

gross_income = int(input("Enter the Gross Income : "))
num_dep = int(input("Enter number of Dependents : "))

taxable_income = gross_income - std_ded - (add_ded*num_dep)

tax = 0

if(taxable_income>0):
    tax = taxable_income*20/100

print("Tax : %0.2f" %tax)
