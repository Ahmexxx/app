def p_a_rettangolo(a:int, b:int):
    '''questa funzione calcola il perimetro e l'area di un rettangolo'''
    print('funzione perimetro e area di un rettangolo:')
    p_rettangolo = a + b
    a_rettangolo = a * b
    print('''il perimetro del rettangolo è '''+str(p_rettangolo),''', invece l'area è '''+str(a_rettangolo))
    return p_rettangolo, a_rettangolo

# x = int(input('inserisci lunghezza lato minore'))
# y = int(input('inserisci lunghezza lato maggiore'))
# perimetro_r, area_r = p_a_rettangolo(a,b)
# print(perimetro_r, area_r)
