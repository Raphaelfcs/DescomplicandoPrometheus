import requests
import json
import time
from prometheus_client import start_http_server, Gauge

url_numero_pessoas = "http://api.open-notify.org/astros.json"
url_local_ISS = "http://api.open-notify.org/iss-now.json"

def pega_local_iss():
    try:
        """
        Pegar o local atual da ISS
        """
        response = requests.get(url_local_ISS)
        data = response.json()
        return data['iss_position']
    except Exception as e:
        print("Tivemos problemas em obter informacoes da localizacao")
        raise e

def pega_numero_astronautas():
    try:
        """
        Pegar o número de astronautas que estão no espaço!!!!
       
        """
        response = requests.get(url_numero_pessoas)
        data = response.json()
        return data['number']
    except Exception as e:
        print("Tivemos problemas para acessar a URL")
        raise e
    
def atualiza_metricas():
    try:
        """
        Atualiza a Metricas com número de astronautas no espaço!!!!
        E local da ISS
        """
        numero_pessoas = Gauge('numero_de_astronautas', 'Número de astronaitas no espaço')
        longitude_iss = Gauge('longitude_iss', 'Longitude atual da ISS')
        latitude_iss = Gauge('latitude_iss', 'latitude atual da ISS')
        while True:
            numero_pessoas.set(pega_numero_astronautas())
            longitude_iss.set(pega_local_iss()['longitude'])
            latitude_iss.set(pega_local_iss()['latitude'])
            time.sleep(10)
            print("o Número de Astronautas no espaço nesse momento é: %s" % pega_numero_astronautas())
            print("A longitude atual da ISS é: %s" % (pega_local_iss()['longitude']))
            print("A latitude atual da ISS é: %s" % (pega_local_iss()['latitude']))
    except Exception as e:
        print("Tivemos problemas para realizar a atualizacao da métrica")
        raise e

def inicia_exporter():
    try:
        """
        Inicia O http Server!!!!
        """
        start_http_server(8899)
        return True
    except Exception as e:
        print("Tivemos problemas ao iniciar o HTTP Server")
        raise e

def main():
    try:
        """
        A nossa função principal que irá chamar as demais
        """
        inicia_exporter()
        print("HTTP SERVER INICIADO")
        atualiza_metricas()
    except Exception as e:
        print("Tivemos problemas na inicialização do nosso EXPORTER")
        exit(1)

if __name__ == '__main__':
    main()
    exit(0)