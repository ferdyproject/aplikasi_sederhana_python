class Kalkulator:
    def __init__(self):
        self.operations = {
            'tambah': lambda a, b: a + b,
            'kurang': lambda a, b: a - b,
            'kali': lambda a, b: a * b,
            'bagi': lambda a, b: a / b if b != 0 else 'Error: Pembagian dengan nol!'
        }

    def execute(self, operation, a, b):
        if operation in self.operations:
            return self.operations[operation](a, b)
        else:
            return 'Operasi tidak valid'

def main():
    kalkulator = Kalkulator()
    
    print("Selamat datang di Kalkulator Sederhana!")
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    operasi_map = {
        '1': 'tambah', 
        '2': 'kurang',
        '3': 'kali',
        '4': 'bagi'
    }

    operasi = input("Masukkan nomor operasi (1/2/3/4): ")
    if operasi in operasi_map:
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
            hasil = kalkulator.execute(operasi_map[operasi], num1, num2)
            print(f"Hasil: {hasil}")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    else:
        print("Operasi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
