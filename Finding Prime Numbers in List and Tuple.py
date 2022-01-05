Numbers=[2,3,12,14,19,9,15,19,7,11,21,13,23,25,31,33]   # Random Numbers
prime=[]    # Empty List for Prime Numbers
Notprime=[] # Empty List for Non Prime Numbers
for i in Numbers:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        prime.append(i)     # Inserting Numbers to Empty Prime List
    else:
        Notprime.append(i)  # Inserting Numbers to Enpty NotPrime List
# Formated Strings
print(f"Prime Numbers are  : {prime}")
print(f"Not Prime numbers are  : {Notprime}")
# We can also Use tuple instead of list It will also works
# But the Prime and Not Prime variables must be in the list
