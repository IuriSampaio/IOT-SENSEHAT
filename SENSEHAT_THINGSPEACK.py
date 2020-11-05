from sense_emu import SenseHat
import time
import thingspeak

thing_ID = "1218262"
thing_key = "6YI56E62Q38IY3FT"
thing_channel = thingspeak.Channel(thing_ID, thing_key)

sense = SenseHat()
sense.clear()

sense.show_message("agr to usando thing speak")

while True:
	temperature = sense.get_temperature()
	humidity = sense.get_humidity()
	payload = {'field1':temperature, 'field2':humidity}

	if(thing_channel.update(payload)):
		print ("Dados: ",payload," enviados para nuvem")
	else:
		print ("ERRO AO ENVIAR OS DADOS")

	time.sleep(10)

