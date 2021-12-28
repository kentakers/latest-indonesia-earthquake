from bs4 import BeautifulSoup
import requests


def ekstraksi_data():
    """
    Proses pengambilan data pada situs BMKG
    menggunakan package BeautifulSoup dan requests
    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")

        result = soup.find(
            "span", {"class": "waktu"}
        )  # Tag dan class harus disesuaikan dengan elemen yang ada di BMKG (inspect)
        result = result.text.split(", ")
        tanggal = result[0]
        waktu = result[1]

        result = soup.find("ul", {"class": "list-unstyled"})
        result = result.findChildren("li")

        i = 0
        # beberapa variabel dengan nilai yang sama
        magnitudo = ls = bt = kedalaman = koordinat = lokasi = tsunami = None

        for res in result:
            #print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(" - ")
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                tsunami = res.text

            i += 1

        hasil = dict()
        hasil["tanggal"] = tanggal
        hasil["waktu"] = waktu
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = {"ls": ls, "bt": bt}
        hasil["lokasi"] = lokasi
        hasil["tsunami"] = tsunami
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print("\nGempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal \t: {result['tanggal']}")
    print(f"Waktu \t\t: {result['waktu']}")
    print(f"Magnitudo \t: {result['magnitudo']}")
    print(f"Kedalaman \t: {result['kedalaman']}")
    print(
        f"Koordinat \t: LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}"
    )
    print(f"Lokasi \t\t: {result['lokasi']}")
    print(f"Tsunami \t: {result['tsunami']}")
