"""
Interface Flask para o Chatbot de Segurança Digital
Versão web responsiva para deploy gratuito
"""
from flask import Flask, render_template, request, jsonify, session
import os
import sys
import uuid
from datetime import datetime

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.deepseek_client import DeepSeekAPIClient
from src.config import SYSTEM_PROMPT

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'chatbot-seguranca-digital-2025')

# Cliente global da API
client = None

def get_client():
    """Obtém instância do cliente da API"""
    global client
    if client is None:
        try:
            client = DeepSeekAPIClient()
        except Exception as e:
            print(f"Erro ao inicializar cliente: {e}")
    return client

@app.route('/')
def index():
    """Página principal"""
    # Inicializa sessão se necessário
    if 'chat_id' not in session:
        session['chat_id'] = str(uuid.uuid4())
        session['messages'] = []
    
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint para processar mensagens"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Mensagem vazia'}), 400
        
        # Obtém cliente da API
        api_client = get_client()
        if not api_client:
            return jsonify({'error': 'Erro de conexão com a API'}), 500
        
        # Obtém histórico da sessão
        chat_history = session.get('messages', [])
        
        # Converte para formato esperado pela API
        history_for_api = []
        for msg in chat_history:
            if msg['role'] == 'user':
                history_for_api.append([msg['content'], ''])
            elif msg['role'] == 'assistant' and history_for_api:
                history_for_api[-1][1] = msg['content']
        
        # Gera resposta
        response = api_client.chat_with_history(
            user_message=user_message,
            system_prompt=SYSTEM_PROMPT,
            chat_history=history_for_api
        )
        
        # Atualiza histórico da sessão
        session['messages'].append({
            'role': 'user',
            'content': user_message,
            'timestamp': datetime.now().isoformat()
        })
        
        session['messages'].append({
            'role': 'assistant',
            'content': response,
            'timestamp': datetime.now().isoformat()
        })
        
        session.modified = True
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Erro no chat: {e}")
        return jsonify({
            'error': 'Erro interno do servidor',
            'response': 'Desculpe, estou com dificuldades para responder neste momento. Tente novamente em alguns instantes.'
        }), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    """Limpa o histórico do chat"""
    session['messages'] = []
    session.modified = True
    return jsonify({'status': 'success'})

@app.route('/suggestions')
def get_suggestions():
    """Retorna perguntas sugeridas"""
    suggestions = [
        "Como criar uma senha segura?",
        "Como identificar mensagens falsas no WhatsApp?",
        "É seguro fazer compras online?",
        "Como proteger meus dados no Facebook?",
        "O que é phishing e como me proteger?",
        "Como saber se um site é confiável?",
        "Posso usar Wi-Fi público com segurança?",
        "Como proteger meu celular de vírus?"
    ]
    return jsonify({'suggestions': suggestions})

@app.route('/health')
def health_check():
    """Endpoint de verificação de saúde"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'api_connected': client is not None
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
