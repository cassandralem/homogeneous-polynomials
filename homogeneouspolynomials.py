
print("This code generates the basis monomials of the spaces of 2 and 3-dimensional homogeneous polynomials of arbitrary degree.")

# dimension = int(input("Enter the dimension: "))
degree = int(input("Enter the degree of the polynomials: "))

#------------------------------------------------------------------------------

if degree == 2:
    
    for a in range(degree + 1):
        
        if a == degree:
            monomial = "a^" + str(a) + "b^0"
            print(monomial)
            break

        b = degree - a
        
        monomial = "a^" + str(a) + "b^" + str(b)
        print(monomial)

#------------------------------------------------------------------------------

if degree == 3:

    for a in range(degree + 1):
        
        if a == degree:
            monomial = "a^" + str(a) + "b^0c^0"
            print(monomial)
            break
        
        for b in range(degree + 1):
            
            if a+b > degree:
                continue
            
            c = degree - a - b
            
            if c < 0:
                c = 0
            
            monomial = "a^" + str(a) + "b^" + str(b) + "c^" + str(c)
            print(monomial)