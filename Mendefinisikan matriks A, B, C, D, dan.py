# Fungsi untuk melakukan perkalian matriks
def perkalian_matriks(X, Y):
    baris_X = len(X)
    kolom_X = len(X[0])
    kolom_Y = len(Y[0])
    hasil = [[0 for _ in range(kolom_Y)] for _ in range(baris_X)]
    for i in range(baris_X):
        for j in range(kolom_Y):
            for k in range(kolom_X):
                hasil[i][j] += X[i][k] * Y[k][j]
    return hasil

# Fungsi untuk menambahkan dua matriks
def tambah_matriks(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk mengurangi dua matriks
def kurang_matriks(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk mencetak matriks dengan rapi
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:5}" for val in row))
    print()

# Matriks A dan modifikasinya untuk perkalian dengan D
A = [[3, 0], [-1, 2], [1, 1]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]
A_modifikasi = [row + [0] for row in A]

# Hitung hasil operasi tanpa pustaka NumPy
hasil_A_C_no_numpy = perkalian_matriks(A, C)
hasil_A_D_no_numpy = perkalian_matriks(A_modifikasi, D)
hasil_D_plus_E_no_numpy = tambah_matriks(D, E)
hasil_D_minus_E_no_numpy = kurang_matriks(D, E)

# Cetak hasil dengan rapi
print("Hasil A * C tanpa NumPy:")
print_matrix(hasil_A_C_no_numpy)

print("Hasil A * D (dengan modifikasi) tanpa NumPy:")
print_matrix(hasil_A_D_no_numpy)

print("Hasil D + E tanpa NumPy:")
print_matrix(hasil_D_plus_E_no_numpy)

print("Hasil D - E tanpa NumPy:")
print_matrix(hasil_D_minus_E_no_numpy)
