n1=float(input("1ere note /20 ?"))
n2=float(input("2e note /20 ?"))
n3=float(input("3e note /20 ?"))

if n1>20:
    while n1>20:
        n1=float(input("1ere note > 20 recommence "))
if n2>20:
    while n2>20:
        n2=float(input("2e note > 20 recommence "))
if n3>20:
    while n3>20:
        n3=float(input("3e note > 20 recommence "))

moy=(n1+n2+n3)/3

if moy<10:
    print(f"tu as {moy} et c'est insufisant")
elif moy>=10 and moy<14:
    print(f"tu as {moy} et c'est correct")
elif moy>=14:
    print(f"tu as {moy} et c'est très bien")