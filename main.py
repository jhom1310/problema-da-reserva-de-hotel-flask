from flask import Flask, jsonify, request
app = Flask(__name__)

hoteis = [
    {
    'nome' : 'Lakewood',
    'classific': 3,
    'regular' : {'t_semana': 110, 't_fim_semana': 90}, 
    'rewards': {'t_semana': 80, 't_fim_semana': 80}
    },
    {
    'nome' : 'Bridgewood',
    'classific': 4,
    'regular' : {'t_semana': 160, 't_fim_semana': 60}, 
    'rewards': {'t_semana': 110, 't_fim_semana': 50}
    },
    {
    'nome' :  'Ridgewood',
    'classific': 5,
    'regular' : {'t_semana': 220, 't_fim_semana': 150}, 
    'rewards': {'t_semana': 100, 't_fim_semana': 40}
    }
]

def calc_dias(dias):
    f_semana = 0
    semana = 0
    for dia in dias:
        if 'sat' in dia or 'sun' in dia:
            f_semana += 1
        else:
            semana += 1
    return {'f_semana' :f_semana, 'semana': semana}


def calc_valor(tipo_cliente, dias):
    # Lakewood = 0, Bridgewood = 1, Ridgewood= 2
    valores = []
    qtd_dias = calc_dias(dias)
    if tipo_cliente.upper() == 'REGULAR':
        valor_Lakewood = qtd_dias['f_semana'] * hoteis[0]['regular']['t_fim_semana'] \
            + qtd_dias['semana'] * hoteis[0]['regular']['t_semana']
        valores.append(valor_Lakewood)

        valor_Bridgewood = qtd_dias['f_semana'] * hoteis[1]['regular']['t_fim_semana'] \
            + qtd_dias['semana'] * hoteis[1]['regular']['t_semana']
        valores.append(valor_Bridgewood)

        valor_Ridgewood = qtd_dias['f_semana'] * hoteis[2]['regular']['t_fim_semana'] \
            + qtd_dias['semana'] * hoteis[2]['regular']['t_semana']
        valores.append(valor_Ridgewood)
  
        return valores

    elif tipo_cliente.upper() == 'REWARD':
        valor_Lakewood = qtd_dias['f_semana'] * hoteis[0]['rewards']['t_fim_semana'] \
            + qtd_dias['semana'] * hoteis[0]['rewards']['t_semana']
        valores.append(valor_Lakewood)

        valor_Bridgewood = qtd_dias['f_semana'] * hoteis[1]['rewards']['t_fim_semana'] \
            + qtd_dias['semana'] * hoteis[1]['rewards']['t_semana']
        valores.append(valor_Bridgewood)

        valor_Ridgewood = qtd_dias['f_semana'] * hoteis[2]['rewards']['t_fim_semana'] \
            + qtd_dias['semana'] * hoteis[2]['rewards']['t_semana']
        valores.append(valor_Ridgewood)

        return valores


def calc_barato(valores):
    menor_valor = min(valores)
    i_hoteis = []
    
    for i, v in enumerate(valores):
        if v == menor_valor:
            i_hoteis.append(i)

    hotel = hoteis[i_hoteis[-1]]['nome']

    return hotel

        

@app.route('/api/v1/cheapest/<entrada>')
def cheapest(entrada):
    try:
        strings = entrada.split(':')
        tipo_cliente = strings[0]
        datas = strings[1].split(',')

        return jsonify( {"cheapest":  calc_barato(calc_valor( tipo_cliente, datas))})
    except:
        return jsonify( {"Erro" : "Entrada inválida"} ), 400

@app.route('/api/v2/cheapest/')
def cheapest2():
    try:    
        tipo_cliente = request.args.get('cliente') 
        datas = request.args.get('datas')

        return jsonify( {"cheapest":  calc_barato(calc_valor( tipo_cliente, datas))})
    except:
        return jsonify( {"Erro" : "Entrada inválida"} ), 400

if __name__ == '__main__':
    app.run(debug=True)