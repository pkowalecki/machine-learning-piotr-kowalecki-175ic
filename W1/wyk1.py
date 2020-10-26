import numpy as np;


#utwórz tablicę zawierającą 10 zer
zeros_array = np.zeros(10)
print("Zeros: \n", zeros_array, "\n")


#utwórz tablicę zawierającą 10 piątek
fives_array = np.ones(10)*5
print("Fives: \n", fives_array, "\n")


#utwórz tablicę zawierającą liczby od 10 do 50
values = np.arange(10,51,1)
print("Values: \n", values, "\n")


#utwórz macierz o wymiarach 3x3 zawierającą liczby od 0 do 8
matrix = np.arange(0,9,1).reshape(3,3)
print("3x3 matrix: \n", matrix, "\n")


#utwórz macierz jednostkową o wymiarach 3x3
identity_matrix = np.identity(3)
print("3x3 identity matrix: \n", identity_matrix, "\n")


#utwórz macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa),
gauss_distribution = np.random.normal(size=(5,5))
print("Gauss distribution: \n", gauss_distribution, "\n")


#utwórz macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01
matrix_small_step = np.arange(0.01,1.01,0.01).reshape(10,10)
print("From 0.01 to 1: \n", matrix_small_step, "\n")


#utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1)
linear_distribute = np.linspace(0,1,20)
print("Linear distribution: \n", linear_distribute, "\n")


#utwórz tablicę zawierającą losowe liczby z przedziału (1, 25),
#następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami
#oblicz sumę wszystkich liczb w ww. macierzy,
#oblicz średnią wszystkich liczb w ww. macierzy,
#oblicz standardową dewiację dla liczb w ww. macierzy,
#oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy.
random_numbers = np.random.randint(1, 26, 25)
print("Random numbers: \n", random_numbers, "\n")
random_numbers = random_numbers.reshape(5,5)
print("Random numbers but in matrix: \n", random_numbers, "\n")
print("Sum of numbers: \n", random_numbers.sum(), "\n")
print("Mean of numbers: \n", random_numbers.mean(), "\n")
print("Deviation of numbers: \n", random_numbers.std(), "\n") 
print("Sum of columns: \n", random_numbers.sum(axis=0), "\n")


#utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) i:
#oblicz medianę tych liczb,
#znajdź najmniejszą liczbę tej macierzy,
#znajdź największą liczbę tej macierzy.
random_numbers_5x5 = np.random.randint(1, 101, (5, 5))
print(random_numbers_5x5)
print("Median of numbers: \n", np.median(random_numbers_5x5), "\n") 
print("Min value: \n", np.min(random_numbers_5x5), "\n") 
print("Max value: \n", np.max(random_numbers_5x5), "\n") 


#utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji,
diff_matrix = np.random.randint(0, 101,(3,2))
print("Diff matrix: \n", diff_matrix, "\n")
print("Transposition: \n", diff_matrix.transpose(), "\n")


#utwórz dwie macierze o odpowiednich wymiarach (doczytać), większych od 2 i dodaj je do siebie,
matrix_M = np.random.randint(2, 11)
matrix_N = np.random.randint(2, 11)
matrix_A = np.random.randint(0, 100, (matrix_M, matrix_N))
print("Matrix A: \n", matrix_A, "\n")
matrix_B = np.random.randint(0, 100, (matrix_M, matrix_N))
print("Matrix B: \n", matrix_B, "\n")
print("Sum of matrixes: \n", matrix_A + matrix_B, "\n")


#utwórz dwie macierze o odpowiednich wymiarach (doczytać) różnych od siebie i większych od 2,
#a następnie pomnóż je przez siebie za pomocą dwóch różnych funkcji (np. ‘matmul’ i ‘multiply’)
#Warunek mnożenia macierzy: Matrix_A[M x N] * Matrix_B[N x P] = Matrix_C[M x P]
matrix_M_multiply = np.random.randint(2, 5)
matrix_N_multiply = np.random.randint(2, 5)
matrix_A_multiply = np.random.randint(0, 100, (matrix_M_multiply, matrix_N_multiply)).transpose()
print("Matrix A: \n", matrix_A_multiply, "\n")
matrix_B_multiply = np.random.randint(0, 100, (matrix_M_multiply, matrix_N_multiply))
print("Matrix B: \n", matrix_B_multiply, "\n")
print("Matmul of matrixes: \n", np.matmul(matrix_A_multiply, matrix_B_multiply), "\n")