from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        # Si els camps estan buits, torna un missatge per evitar errors
        if not name or not age:
            return "Els camps no poden estar buits!."
        return f"Hola, {name}, tens {age} anys!"

    # Aquesta resposta s'envia si la petició no és POST
    return '''
    <form method="post">
        Nom: <input type="text" name="name"><br>
        Edat: <input type="text" name="age"><br>
        <input type="submit" value="Enviar">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
       app.run(debug=True)
   
