import numpy as np
import cv2 as cv
import time
import nal1

# Enostaven test za zmanjsaj_sliko
def test_zmanjsaj_sliko():
    slika = np.ones((100, 100, 3), dtype=np.uint8) * 255  # bela slika
    nova_slika = nal1.zmanjsaj_sliko(slika, 50, 50)
    assert nova_slika.shape == (50, 50, 3)

# Test za doloci_barvo_koze
def test_doloci_barvo_koze():
    slika = np.zeros((100, 100, 3), dtype=np.uint8)
    slika[40:60, 40:60] = [100, 150, 200]  # umetna "koža"
    barva_koze = nal1.doloci_barvo_koze(slika, (40, 40), (60, 60))
    spodnja, zgornja = barva_koze
    assert np.all(spodnja <= [100, 150, 200]) and np.all(zgornja >= [100, 150, 200])

# Test za prestej_piklse_z_barvo_koze
def test_prestej_piklse_z_barvo_koze():
    slika = np.zeros((10, 10, 3), dtype=np.uint8)
    slika[0:5, 0:5] = [100, 150, 200]  # 25 pikslov umetne "kože"
    barva_koze = (np.array([90, 140, 190]), np.array([110, 160, 210]))
    st = nal1.prestej_piklse_z_barvo_koze(slika, barva_koze)
    assert st == 25

# Test za obdelaj_sliko_s_skatlami
def test_obdelaj_sliko_s_skatlami():
    slika = np.zeros((20, 20, 3), dtype=np.uint8)
    slika[0:10, 0:10] = [100, 150, 200]  # ena "kožna" škatla
    barva_koze = (np.array([90, 140, 190]), np.array([110, 160, 210]))
    rezultat = nal1.obdelaj_sliko_s_skatlami(slika, 10, 10, barva_koze)
    assert rezultat == [[100, 0], [0, 0]]  # ker je prvih 10x10 pikslov koža, ostalo pa nič

# Test za izracunaj_fps
def test_izracunaj_fps():
    start = time.time() - 2  # kot da je minilo 2 sekundi
    fps = nal1.izracunaj_fps(start, 10)
    assert 4.9 < fps < 5.1  # približno 5 fps
