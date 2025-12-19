import RPi.GPIO as IO
import time

# On définit le PIN ici pour être sûr
SERVO_PIN = 12 

def activer_moteur_seuil():
    # Initialisation locale pour éviter les conflits de signal
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(SERVO_PIN, IO.OUT)
    
    pwm = IO.PWM(SERVO_PIN, 50) # Fréquence 50Hz
    pwm.start(0) # Démarre sans bouger

    try:
        # --- PHASE 1 : OUVERTURE ---
        print("Moteur : Ouverture à 90°")
        duty_open = (90 / 18.0) + 2.5
        pwm.ChangeDutyCycle(duty_open)
        time.sleep(0.8)       # Laisse le temps au bras de bouger
        pwm.ChangeDutyCycle(0) # STOPPE LE SIGNAL (Arrête les vibrations)
        
        # --- PHASE 2 : ATTENTE ---
        time.sleep(2.0)       # Reste dans cette position 2 secondes
        
        # --- PHASE 3 : FERMETURE ---
        print("Moteur : Retour à 0°")
        duty_close = (0 / 18.0) + 2.5
        pwm.ChangeDutyCycle(duty_close)
        time.sleep(0.8)       # Laisse le temps de revenir
        pwm.ChangeDutyCycle(0) # STOPPE LE SIGNAL (Fini les sifflements)

    finally:
        pwm.stop() # Arrête proprement le PWM
        # On ne fait PAS GPIO.cleanup() ici pour ne pas couper les autres capteurs