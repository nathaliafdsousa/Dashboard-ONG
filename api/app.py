from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/doacoes', methods=['GET'])
def gerar_dados():
    meses = ["Janeiro", "Fevereiro", "Março"]
    dados = []

    for mes in meses:
        dinheiro = random.randint(5000, 15000)
        alimento = random.randint(3000, 12000)
        produtoLimpeza = random.randint(4000, 13500)
        
        # Cria a estrutura do dado
        dados.append({
            "Mês": mes, 
            "Dinheiro": dinheiro, 
            "Alimentos": alimento, 
            "Produtos de Limpeza": produtoLimpeza
        })

    return jsonify(dados)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)