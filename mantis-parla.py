#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# autor: joan català <joan@riseup.net>
# web: http://joancatala.net
#

# Importem moduls
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import feedparser, datetime, os, difflib, time
from pathlib import Path
from sty import fg, bg, ef, rs, RgbFg

#Configuracions vàries
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
horaActual = datetime.datetime.now()
directori = "~/.mantis_parla/"
fitxer_economica_tickets = "/home/joan/.mantis_parla/economicatickets.txt"
fitxer_economica_ultims = "/home/joan/.mantis_parla/economicaticketsultims.txt"
fitxer_economica_distints = "/home/joan/.mantis_parla/economicaticketsdistints.txt"

fitxer_informatica_tickets = "/home/joan/.mantis_parla/informaticatickets.txt"
fitxer_informatica_ultims = "/home/joan/.mantis_parla/informaticaticketsultims.txt"
fitxer_informatica_distints = "/home/joan/.mantis_parla/informaticaticketsdistints.txt"

fitxer_pwm_tickets = "/home/joan/.mantis_parla/pwmtickets.txt"
fitxer_pwm_ultims = "/home/joan/.mantis_parla/pwmticketsultims.txt"
fitxer_pwm_distints = "/home/joan/.mantis_parla/pwmticketsdistints.txt"

fitxer_app_tickets = "/home/joan/.mantis_parla/apptickets.txt"
fitxer_app_ultims = "/home/joan/.mantis_parla/appticketsultims.txt"
fitxer_app_distints = "/home/joan/.mantis_parla/appticketsdistints.txt"

fitxer_padron_tickets = "/home/joan/.mantis_parla/padrontickets.txt"
fitxer_padron_ultims = "/home/joan/.mantis_parla/padronticketsultims.txt"
fitxer_padron_distints = "/home/joan/.mantis_parla/padronticketsdistints.txt"

fitxer_juridica_tickets = "/home/joan/.mantis_parla/juridicatickets.txt"
fitxer_juridica_ultims = "/home/joan/.mantis_parla/juridicaticketsultims.txt"
fitxer_juridica_distints = "/home/joan/.mantis_parla/juridicaticketsdistints.txt"

fitxer_ens_tickets = "/home/joan/.mantis_parla/enstickets.txt"
fitxer_ens_ultims = "/home/joan/.mantis_parla/ensticketsultims.txt"
fitxer_ens_distints = "/home/joan/.mantis_parla/ensticketsdistints.txt"

fitxer_menor_tickets = "/home/joan/.mantis_parla/menortickets.txt"
fitxer_menor_ultims = "/home/joan/.mantis_parla/menorticketsultims.txt"
fitxer_menor_distints = "/home/joan/.mantis_parla/menorticketsdistints.txt"

# Mostrem un logo xulo, la URL, la versió, l'hora actual i l'hora en un minut
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
os.system("clear")
os.system("toilet -f future -F metal Mantis Bug Tracker")
print ("URL: http://incidencias.dipcas.es\t VERSION: 1.0")
print ("HORA ACTUAL: ",(horaActual.strftime("%H:%M:%S")),"\t\t\t VOZ: espeak\n")

# Anem a comprovar si és la primera vegada que l'usuari executa l'aplicació o, si pel contnrari, 
# l'usuari ja ha entrat més vegades. Aleshores anem a comprovar si ja tenim el ~/.mantis_parla/
# i en cas de que no, guardarem les incidències al fitxer nous.txt	
# Guardarem també: sessio (no_primera_vegada o primera_vegada)

if os.path.isdir("/home/joan/.mantis_parla"):
	#DEBUG
	#print ("SI EXISTEIX EL DIRECTORI")
	sessio = "no_primera_vegada"
else:
	#DEBUG
	#print ("NO EXISTEIX MANTIS_PARLA")
	os.system("mkdir " + directori)
	sessio = "primera_vegada"

# Esborrem fitxers *ultims per a netejar l'inici del programa
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Si existeix 'economicaultims.txt', l'esborrem.
if (Path(fitxer_economica_ultims).is_file()):
	os.system('rm  ' + fitxer_economica_ultims)
	
# Si existeix 'informaticaultims.txt', l'esborrem.	
if (Path(fitxer_informatica_ultims).is_file()):
	os.system('rm  ' + fitxer_informatica_ultims)	
		
# Si existeix 'pwmultims.txt', l'esborrem.	
if (Path(fitxer_pwm_ultims).is_file()):
	os.system('rm  ' + fitxer_pwm_ultims)	
	
