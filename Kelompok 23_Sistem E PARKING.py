import winsound
import time
from time import sleep


print("==========================================================")
print()
print('E-PARKING')


# FUNGSI PEMBATAS
def space():
    print()
    print("==========================================================");
    sleep(1)
    print()

    
# LOADING
def wait():
    print("[MOHON TUNGGU SEBENTAR]");
    sleep(0.25)
    print(".", end=" ");
    sleep(0.25)
    print(".", end=" ");
    sleep(0.25)
    print(".");
    sleep(0.25)
    print()

    
# PENGATURAN AWAL PARKING SYSTEM
slot_motor = 20
slot_mobil = 30
jam1_motor = 3600
biaya1_motor = 2000
jam2_motor = 3600
biaya2_motor = 3000
jam1_mobil = 3600
biaya1_mobil = 5000
jam2_mobil = 3600
biaya2_mobil = 7000
space()


# MENUNJUKKAN KETERSEDIAAN SLOT PARKIR
def slot_parkir(motor_count, mobil_count):
    print("[SLOT PARKIR TERSEDIA]")
    print("Mobil =", mobil_count)
    print("Motor =", motor_count)

# MENGHITUNG JUMLAH SLOT PARKIR YANG KOSONG
def count_motor(x):
    motor_count = 0
    for i in range(slot_motor):
        motor_count = motor_count + x[i]
    return motor_count


def count_mobil(y):
    mobil_count = 0
    for i in range(slot_mobil):
        mobil_count = mobil_count + y[i]
    return mobil_count


# KALKULASI HARGA
def perhitungan_motor(durasi):
    harga = 0
    harga1 = 0
    total = 0
    if durasi >= jam1_motor:
        harga1 = harga + biaya1_motor
        durasi = durasi - jam1_motor
        if durasi < 0:
            durasi = 0
        if durasi % jam2_motor > 0:
            durasi = durasi + jam2_motor
        harga = (durasi // jam2_motor) * biaya2_motor
        total = harga1 + harga
    elif durasi < jam1_motor:
        total = biaya1_motor
    return total




def perhitungan_mobil(durasi):
    harga = 0
    harga1 = 0
    if durasi >= jam1_mobil:
        harga1 = harga + biaya1_mobil
        durasi = durasi - jam1_mobil
        if durasi < 0:
            durasi = 0
        elif durasi % jam2_mobil > 0:
            durasi = durasi + jam2_mobil
        harga = (durasi // jam2_mobil) * biaya1_mobil
        total = harga1 + harga
    elif durasi < jam1_mobil:
        total = biaya1_mobil
    return total

# DEKLARASI VARIABEL
motor = [1 for i in range(slot_motor)]
mobil = [1 for j in range(slot_mobil)]
start_motor = [0 for i in range(slot_motor)]
start_mobil = [0 for i in range(slot_mobil)]


# PROGRAM UTAMA
loop = 0
while (loop < 1):
    sistem = int(input("Tekan 1 untuk masuk atau 2 untuk keluar. \n"))
    space()
    wait()
    print()
    if sistem == 1:
        motor_count = count_motor(motor)
        mobil_count = count_mobil(mobil)
        slot_parkir(motor_count, mobil_count)
        print()
        print("[SELAMAT DATANG]")
        winsound.PlaySound("selamat datang.wav", winsound.SND_ASYNC)
        jenis = int(input("Tekan 1 untuk motor atau 2 untuk mobil. \n"))
        space()

        if jenis == 1 and motor_count != 0:
            bantuan = int(input("Silahkan tekan 1 untuk cetak karcis atau 2 untuk bantuan. \n"))
            if bantuan == 1:
                check = 0
                while check < slot_motor:
                    if motor[check] == 1:
                        slot = check
                        check = 999
                    check = check + 1
                motor[slot] = motor[slot] - 1
                print("[TERIMAKASIH]\nAnda parkir pada slot", str(slot + 1))
                space()
                start_motor[slot] = time.time()

            else:
                print("Menghubungi Operator...")
                space()
                
    elif jenis == 2 and mobil_count != 0:
            bantuan = int(input("Silahkan tekan 1 untuk cetak karcis atau 2 untuk bantuan. \n"))
            space()
            if bantuan == 1:
                check = 0
                while check < slot_mobil:
                    if mobil[check] == 1:
                        slot = check
                        check = 999
                    check = check + 1
                mobil[slot] = mobil[slot] - 1
                print("[TERIMAKASIH]\nAnda parkir pada slot", str(slot + 1))
                space()
                start_mobil[slot] = time.time()
            else :
                print("Menghubungi Operator...")
                space()

        elif mobil_count == 0 or motor_count == 0:
            print("Mohon maaf parkiran telah penuh.")
            space()
            
        else:
            print("[MOHON MAAF SILAHKAN COBA LAGI]")
            space()
