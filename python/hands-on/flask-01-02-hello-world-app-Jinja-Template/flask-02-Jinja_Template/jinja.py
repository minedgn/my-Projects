from flask import Flask, render_template #flask ve render template modulu import ediliyor.

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=34, number2=45) #render template, template kiralama.

@app.route("/mult")
def number():
    var1 = 23
    var2 = 54
    return render_template("body.html", num1 = var1, num2 = var2, sum=var1*var2)



if __name__== "__main__":
    app.run(debug=True) #port belirlemezisek default olarak 5000 de calisir.