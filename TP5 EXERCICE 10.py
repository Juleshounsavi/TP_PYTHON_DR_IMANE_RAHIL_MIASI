
def moyenne_ponderee(notes, coefficients):
    somme = 0
    for i in range(len(notes)):
        somme = somme + notes[i] * coefficients[i]
    moy = somme / sum(coefficients)
    return moy

moyenne_ponderee([15, 12, 18], [2, 1, 3])

