from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input("Digite a URL do vídeo que deseja baixar: ")
path = input("Digite o diretório onde deseja salvar o arquivo: ")
youtube = YouTube(link)

# Faz o download do arquivo
print("Baixando...")
ys = youtube.streams.filter(only_audio=True).first().download(path)
print("Download finalizado!")

# No streams, o default_filename retorna apenas o nome da música
# Definindo o título padrão como [Nome do Artista - Nome da Música]
title = youtube.author + " - " + youtube.title

# Converte de MP4 para MP3
print("Convertendo arquivo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, title + '.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

print("Arquivo gravado com sucesso!")
