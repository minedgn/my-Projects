from flask import Flask 

app = Flask(__name__) 

@app.route('/') 
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return 'Hayat kisa, kuslar ucuyor!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>') #forth dan sonra hangi sayiyi yazarsak bize onun id numarasini verir.
def forth(id):
    return f'Id number of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True, port=2000)