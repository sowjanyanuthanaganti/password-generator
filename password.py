import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
   'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','&','%','=','*','(',')']
n_letters=int(input("how many letters u want in ur password:\n"))
n_symbols=int(input("how many symbols u want in ur password:\n"))
n_digits=int(input("how many digits u want in ur password:\n"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,n_digits+1):
    char=random.choice(digits)
    password+=char    
print(password)

