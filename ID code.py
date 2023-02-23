"""Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""
järjekord = 0
total = 0

while järjekord < 10 :
    
        järjekord += 1
        number_input = input(f"Sisesta {järjekord}. number (või tühik lõpetamiseks) :")
        if number_input == "":
            break
        number = int(number_input)
        total += number
print("numbrite summa on:" ,total )