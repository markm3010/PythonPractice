
# casing ID
id = float(input("casing ID: "))

# constant
C = float(input("constant: "))

# calx
cx = float(input("calx value: "))

# CCF calculated
ccf = (id-C)/(cx-C)
print("CCF=%.3f" % ccf )
