
parola=input("scrivere la parola: ")
output=" "
def rovescio(parola,output):
    if len(parola) == 0:
        return output
    return rovescio(parola[:-1],output + parola[-1] ) #prende l'ultimo elemento della stringa iniziale e poi lo vado a sommare alla stringa output 
print(rovescio(parola,output))