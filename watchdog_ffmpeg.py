#!/usr/bin/python
#----------------------------------------------------------------------------------
# Descripcion:
#   Revisa cada minuto que el proceso ffmpeg asociado a un o varios canales este
#	funcionando. Sino reinicia el proceso basado en el script de ffmpeg.
# Modo de ejecucion:
#   Se ejecuta por tiempo en un crontab cada minuto
#   crontab:
#		* * * * * python /home/user/enc_scripts/watchdog_ffmpeg.py   
# Fecha Modificacion: 17 NOV 2016
# Autor: JCRAMIREZ
#----------------------------------------------------------------------------------

#**********************************************************************************
# Library Load
#**********************************************************************************
import os
import sys
import time
import select
import traceback
import smtplib
import datetime
import argparse
import subprocess
import shlex

from subprocess import *
#**********************************************************************************
# Global Variables
#**********************************************************************************

#**********************************************************************************
# Funtions
#********************************************************************************** 
def envio_email(message_in):
	# Toma fecha y hora de la notificacion
	now = datetime.datetime.now()
	now_strg = "%.2i-%.2i-%.2i %.2i:%.2i:%.2i" % (now.year,now.month,now.day,now.hour,now.minute,now.second)	
	sender = 'bettysat-enc@rcntecnica.com'
	receivers = ['jcramirez@rcntv.com.co']
	server = "172.20.7.19"
	email_head = """From: bettysat-enc <bettysat-enc@rcntecnica.com>\nTo: Juan Carlos Ramirez Angel <jcramirez@rcntv.com.co>\nSubject:Evento bettysat-enc FFMPEG\n\n"""
	message = email_head + now_strg + "\n" + message_in + "\n"  
	try:
		smtpObj = smtplib.SMTP(server)
		smtpObj.sendmail(sender, receivers, message)
		print "Notificacion Enviada"
	except:
		print "Error: No se envio notificacion"
	return;

def check_folder_today(base_path):
	# Revisa que la carpeta en el almacenamiento exista, sino la crea.
	today = datetime.datetime.today()
	year = datetime.datetime.strftime(today,'%Y')
	month = datetime.datetime.strftime(today,'%m')
	day = datetime.datetime.strftime(today,'%d')
	path = base_path + year + '/' + month + '/' + day	
	if not os.path.exists(path):
		os.makedirs(path)
	return;
	
def check_ffmpeg():
	#Revisa Canal 1:
	check_folder_today("/ffmpeg_video/rcn-hd-1/")
	pid = subprocess.Popen("""ps -ef | grep "DeckLink Mini Recorder" | grep -v grep | awk '{print $2}'""", shell=True, stdout=PIPE).stdout.read().rstrip()
	if not pid.isdigit():
		subprocess.call('sudo nohup ./mini1.sh &',shell=True,cwd='/home/user/enc_scripts')
		envio_email("Inicio de FFMPEG: canal 1 mini rec hdmi BettySAT Enc")
	return;

def main():
	check_ffmpeg()
	return;

#**********************************************************************************
#       MAIN 
#**********************************************************************************
if __name__ == '__main__':
	main()
