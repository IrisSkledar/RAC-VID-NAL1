
import cv2 as cv
import numpy as np
import time


def zmanjsaj_sliko(slika, sirina, visina):
    '''Zmanjšaj sliko na velikost sirina x visina.'''
    pass


def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    '''Sprehodi se skozi sliko v velikosti škatle (sirina_skatle x visina_skatle) in izračunaj število pikslov kože v vsaki škatli.
    Škatle se ne smejo prekrivati!
    Vrne seznam škatel, s številom pikslov kože.
    Primer: Če je v sliki 25 škatel, kjer je v vsaki vrstici 5 škatel, naj bo seznam oblike
      [[1,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1]].
      V tem primeru je v prvi škatli 1 piksel kože, v drugi 0, v tretji 0, v četrti 1 in v peti 1.'''
    pass


def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    '''Prestej število pikslov z barvo kože v škatli.'''
    pass


def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Ta funkcija se kliče zgolj 1x na prvi sliki iz kamere.
    Vrne barvo kože v območju ki ga definira oklepajoča škatla (levo_zgoraj, desno_spodaj).
      Način izračuna je prepuščen vaši domišljiji.'''
    # Izrežemo območje, kjer bomo določili barvo kože
    izrez = slika[levo_zgoraj[1]:desno_spodaj[1], levo_zgoraj[0]:desno_spodaj[0]]

    # Izračunaj povprečno barvo v tem območju (BGR vrednosti) mean računa aritmetično sredino
    povprecna_barva = np.mean(izrez, axis=(0, 1))  # Povprečne vrednosti po BGR kanalih

    # Nastavimo meje okoli povprečne barve kože
    spodnja_meja = np.array(
        [max(0, povprecna_barva[0] - 10), max(0, povprecna_barva[1] - 10), max(0, povprecna_barva[2] - 10)],
        dtype=np.uint8)
    zgornja_meja = np.array(
        [min(255, povprecna_barva[0] + 10), min(255, povprecna_barva[1] + 10), min(255, povprecna_barva[2] + 10)],
        dtype=np.uint8)

    return spodnja_meja, zgornja_meja

def narisi_skatle(slika, rezultat, sirina_skatle, visina_skatle, prag=300):
    pass

def izracunaj_fps(start_time, frame_count):
    pass

def narisi_modri_okvir(slika, levo_zgoraj, desno_spodaj):
    pass

if __name__ == '__main__':
    # Pripravi kamero
    kamera = cv.VideoCapture(0)
    start_time = time.time()
    frame_count = 0
    barva_koze = None

    sirina_slike = 340
    visina_slike = 220

    sirina_skatle = 100
    visina_skatle = 100

    levo_zgoraj = ((sirina_slike - sirina_skatle) // 2, (visina_slike - visina_skatle) // 2)
    desno_spodaj = (levo_zgoraj[0] + sirina_skatle, levo_zgoraj[1] + visina_skatle)
    while True:
    # Zajami prvo sliko iz kamere
        ret, slika = kamera.read()
        if not ret:
            break

        if barva_koze is None:  # Samo prvič, ko določimo barvo kože
            # Nariši modri okvir okoli območja za določitev barve kože
            narisi_modri_okvir(slika, levo_zgoraj, desno_spodaj)

            # Ko pritisnemo 's', določimo barvo kože v območju
            if cv.waitKey(1) & 0xFF == ord('s'):
                barva_koze = doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj)
                print("Barva kože določena:", barva_koze)

        if barva_koze is not None:  # Ko imamo določeno barvo kože
            # Obdelava slike s škatlami in preštevanje pikslov kože
            rezultat = obdelaj_sliko_s_skatlami(slika, 10, 10, barva_koze)

            # Nariši škatle z dovolj pikslov kože
            narisi_skatle(slika, rezultat, 10, 10, prag=10)

    # Označi območja (škatle), kjer se nahaja obraz (kako je prepuščeno vaši domišljiji)
    # Vprašanje 1: Kako iz števila pikslov iz vsake škatle določiti celotno območje obraza (Floodfill)?
    # Vprašanje 2: Kako prešteti število ljudi?

    # Kako velikost prebirne škatle vpliva na hitrost algoritma in točnost detekcije? Poigrajte se s parametroma velikost_skatle
    # in ne pozabite, da ni nujno da je škatla kvadratna.
    pass