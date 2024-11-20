from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de estoque
estoque = []

@app.route('/')
def home():
    return render_template('index.html', estoque=estoque)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    if nome and quantidade:
        estoque.append({"nome": nome, "quantidade": int(quantidade)})
    return redirect(url_for('home'))

@app.route('/edit/<int:index>', methods=['POST'])
def edit(index):
    novo_nome = request.form.get('novo_nome')
    nova_quantidade = request.form.get('nova_quantidade')
    
    # Atualiza apenas os campos preenchidos
    if novo_nome:
        estoque[index]["nome"] = novo_nome
    if nova_quantidade:
        try:
            estoque[index]["quantidade"] = int(nova_quantidade)
        except ValueError:
            pass  # Ignora se a quantidade não for um número válido

    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(estoque):
        del estoque[index]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
