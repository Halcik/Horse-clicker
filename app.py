from flask import Flask, render_template, request
from main import start_sitter
import sys

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.form.get('sitter') == 'Zacznij sitterkę':
        n = request.form['konie']
        if n:
            n = int(n)
        else:
            n = 1
        v = int(request.form['vip'])
        reg = request.form['reg']
        func_sleep = request.form['sleep']
        multiplication = request.form['multiplication']
        shutdown = request.form['shutdown']
        path_project = sys.argv[0][:-7]
        print(path_project)
        start_sitter(n, v, func_sleep, multiplication, reg, shutdown, path_project)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)