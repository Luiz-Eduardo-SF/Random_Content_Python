#name = str(input('Qual o seu nome? ')).upper() # Take the name and put everything in upperCase
#silv = name.find('SILVA') # find "Silva" and return de value of the first letter
#print(f'O nome tem silva?: {name[silv:(silv+5)] == 'SILVA'}') # take the first letter and comput if the hole word is iquals to "SILVA"

# or 

name = str(input('Whats your name?: ')).upper()
print(f'Your name have "Silva"?: {'SILVA' in  name}')