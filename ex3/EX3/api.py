from flask import Flask,jsonify
from new.jsonhandler import show_the_write
from new.HWD import hwd

app=Flask(__name__)

@app.route('/api/printHello')
def hello():
    data=hwd()
    return jsonify(data)

@app.route('/api/modifyRecepie')
def modrec():
    data=show_the_write()
    return jsonify(data)   

if __name__=='__main__':
    app.run(debug=True)