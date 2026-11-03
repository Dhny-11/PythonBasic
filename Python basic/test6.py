import pdb 

def devide_num(a, b):
    #pdb.set_trace()
    result =a / b
    return result

print(devide_num(10,2))



try:
    number = int(0)
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
    
    

def bagi_angka(angka1, angka2):
    try:
        # Kode yang diuji
        print(f"Mencoba membagi {angka1} dengan {angka2}...")
        hasil = angka1 / angka2
        
    except ZeroDivisionError:
        # Menangani error pembagian dengan nol
        print("Peringatan: Tidak bisa membagi angka dengan nol!")
        
    except TypeError:
        # Menangani error tipe data (misal: string dibagi integer)
        print("Peringatan: Pastikan kedua input adalah angka!")
        
    else:
        # Hanya dieksekusi jika TIDAK ADA error di blok try
        print(f"Sukses! Hasil pembagian adalah: {hasil}")
        
    finally:
        # Selalu dieksekusi apapun yang terjadi
        print("Operasi matematika selesai.\n")

# Skenario 1: Berhasil (Memicu try, else, finally)
bagi_angka(10, 2)

# Skenario 2: Error dibagi nol (Memicu try, except ZeroDivisionError, finally)
bagi_angka(10, 0)

# Skenario 3: Error tipe data (Memicu try, except TypeError, finally)
bagi_angka(10, "B")


def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-1)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
    
    
print('\n')
    
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')
    



def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')