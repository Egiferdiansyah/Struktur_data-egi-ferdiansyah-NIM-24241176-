#membuat pengecekkan password
#ketika yang di input kurang dari 8, = karakter kurang
##ketika yang di input sama/lebih dari 8, = karakter cukup

# Input password
password = input("Masukkan password: ")
if len(password) > 8:
    print("Karakter cukup");
else:
    print("Karakter kurang");