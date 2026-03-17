import random
import datetime

list_mood = ("senang", "sedih", "semangat", "santai", "galau")
set_mood = set()
riwayat_mood = []

def daftar_mood():
    print("Daftar mood:")
    for mood in list_mood:
        print("-", mood)

def rekomendasi_lagu(mood):
    if mood == "senang":
        lagu = random.choice(["yellow", "clap!", "hello", "my treasure"])
    elif mood == "sedih":
        lagu = random.choice(["whatever whenever", "it's okay", "the way to"])
    elif mood == "santai":
        lagu = random.choice(["darari", "yamai", "be with me"])
    elif mood == "semangat":
        lagu = random.choice(["run", "i love you", "jikjin"])
    elif mood == "galau":
        lagu = random.choice(["orange", "hold it in", "better than me"])
    else:
        print("Mood tidak valid")
        return

    print("Rekomendasi lagu:", lagu)

def main():
    print("=== Rekomendasi Lagu TREASURE Berdasarkan Mood ===")

    while True:
        print("\nMenu:")
        print("1. Lihat daftar mood")
        print("2. Rekomendasi lagu")
        print("3. Keluar")

        menu = input("Pilih menu (1-3): ")

        if menu == "1":
            daftar_mood()

        elif menu == "2":
            mood = input("Masukkan mood: ")

            if mood == "":
                print("Mood harus diisi")
                continue

            if mood not in list_mood:
                print("Mood tidak tersedia")
                continue

            riwayat_mood.append(mood)
            set_mood.add(mood)

            rekomendasi_lagu(mood)

        elif menu == "3":
            break

        else:
            print("Menu tidak valid")

    print("\nRiwayat mood:")
    for m in riwayat_mood:
        print("-", m)

    print("Mood unik:", set_mood)
    print("Waktu selesai:", datetime.datetime.now())


if __name__ == "__main__":
    main()