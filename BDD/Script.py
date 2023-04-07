import paho.mqtt.client as mqtt
import json as json
import base64
import psycopg2


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    resultat_complet = json.loads(msg.payload.decode())
    print(resultat_complet)
    payload = resultat_complet['uplink_message']['frm_payload']
    date = resultat_complet
    print("Information reçu :", base64.b64decode(payload).decode(), "\nà la date : ", resultat_complet['received_at'])
    varPrincip = base64.b64decode(payload).decode()
    i = 0

    while i < len(varPrincip):

        if varPrincip[i] == "#":  # Valeur Hexa de "#"= 23
            temp = ord(varPrincip[i - 1])
            print(temp)
        elif varPrincip[i] == "$":  # Valeur Hexa de "$"=24
            vol = ord(varPrincip[i - 1])
            print(vol)
        elif varPrincip[i] == "%":  # Valeur Hexa de "%"=25
            haut = ord(varPrincip[i - 1])
            print(haut)
        elif varPrincip[i] == "&":  # Valeur Hexa de "&"=26
            id = ord(varPrincip[i - 1])
            print(id)
        i += 1

    try:
        conn = psycopg2.connect(
            user="postgres",
            password="admin",
            host="172.20.10.3",
            port="5432",
            database="eaux"
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO Mesure(temperature,volume,hauteur,id_bassin) VALUES(%s,%s,%s,%s)",
                    (temp, vol, haut, id))
        conn.commit()
        conn.close()


    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à PostgreSQL", error)


client = mqtt.Client()
client.username_pw_set("recupeauxcapt-1@ttn",
                       "NNSXS.4CMRYPQ5HSOOO536ROSQLXW3JPX6EOB7RTCSUUY.M7JAMDT7PG2PVT6LR2Q5KSKUC6W5XY3F3YLS5RRTU72RR5P4ACAQ")

client.on_connect = on_connect
client.on_message = on_message

client.connect("eu1.cloud.thethings.network", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
