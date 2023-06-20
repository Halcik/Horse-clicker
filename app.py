from flask import Flask, render_template, request
from start import start_sitter

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
        print(n, type(n))
        start_sitter(n, v, func_sleep, multiplication, reg, shutdown)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)