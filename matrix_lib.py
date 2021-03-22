# macierz kwadratowa, to taka gdzie wysokość
# oraz wszystkie szerokości są takie same
def is_matrix_square(M):
    h = len(M)
    w = len(M[0])
    # sprawdź czy pierwszy wiersz i wysokość się zgadzają
    if (h != w): return False
    # sprawdź czy wszystkie wiersze mają tę samą szerokość
    for line in M:
        if (w != len(line)): return False
    # jak jest ok, to zwróc True
    return True


# Macierz dominująca to macierz, której wartości
# bezwzględne elementów na głównej przekątnej są
# większe od sumy wartości bezwzględnych
# pozostałych elementów w wierszach
def is_matrix_convergent(M):
    # dla każdej linii macierzy
    for i in range(len(M)):
        # policz sumę wartości bezwzględnych
        # z wyłączeniem wartości na przekątnej
        sum = 0
        for j in range(len(M[i])):
            if (i == j): continue
            sum += abs(M[i][j])
        # jeżeli ta suma jest większa lub równa
        # wartości bezwzględnej wartości na przekątnej
        # to macierz NIE jest zbieżna
        if (sum >= abs(M[i][i])):
            return False
    # jak przeszło, to macierz jest zbieżna
    return True