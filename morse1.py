import time 
import winsound 

diz_morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..', " ":" "
}



persona=input("scrivere frase o parola: ").upper() 

let_vuota=" "            #serve per il print dopo , qua dentro ad ogni occorenza metto il carattere 

for lettera in persona:
    if lettera not in diz_morse:
        pass
        print("Carattere non esistente ")
    else:
         carattere=diz_morse[lettera]   #sostanzialmente prendo i valori delle lettere che sono riuscite a passare (lo fa per una lettera alla volta )
         
         for simbolo in carattere:    # scorro ogni singolo elemento di carattere 
        
            if simbolo== ".":
                winsound.Beep(550, 200) #550 è la frequenza e 200 è la durata
                time.sleep(0.3)
                let_vuota+= simbolo

            else:
                if simbolo== "-":
                        winsound.Beep(600, 600)
                        time.sleep(0.3)
                        let_vuota+= simbolo 
                        
                else:
                    if simbolo ==" ":
                            time.sleep(2)
                            print("SPAZIO VUOTO")
                            let_vuota+= simbolo


print(let_vuota)
