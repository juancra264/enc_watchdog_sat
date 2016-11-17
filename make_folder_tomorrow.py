#!/usr/bin/python
#----------------------------------------------------------------------------------
# Descripcion:
#   Crear la carpeta del dia siguiente segun el path ingresado
# Modo de ejecucion:
#   Se ejecuta por tiempo en un crontab todos los dias a 20:00 pm
#   crontab:
#		0 20 * * * python /home/user/make_folder_tomorrow.py
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
def check_tomorrow_folder(base_path):
	tomorrow = datetime.datetime.today() + datetime.timedelta(1) 
	year = datetime.datetime.strftime(tomorrow,'%Y')
	month = datetime.datetime.strftime(tomorrow,'%m')
	day = datetime.datetime.strftime(tomorrow,'%d')
	path = base_path + year + '/' + month + '/' + day
	if not os.path.exists(path):
		os.makedirs(path)
	return;

def main():
	check_tomorrow_folder('/ffmpeg_video/rcn-hd-1/')
	return;

# #############################################
#               MAIN SCRIPT
# #############################################
if __name__ == '__main__':
	main()
