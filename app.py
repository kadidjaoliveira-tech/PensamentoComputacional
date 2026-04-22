from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Endpoint para realizar cálculos.
    Espera um JSON com 'num1', 'num2' e 'operation'
    """
    try:
        data = request.get_json()
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation')
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({'error': 'Divisão por zero não é permitida'}), 400
            result = num1 / num2
        elif operation == '%':
            if num2 == 0:
                return jsonify({'error': 'Módulo por zero não é permitido'}), 400
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        else:
            return jsonify({'error': 'Operação inválida'}), 400
        
        return jsonify({
            'num1': num1,
            'num2': num2,
            'operation': operation,
            'result': result
        }), 200
    
    except (ValueError, TypeError):
        return jsonify({'error': 'Números inválidos'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Verificar se a API está funcionando"""
    return jsonify({'status': 'API de Calculadora funcionando'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000