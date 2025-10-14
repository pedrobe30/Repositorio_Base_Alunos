from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

emails = []

from views  import *


# app.add_url_rule('/', 'index', index)


if __name__ == '__main__':
    app.run()