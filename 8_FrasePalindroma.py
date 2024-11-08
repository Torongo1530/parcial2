def verificacionPalindromo(frase):
    palabraAlreves = frase[::-1]
    if frase == palabraAlreves:
        print(f"La frase {frase} es palindroma")
    else:
        print(f"La frase {frase} NO es palindroma")

verificacionPalindromo("reconocer")
verificacionPalindromo("caminar")