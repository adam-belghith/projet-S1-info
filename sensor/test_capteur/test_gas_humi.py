import time
import sys
import seeed_dht
from grove.adc import ADC

class GroveGasSensorMQ2:
    """Classe pour le capteur de gaz MQ2"""
    
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value


def main2(port_temp_humi,port_CO2):
    # Définir le canal par défaut à 0 si aucun argument n'est fourni
    adc_channel = port_CO2

    
    # Initialisation du capteur DHT22 (pin 22)
    sensor_dht = seeed_dht.DHT(str(port_temp_humi), port_temp_humi)
    
    # Initialisation du capteur de gaz MQ2
    sensor_gas = GroveGasSensorMQ2(adc_channel)
    
    #print('Démarrage de la détection...')
    #print('-' * 50)
    
    try:
        while True:
            # Lecture du capteur DHT22 (température et humidité)
            humi, temp = sensor_dht.read()
            
            if humi is not None:
                print('DHT{0} - Humidité: {1:.1f}%, Température: {2:.1f}°C'.format(
                    sensor_dht.dht_type, humi, temp))
            else:
                print('DHT{0} - Erreur de lecture: {1}'.format(
                    sensor_dht.dht_type, temp))
            
            # Lecture du capteur de gaz MQ2
            gas_value = sensor_gas.MQ2
            #print('MQ2 - Valeur du gaz: {0}'.format(gas_value))
            
            #print('-' * 50)
            return humi, temp, gas_value
            time.sleep(1)
            
    except KeyboardInterrupt:
        print('\nArrêt du programme')
        sys.exit(0)


if __name__ == '__main__':
    main2()
