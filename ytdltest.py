import os
import re
import subprocess

link = 'https://www.youtube.com/watch?v=214-gNHIoPk'

# Download Youtube video as mp3

cmds = ['youtube-dl',
        '-f',
        'bestaudio',
        '--restrict-filenames',
        '--extract-audio',
        '--audio-format',
        'mp3',
        link]

subprocess.Popen(cmds).wait()
