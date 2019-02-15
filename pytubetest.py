from pytube import YouTube
import os
import re
import subprocess

# link = 'https://www.youtube.com/watch?v=214-gNHIoPk'


def ytmp3downloader(link):
    yt = YouTube(link)
    t = yt.streams.filter(only_audio=True).order_by('abr').desc().all()
    filename = t[0].default_filename.encode('ascii', errors='ignore').decode()
    s = str(filename).strip().replace(' ', '_')
    cleaned_filename = re.sub(r'(?u)[^-\w.]', '', s)
    output_dir = os.path.expanduser('~/Downloads')
    title = os.path.splitext(cleaned_filename)[0]
    abs_path = os.path.join(output_dir, cleaned_filename)

    if os.path.isfile(abs_path):
        print(f'{abs_path} already exists. Aborting download!')
        exit(0)

    # Downloading original YouTube audio
    print('Downloading original YouTube audio')
    print(f'Original YouTube audio Filename: {abs_path}')
    t[0].download(output_path=output_dir, filename=title)
    print('Download successful!')

    # Converting to MP3
    print('Converting to MP3..')
    new_filename = os.path.splitext(abs_path)[0] + '.mp3'
    if os.path.isfile(new_filename):
        print(f'{new_filename} already exists!')
        exit(0)
    else:
        cmds = ['ffmpeg', '-i', abs_path, new_filename]
        subprocess.Popen(cmds).wait()
        print('MP3 conversion successful!')
        print(f'New file name: {new_filename}')
        print('Deleting original file.')
        os.remove(abs_path)
        print(f'{abs_path} deleted!')

        return new_filename


if __name__ == '__main__':
    ytmp3downloader('https://www.youtube.com/watch?v=214-gNHIoPk')
