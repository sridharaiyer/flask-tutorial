from ytdlproject import app
from flask import render_template, url_for, redirect
from ytdlproject.forms import DownloadMP3
from pytubetest import ytmp3downloader


@app.route('/', methods=['GET', 'POST'])
def downloadmp3():
    form = DownloadMP3()

    if form.validate_on_submit():
        url = form.videourl.data
        mp3filename = ytmp3downloader(url)

        return redirect(url_for('listdownload', filename=mp3filename))

    return render_template('index.html', form=form)


@app.route('/listdownload')
def listdownload(filename=None):
    return render_template('listdownload.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
