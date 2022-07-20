
def lgst_common_subtring(X,Y):

    #       zerowanie tablicy
    # x - wiersze   y - kolumny
    tab = [[0 for y in range(len(Y)+1)] for x in range(len(X)+1)]


    for x in range(len(X)):
        row_before = tab[x]
        row_now = tab[x+1]
        x_letter = X[x]

        for y in range(len(Y)):
            y_letter = Y[y]
            if x_letter == y_letter:
                # z lewo-gora +1
                row_now[y+1]=row_before[y]+1
                continue
                # albo wiekszy lewo / gora
            row_now[y+1] = max(row_now[y], row_before[y+1])

    x = len(X)
    y = len(Y)

    # czytanie tablicy od prawego dolnego rogu
    substring = []
    while x>0 and y>0:
        x_letter = X[x-1]
        y_letter = Y[y - 1]

        if x_letter == y_letter:
            x -= 1
            y -= 1
            substring.append(x_letter)
            continue
        if tab[x-1][y] > tab[x][y-1]:
            x-=1
            continue
        y-=1


    # wypisanie tablicy
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in tab]))

    print("\n")
    print("X = ",X, "     Y = ",Y)
    lgst = "".join([str(x) for x in substring[::-1]])
    print("Longest common subsequence: ",lgst)


    x= all_lgst(X,Y,len(X),len(Y),tab)
    print("All longest common subsequences ",x)
    print("Unique longest common subsequences ",set(x),"\n")



def all_lgst(X, Y, lx, ly, tab):
    # czy doszlismy do konca ktoregos stringa
    if lx == 0 or ly == 0:
        return [""]

    # jesli ostatni znak w X i Y jest taki sam
    if X[lx - 1] == Y[ly - 1]:
        # szukaj pomijajac ostatni znak
        lcs = all_lgst(X, Y, lx - 1, ly - 1, tab)
        # dodaj go do wyniku
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (X[lx - 1])
        return lcs

    # Ostatni znak w X i Y jest inny
#jesli gorna kom   > lewa komorka  to pomin akatualny znak w X i wywolaj f dla lx-2 i ly-1
    if tab[lx - 1][ly] > tab[lx][ly - 1]:
        return all_lgst(X, Y, lx - 1, ly, tab)

#jesli lewa kom   >  gorna komorka  to pomin akatualny znak w X i wywolaj f dla lx-1 i ly-2
    if tab[lx][ly - 1] > tab[lx - 1][ly]:
        return all_lgst(X, Y, lx, ly - 1, tab)

    # jesli wartosc komorki z gory jest rowna wartosci komorki z lewej to rozwazamy obie opcje
    upper = all_lgst(X, Y, lx - 1, ly, tab)
    left = all_lgst(X, Y, lx, ly - 1, tab)

    # dodaj obie listy
    return upper + left



if __name__ == '__main__':
    X = "NRIUEGNWEIVNADIU"
    Y = "WEIOGPEUNDU"

    lgst_common_subtring(X,Y)

    X = "XXXYYYZZ"
    Y = "XYZXY"
    lgst_common_subtring(X, Y)

    X = "abbaac"
    Y = "bacbacba"
    lgst_common_subtring(X, Y)







