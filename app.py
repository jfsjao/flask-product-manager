from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os produtos cadastrados
produtos = []

@app.route('/')
def listagem():
    # Ordenar os produtos pelo valor, do menor para o maior
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('listagem.html', produtos=produtos_ordenados)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        try:
            # Receber os dados do formulário
            nome = request.form['nome'].strip()
            descricao = request.form['descricao'].strip()
            valor = float(request.form['valor'])
            disponivel = request.form['disponivel'].strip().lower() == 'sim'

            if not nome or not descricao or valor < 0:
                raise ValueError("Dados inválidos fornecidos.")

            # Adicionar o produto na lista
            produtos.append({
                'nome': nome,
                'descricao': descricao,
                'valor': valor,
                'disponivel': disponivel
            })

            # Redirecionar para a página de listagem
            return redirect(url_for('listagem'))
        except ValueError as e:
            return render_template('cadastrar.html', error=str(e))

    return render_template('cadastrar.html', error=None)

if __name__ == "__main__":
    app.run(debug=True)
