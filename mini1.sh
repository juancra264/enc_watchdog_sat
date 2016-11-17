#!/bin/bash

# ************************************************************************************************
# Script para captura de video BlackMagic Decklink + FFMPEG
#
#		ENTRADA
#		Board de Entrada: 			Decklink Mini Recorder	
#		Puerto de entrada:			HDMI
#		Tipo de senal de entrada:	720p60	(HD HDMI)
#		 
#		SALIDA
#		Tipo de salida:				FILE
#		Tamano de cuadro:			848x480
#		Codec video:				H.264
#		bitrate video:				250Kbps
#		Codec audio:				NO AUDIO
#		bitrate audio:				NO AUDIO
#		Contenidor:					.mp4
#		Almacenamiento:				bettysat-storage(172.20.7.211)
#		Ruta Almacenamiento:		/ffmpeg_video/rcn-hd-1/{year}/{month}/{day}/RCN_Ch1_....
# 	
# ************************************************************************************************

# Marca para log de salida de FFMPEG:
# 	-loglevel warning

# Almacena la ruta y archivo de la salida para el ffmpeg.
file_path=$(date +"/ffmpeg_video/rcn-hd-1/%Y/%m/%d/RCN_Ch1_%Y_%m_%d_%H_%M_%S.mp4")

# Codifacion en linea FFMPEG:
ffmpeg \
 -loglevel warning \
 -video_input "hdmi" \
 -hide_banner \
 -f decklink \
 -i 'DeckLink Mini Recorder@15' \
 -vsync 0 \
 -filter_complex "scale=848x480,yadif=0:0:1,pad=848:500:0:0:0x00008B,drawtext=fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf':text='RCN TV S.A - BettySAT Analizador1 '%{localtime}'':x=5:y=486:fontcolor=yellow:fontsize=12" \
 -vcodec libx264 \
 -pix_fmt yuv420p \
 -b:v 250k \
 -an \
 -reset_timestamps 1 \
 -segment_format_options movflags=+faststart \
 -segment_atclocktime 1 \
 -strftime 1 \
 -segment_time 1800 \
 "$file_path"
