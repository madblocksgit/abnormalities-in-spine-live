from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
 return(render_template('index.html'))

@app.route('/madhu')
def madhu():
 return(render_template('madhu.html'))

@app.route('/result')
def maddy_result():
 k='Everything is Normal'
 return(render_template('result.html',output=k))


if __name__=="__main__":
 app.run()