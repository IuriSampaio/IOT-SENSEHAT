from sense_emu import SenseHat
import time
import thingspeak

thing_id = "1220519"
thing_key = "FCWA8LQ9NTSXFISB"
thing_channel = thingspeak.Channel( thing_id , thing_key )

sense = SenseHat()
sense.show_message("SmartCities",text_colour=[0,0,255])

while True:

	temperature = sense.get_temperature()
	humidity = sense.get_humidity()

	formated_humidity = f'{int(humidity)}%'

	if( humidity >= 40 and humidity <= 60 ):
		print ("ESTADO NORMAL :)")
		sense.show_message(formated_humidity,text_colour=[0,255,0])
	else:
		print ("!!! ESTADO DE ATENCAO !!! :!")
		sense.show_message(formated_humidity,text_colour=[255,0,0])

	data = { 'field1':temperature, 'field2':humidity }

	if( thing_channel.update(data) ):
		print (F"TEMPERATURA: {temperature} C \nHUMIDADE: {formated_humidity}")
		print ("DADOS ENVIADOS COM SUCESSO PARA THINGSPEAK")
	else:
		print ("ERRO NAO FOI POSSIVEL ENVIAR OS DADOS")

	print ("\n=====================================\n")
	time.sleep(2)


