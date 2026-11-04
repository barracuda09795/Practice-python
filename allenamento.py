import os 
import json

nome="goku.json"
ai="if i dont do it who will" 
if not os.path.exists(nome):  # dice se il file di nome goku esiste se non esiste fa questo 
    
    
    with open(nome,"w",encoding="utf-8")as file_creazione:           #con questo creo il file in questione 
        json.dump(ai,file_creazione)            #dico che il contenuto di ai va in nome 
        print("non esiste creo subito il file")
else:
    print("file esiste gia")
    chiedere=input("vuoi modificarlo,rispondere con si o no: ")
    if chiedere == "si":
        ai2=input("scrivere cio che si vuole aggiungere: ")

        ai3=ai+ " " +ai2                                        # lo faccio per unire le stringhe 

        with open(nome,"w",encoding="utf-8")as file_creazione:    #faccio questo per poter modificare il file        
                json.dump(ai3,file_creazione,indent= 1)  

        with open(nome,"r",encoding="utf-8")as file:    
                json.load(file)

    if chiedere == "no":
        print("ok")
        






with open(nome,"r",encoding="utf-8")as file:    #sostanzialmente vado a leggere il file 
    json.load(file)






    
