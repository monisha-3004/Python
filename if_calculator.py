def calculator(operation,n1,n2):
    if operation=='add':
        print(n1+n2)
    elif operation=='subtract':
        print(n1-n2)
    elif operation=='multiply':
        print(n1*n2)
    elif operation=='divide':
        print(n1/n2)
    else:
        print("Invalid operation")
  
operation=input('>')      
n1=int(input('>'))
n2=int(input('>'))
calculator(operation,n1,n2)
