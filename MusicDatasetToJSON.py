import os
import json
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.mp3 import MP3

music_directory = "F:/Sakamichi" # sesuaikan dengan folder yang mau diambil datanya
cover_directory = "F:/Sakamichi/cover" # sesuaikan dengan folder yang mau diambil datanya

def collect_music_data(music_folder, cover_folder):
    data = []
    for root, dirs, files in os.walk(music_folder):
        for file in files:
            full_path = os.path.join(root, file)
            if file.endswith(".mp3"):
                try:
                    audiofile = MP3(full_path, ID3=EasyID3)
                except Exception as e:
                    print(f"Error reading MP3 metadata: {e}")
                    continue
            elif file.endswith(".flac"):
                try:
                    audiofile = FLAC(full_path)
                except Exception as e:
                    print(f"Error reading FLAC metadata: {e}")
                    continue
            else:
                continue
            
            title = audiofile.get('title', [os.path.splitext(file)[0]])[0]
            artist = audiofile.get('artist', ["Unknown"])[0]
            
            cover_path = os.path.join(cover_folder, f"{title}.jpg")
            
            song_data = {
                "title": title,
                "artist": artist,
                "song_path": full_path,
                "cover_path": cover_path
            }
            data.append(song_data)
    return data

music_data = collect_music_data(music_directory, cover_directory)

with open("music_data.json", "w", encoding='utf-8') as f:
    json.dump(music_data, f, ensure_ascii=False, indent=4)

print("Data musik telah berhasil disimpan ke 'music_data.json'")
