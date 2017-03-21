LoraWan module
================================

Ce code de module est basé sur la l'exemple officiel de PyCom
disponible à l'adresse:
https://github.com/pycom/pycom-libraries/tree/master/examples/loraNanoGateway .
Des fonctions de debug visuel et debug console ont été ajoutés pour faciliter
l'utilisation de la gateway.

Obtenir l'adresse LoRa Mac du Lopy
----------------------

Dans la console python du module, executer le code suivant pour obtenir
l'adresse LoRa Mac du modue

```
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
```

Configuration
----------------------

Editer le fichier config.py et remplissez les champs suivants:

```
DEV_EUI = '<DEV_EUI>'
APP_EUI = '<APP_EUI>'
APP_KEY = '<APP_KEY>'
```

Debug
----------------------

Un debug 'visuel' a été ajouté, pour l'activer, positionnez la variable
"DEBUG_LED" à 'True'.

- LED rouge: Connection au réseau LoRa
- LED verte: Envoi d'un paquet
- LED bleue: Réception d'un paquet
