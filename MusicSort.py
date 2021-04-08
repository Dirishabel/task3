
# -*- coding: utf-8 -*-
# -*- coding: cp1251 -*-
import mp3_tagger
import os
import re
import click

def mp3_redirect(music, src_dir, dst_dir):
    new_name = ''
    audiofile = mp3_tagger.MP3File(src_dir+"/"+music)
    tags_music = audiofile.get_tags().get('ID3TagV1')            
    if not tags_music.get('artist') or not tags_music.get('album'):
        continue
    if not tags_music.get('song'):
        new_name = music
    else:
        new_name = re.sub(r'\s+', '', (tags_music.get('artist')+'-'+tags_music.get('album')+'-'+tags_music.get('song')+'.mp3'))
    new_dir = dst_dir+tags_music.get('artist').strip()+'/'+tags_music.get('album').strip()
    print(src_dir+'/'+music , " -> ", new_dir+'/'+new_name)
    new_dir = re.sub(r'[?]', '', new_dir)
    if not os.path.isdir(new_dir):
        os.makedirs(new_dir)
    os.replace(main_route+'/'+music,  re.sub(r'[?]', '', (new_dir+'/'+new_name)))

@click.command()
@click.option('--src-dir', '-s', default='.', help='Sourse directory.')
@click.option('--dst-dir', '-d', default='.', help='Destination derectory.')
def main(src_dir, dst_dir ):
    print(src_dir)
    print(dst_dir)
    fds = sorted(os.listdir(src_dir))
    for music in fds:
        if music.endswith(('.mp3',)):
            try:
                mp3_redirect(music, src_dir, dst_dir)
            except:
                continue

if __name__ == "__main__":
    main()