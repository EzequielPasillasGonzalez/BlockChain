from flask import Flask
from flask import render_template
from flask import request

from block import write_block, check_integrity

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        vendedor = request.form.get('vendedor')
        comprador = request.form.get('comprador')
        cantidad = request.form.get('cantidad')
        
        write_block(vendedor = vendedor, comprador = comprador, montoCompra = cantidad)
    return render_template('index.html')

@app.route('/checking')
def check():
    results = check_integrity()
    print(results)
    return render_template('index.html', checking_results=results)

if __name__ == '__main__':
    app.run(debug=True)