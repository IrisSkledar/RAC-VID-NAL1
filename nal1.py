
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

    visina, sirina, _ = slika.shape
    rezultat = []
    for y in range(0, visina - visina_skatle, visina_skatle):  # Premikamo se po sliki
        vrstica = []
        for x in range(0, sirina - sirina_skatle, sirina_skatle):
            # Izrežemo podsliko (škatlo)
            skatla = slika[y:y + visina_skatle, x:x + sirina_skatle]
            # Preštejemo piksle kože v tej škatli
            st_koza = prestej_piklse_z_barvo_koze(skatla, barva_koze)
            vrstica.append(st_koza)
        rezultat.append(vrstica)

    return rezultat


def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    '''Prestej število pikslov z barvo kože v škatli.'''
    pass


def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Ta funkcija se kliče zgolj 1x na prvi sliki iz kamere.
    Vrne barvo kože v območju ki ga definira oklepajoča škatla (levo_zgoraj, desno_spodaj).
      Način izračuna je prepuščen vaši domišljiji.'''
    pass

def narisi_skatle(slika, rezultat, sirina_skatle, visina_skatle, prag=300):
    '''Nariši pravokotnike na območjih z veliko kožnimi piksli.'''
    for y, vrstica in enumerate(rezultat):
        for x, st_pikslov in enumerate(vrstica):
            if st_pikslov > prag:
                zgoraj = y * visina_skatle
                levo = x * sirina_skatle
                cv.rectangle(slika, (levo, zgoraj),
                             (levo + sirina_skatle, zgoraj + visina_skatle),
                             (0, 255, 0), 2)


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
    # Izračunamo barvo kože na prvi sliki

    # Zajemaj slike iz kamere in jih obdeluj



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