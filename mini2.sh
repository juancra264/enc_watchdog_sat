#!/bin/bash

# ************************************************************************************************
# Script para captura de video BlackMagic Decklink + FFMPEG
#
#		ENTRADA
#		Board de Entrada: 			Decklink Mini Recorder	
#		Puerto de entrada:			HDMI
#		Tipo de senal de entrada:	1080i59.94	(HD HDMI)
#		 
#		SALIDA
#		Tipo de salida:				FILE cada 5 mins
#		Tamano de cuadro:			848x480
#		Codec video:				H.264
#		Deinterlace:				Habilitado (yadif=0:0:1)
#		Frame rate:					29 fps
#		Bitrate video:				250Kbps
#		Codec audio:				NO AUDIO
#		Bitrate audio:				NO AUDIO
#		Contenedor:					.mp4
#		Almacenamiento:				bettysat-storage(172.20.7.211)
#		Ruta Almacenamiento:		/ffmpeg_video/rcn-hd-1/{year}/{month}/{day}/RCN_Ch1_....
# 	
# ************************************************************************************************

# Marca para log de salida de FFMPEG:
# 	-loglevel warning

# Codifacion en linea FFMPEG:
ffmpeg \
 -video_input "hdmi" \
 -hide_banner \
 -f decklink \
 -i 'DeckLink Mini Recorder@11' \
 -vsync 0 \
 -filter_complex "scale=848x480,yadif=0:0:1,pad=848:500:0:0:0x00008B,drawtext=fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf':text='RCN TV S.A - BettySAT Analizador1 '%{localtime}'':x=5:y=486:fontcolor=yellow:fontsize=12" \
 -f segment \
 -vcodec libx264 \
 -profile:v baseline \
 -level 3 \
 -pix_fmt yuv420p \
 -force_key_frames 'expr:gte(t,n_forced*2)' \
 -b:v 250k \
 -an \
 -reset_timestamps 1 \
 -segment_format_options movflags=+faststart \
 -segment_atclocktime 1 \
 -strftime 1 \
 -segment_time 300 \
 -map 0 \
 /ffmpeg_video/rcn-hd-1/%Y/%m/%d/RCN_CH_1_'%Y_%m_%d'_%H_%M_%S.mp4
