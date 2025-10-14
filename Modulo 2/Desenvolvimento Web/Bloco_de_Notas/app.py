from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

BANCO_DE_DADOS = "bloco_de_notas.db"

def get_db():
    db = sqlite3.connect(BANCO_DE_DADOS)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())


@app.route('/')
def index():
    init_db()
    return render_template('index.html')

@app.route('/notas', methods=["GET"])
def get_notas():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT * FROM anotacoes')
        dados = cur.fetchall()
        return render_template('index.html', data=[dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        db.close()

@app.route('/notas', methods=["GET", "POST"])
def notas():
    if request.method == 'GET':
        return get_notas
    elif request.method == 'POST':
        anotacao = request.form.get('anotacao')

        if not anotacao:
            return jsonify({'error': 'Anotacão é obrigatorio'}), 400
        try:
            db = get_db()
            cur = db.cursor()
            cur.execute("INSERT INTO anotacoes (texto, data_hora)" + "VALUES (?, datetime('now'))", (anotacao,))
            db.commit()
            return render_template('index.html')
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}),500