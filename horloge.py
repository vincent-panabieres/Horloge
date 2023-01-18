Copy code
import time

def afficher_heure():
    heure_actuelle = time.localtime()
    heures = heure_actuelle.tm_hour
    minutes = heure_actuelle.tm_min
    secondes = heure_actuelle.tm_sec
    print("{:02d}:{:02d}:{:02d}".format(heures, minutes, secondes))

def regler_heure(heures, minutes, secondes):
    heure_actuelle = time.localtime()
    heure_actuelle = time.struct_time((heure_actuelle.tm_year, heure_actuelle.tm_mon, heure_actuelle.tm_mday, heures, minutes, secondes, heure_actuelle.tm_wday, heure_actuelle.tm_yday, heure_actuelle.tm_isdst))
    time.localtime(time.mktime(heure_actuelle))

def regler_alarme(heures, minutes, secondes):
    while True:
        afficher_heure()
        heure_actuelle = time.localtime()
        if heure_actuelle.tm_hour == heures and heure_actuelle.tm_min == minutes and heure_actuelle.tm_sec == secondes:
            print("Alarme!")
            break
        time.sleep(1)

regler_heure(16, 30, 0)
regler_alarme(16, 30, 0)