# Si existeix 'padronultims.txt', l'esborrem.	
if (Path(fitxer_padron_ultims).is_file()):
	os.system('rm  ' + fitxer_padron_ultims)	
		
# Si existeix 'juridicaultims.txt', l'esborrem.	
if (Path(fitxer_juridica_ultims).is_file()):
	os.system('rm  ' + fitxer_juridica_ultims)	
	
# Si existeix 'ensultims.txt', l'esborrem.	
if (Path(fitxer_ens_ultims).is_file()):
	os.system('rm  ' + fitxer_ens_ultims)	
	
# Si existeix 'menorultims.txt', l'esborrem.	
if (Path(fitxer_menor_ultims).is_file()):
	os.system('rm  ' + fitxer_menor_ultims)	
	
			
# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de Asistencia Economica
# ---------------------------------------------------------------------------------------------
FeedEconomica = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")	
	
try:
	if (FeedEconomica.entries[0] != ''):		
		print ("\n\nNOUS TICKETS A L'ASSISTÈNCIA ECONÒMICA")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedEconomica['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_economica_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_economica_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_economica_tickets, 'r') as fitxer_tickets:
			with open(fitxer_economica_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_economica_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_economica_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_economica_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats a la Assistencia Econòmica'")
		
		fitxer_distints = open(fitxer_economica_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_economica_ultims + ' ' + fitxer_economica_tickets)
		os.system('rm ' + fitxer_economica_distints)
    			
except:
		
		exit




# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de Asistencia Informatica
# ---------------------------------------------------------------------------------------------
# Agafem els tickets via RSS
FeedInformatica = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedInformatica.entries[0] != ''):		
		print ("\nNOUS TICKETS A L'ASSISTÈNCIA INFORMÀTICA")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedInformatica['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_informatica_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_informatica_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_informatica_tickets, 'r') as fitxer_tickets:
			with open(fitxer_informatica_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_informatica_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_informatica_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_informatica_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats a la Assistencia Informàtica'")
		
		fitxer_distints = open(fitxer_informatica_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_informatica_ultims + ' ' + fitxer_informatica_tickets)
		os.system('rm ' + fitxer_informatica_distints)
    			
except:
		
		exit
		
		




# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de PWM
# ---------------------------------------------------------------------------------------------
FeedPWM = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedPWM.entries[0] != ''):		
		print ("\nNOUS TICKETS AL PROJECTE WEB MUNICIPAL")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedPWM['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_pwm_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_pwm_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_pwm_tickets, 'r') as fitxer_tickets:
			with open(fitxer_pwm_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'pwmdistints.txt'
			f=open(fitxer_pwm_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_pwm_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_pwm_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats al Projecte Web Municipal'")
		
		fitxer_distints = open(fitxer_pwm_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_pwm_ultims + ' ' + fitxer_pwm_tickets)
		os.system('rm ' + fitxer_pwm_distints)
    			
except:
		
		exit



# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de APP
# ---------------------------------------------------------------------------------------------
FeedApp = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedApp.entries[0] != ''):		
		print ("\nNOUS TICKETS A L'APP DELS AJUNTAMENTS")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedApp['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_app_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_app_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_app_tickets, 'r') as fitxer_tickets:
			with open(fitxer_app_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_app_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_app_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_app_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats a la App dels Ajuntaments'")
		
		fitxer_distints = open(fitxer_app_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_app_ultims + ' ' + fitxer_app_tickets)
		os.system('rm ' + fitxer_app_distints)
    			
except:
		
		exit
		
		
		
# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de Padrón Municipal de Habitantes
# ---------------------------------------------------------------------------------------------
FeedPadron = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedPadron.entries[0] != ''):		
		print ("\nNOUS TICKETS AL PADRÓ MUNICIPAL D'HABITANTS")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedPadron['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_padron_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_padron_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_padron_tickets, 'r') as fitxer_tickets:
			with open(fitxer_padron_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_padron_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_padron_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_padron_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats al Padró Municipal dHabitants'")
		
		fitxer_distints = open(fitxer_padron_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_padron_ultims + ' ' + fitxer_padron_tickets)
		os.system('rm ' + fitxer_padron_distints)
    			
except:
		
		exit
		
			
			
# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de Asistencia Juridica
# ---------------------------------------------------------------------------------------------
FeedJuridica = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedJuridica.entries[0] != ''):		
		print ("\nNOUS TICKETS A L'ASSISTÈNCIA JURÍDICA")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedJuridica['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_juridica_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_juridica_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_juridica_tickets, 'r') as fitxer_tickets:
			with open(fitxer_juridica_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_juridica_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_juridica_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_juridica_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats a la Assistència Jurídica'")
		
		fitxer_distints = open(fitxer_juridica_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_juridica_ultims + ' ' + fitxer_juridica_tickets)
		os.system('rm ' + fitxer_juridica_distints)
    			
except:
		
		exit
		
						
# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de ENS RGPD
# ---------------------------------------------------------------------------------------------
FeedENS = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedENS.entries[0] != ''):		
		print ("\nNOUS TICKETS AL ESQUEMA NACIONAL DE SEGURETAT I RGPD")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedENS['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_ens_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_ens_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_ens_tickets, 'r') as fitxer_tickets:
			with open(fitxer_ens_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_ens_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_ens_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_economica_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats a lEsquema Nacional de Seguretat i RGPD'")
		
		fitxer_distints = open(fitxer_economica_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_ens_ultims + ' ' + fitxer_ens_tickets)
		os.system('rm ' + fitxer_ens_distints)
    			
except:
		
		exit
	
		
		
# ---------------------------------------------------------------------------------------------
# Anem mostrant els feeds de Menor RGPD
# ---------------------------------------------------------------------------------------------
FeedMenorRGPD = feedparser.parse("ACÍ_HAS_DE_FICAR_EL_TEU_RSS")

try:
	if (FeedMenorRGPD.entries[0] != ''):		
		print ("\n\nNOUS TICKETS A MENOR RGPD")
		print ("=======================================================================================")
	
		# DESCARREGUEM ELS RSS I PREPAREM ELS FITXERS 'tickets.txt' I 'ultims.txt'
	   	
		for i in FeedMenorRGPD['entries']:
			linea_neta = (i['title'].replace("[privado]", " "))
			# Finalment, imprimim els feeds de l'RSS
			#print (linea_neta[9:])	  
								
			
			# Accedim per primera vegada a mantis-parla.py
			
			if (sessio == "primera_vegada"):
				f=open(fitxer_menor_tickets,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
			
			# No accedim per primera vegada a mantis-parla.py
			
			if (sessio == "no_primera_vegada"):
				f=open(fitxer_menor_ultims,"a")
				f.write(linea_neta[9:] + "\n")
				f.close()
	

		# Comparem tickets i ultims.txt, i a continuació imprimim la diferència (anomenant a cada linea 'distints')
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		with open(fitxer_menor_tickets, 'r') as fitxer_tickets:
			with open(fitxer_menor_ultims, 'r') as fitxer_ultims:
				difference = set(fitxer_ultims).difference(fitxer_tickets)

		for distints in difference:
			#print (distints.replace("\n", " "))	 # <--- Aquesta és la línea distinta entre fitxer_tickets i fitxer_ultims
			# Ara la pintaré de color verd.
			print (fg.green + distints.replace("\n", " ") + fg.rs)
			
			# creem ek fitxer 'distints.txt'
			f=open(fitxer_menor_distints,"a")
			f.write(distints)
			f.close()
			
		# I ara, finalment, una vegada impressos per pantalla els 'distints', ara imprimim el fitxer tickets.txt i ja
		# estaran tots els tickets mostrats: dalt els nous (o distints) i a continuació l'anterior fitxer tickets				
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		lista_tickets = []
		i = 0
		fitxer_tickets = open(fitxer_menor_tickets, "r") 
		for line in fitxer_tickets:
			lista_tickets.append(line)
			print (lista_tickets[i].replace("\n", " "))	
			i = i+1 
			
		# Parlem amb espeak
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
		# Si existeix 'distints, llancem espeak
		if (Path(fitxer_menor_distints).is_file()):
			os.system("espeak -vca 'Hi ha novetats a la Assistencia Econòmica'")
		
		fitxer_distints = open(fitxer_menor_distints, "r") 
		for line in fitxer_distints:
				os.system('espeak -vca "%s"' % line)
				time.sleep (.5)
				
		# Netejem fitxers ultims.txt i distints.txt
		#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		os.system('mv ' + fitxer_menor_ultims + ' ' + fitxer_menor_tickets)
		os.system('rm ' + fitxer_menor_distints)
    			
except:
		
		exit
		

# Fi
print ("\n\n")
