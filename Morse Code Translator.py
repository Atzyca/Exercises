alphabet = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---",
            "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-",
            "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
m_alphabet = {v:k for k,v in alphabet.items()}
def text_to_morse(text):
    morse = []
    for symbol in text.lower():
        if symbol in alphabet:
            morse.append(alphabet[symbol])
        else:
            morse.append("X")
    return " ".join(morse)
            

print ("Tere")

    
while True:
    message = input("Sisesta oma sõnum, mida morse koodi teisendada: ")
    if message == "":
        break
    print(text_to_morse(message))
    print("Sisesta kontrolliks morse kood: ")
    print(morse_to_text(input()))
def morse_to_text(morse):
    message = []
    morse_list = morse.split(" ")
    for character in morse_list:
        if character in m_alphabet:
            mesasge.append(m_alphabet[character])
        else:
            message.append(" ")
    return " ".join(message)
        
        
    