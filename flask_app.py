'''
--------------------------------------------------------------------------------
instructor's note:
in the console, set the FLASK_APP variable to our new file:
export FLASK_APP=flask_app.py
( no spaces around the =!, also be in the git bash terminal!)
Students using the DOS prompt; must type
set FLASK_APP=flask_app.py
Running on http://127.0.0.1:5000

--------------------------------------------------------------------------------
'''

from flask import Flask, render_template


app=Flask(__name__, static_url_path='/static')
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
