
# -*- coding: utf-8 -*-
# -*- coding: cp1251 -*-
import mp3_tagger
import os
import re
main_route = os.getcwd() + '/Подборка музыки'
fds = sorted(os.listdir(main_route))
for music in fds:
    if music.endswith(('.mp3',)):
        new_name = ''
        audiofile = mp3_tagger.MP3File(main_route+"/"+music)
        tags_music = audiofile.get_tags().get('ID3TagV1')            
        if not tags_music.get('artist') or not tags_music.get('album'):
            continue
        if not tags_music.get('song'):
            new_name = music
        else:
            new_name = re.sub(r'\s+', '', (tags_music.get('artist')+'-'+tags_music.get('album')+'-'+tags_music.get('song')+'.mp3'))
        new_dir = os.getcwd() +'/Sorted_music/'+tags_music.get('artist').strip()+'/'+tags_music.get('album').strip()
        print(main_route+'/'+music)
        print(new_dir+'/'+new_name)
        new_dir = re.sub(r'[?]', '', new_dir)
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)
        os.replace(main_route+'/'+music,  re.sub(r'[?]', '', (new_dir+'/'+new_name)))