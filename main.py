def printnumber(n):
    iteration=0
    print ("The number entered by user is ",n)
    iteration+=1
    print ("Total iterations done by the code is ",iteration, "\n")
printnumber (10) 
printnumber (20)
print("\n With any 'n' the time taken by our code won't change")
def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print ("When n is ",n," Iterations = ",iteration)
OnTime (10)
OnTime (20)
OnTime (42)
print("\nWith every 'n' the time taken and iterations will increase")
