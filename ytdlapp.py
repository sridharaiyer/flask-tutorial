from ytdlproject import app
from flask import render_template,url_for,redirect
from ytdlproject.forms import DownloadMP3


@app.route('/')
def index():
    mp3name = ''
    return render_template('index.html',mp3name=mp3name)

@app.route('/downloadmp3',methods=['GET','POST'])
def downloadmp3():
    form = DownloadMP3()

    if form.validate_on_submit():
        url = form.videourl.data

        return redirect(url_for('index'))

    return render_template('downloadmp3.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
