LoraWan nano gateway
================================

Ce code de nano gateway est basé sur la l'exemple officiel de PyCom
disponible à l'adresse:
https://github.com/pycom/pycom-libraries/tree/master/examples/loraNanoGateway .
Des fonctions de debug visuel et debug console ont été ajoutés pour faciliter
l'utilisation de la gateway.


Création de la gateway sur The Thing network
----------------------

1. Connectez vous sur le site
https://console.thethingsnetwork.org/gateways/register
(créez vous un compte si nécessaire)
2. Selectionner le type "packet forwarder"
3. Créer un EUI à 8 bytes hexadécimaux (https://www.random.org/cgi-bin/randbyte?nbytes=8&format=h)
4. Ajouter une description pour les humains :)
5. Selectionner la fréquence 868MHz
6. Placer la gateway sur la carte
7. Indiquez si votre antenne est intérieure ou extérieure


Configuration
----------------------

Editer le fichier config.py et remplissez les champs suivants:

```
GATEWAY_ID = '<gateway_eui>'

WIFI_SSID = '<ssid>'
WIFI_PASS = '<password>'
```

Debug
----------------------

Un debug 'visuel' a été ajouté, pour l'activer, positionnez la variable
"DEBUG_LED" à 'True'.

- LED rouge: Le réseau s'initialise
- LED verte: Réception d'un paquet via WIFI
- LED bleue: Envoi d'un paquet via Wifi
