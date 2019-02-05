# This is app.py, this is the main file called.
# The app imported is the app variable from the __init__.py under the myproject directory
from myproject import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
