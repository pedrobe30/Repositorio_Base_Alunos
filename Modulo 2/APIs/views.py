from  app import  app, request, jsonify, render_template, emails

# @app.route('/example', methods=['GET', 'POST'])
# def example():
#     if request.method =='GET':
#         return jsonify({"message": "Este é um Corpo (body) de uma requisição GET"})
#     elif request.method =='POST':
#         data = request.json
#         return jsonify({"message": "esta é uma requisição POST!", "data": data})
    
# @app.route('/example/2', methods=['GET'])
# def test():
#     return jsonify({"message": "FUNCIONOU, True",})

# @app.route('/<numero>')
# def num(numero):
#     return render_template("index.html", numero=numero)

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        print(nome)
        
        email = request.form.get('email')
        if email in emails:
            return f"Error: email já cadastrado"
        else:
            emails.append(email)
            print(emails)
        
        senha = request.form.get('senha')
        print(senha)

        

        return f"<h1>Username: {nome} foi recebido com o Email: {email} </h1>"
    
    
    else:
        return render_template('form.html')
        
    
