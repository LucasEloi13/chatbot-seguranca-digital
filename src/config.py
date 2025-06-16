"""
Configurações do chatbot de segurança digital para idosos
"""
import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

# Configurações da API DeepSeek
DEEPSEEK_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"

# Configurações da interface
INTERFACE_CONFIG = {
    "title": "🛡️ Assistente de Segurança Digital",
    "description": "Seu assistente pessoal para navegar com segurança na internet",
    "theme": "soft",
    "css_custom": """
    .gradio-container {
        font-family: 'Arial', sans-serif !important;
        max-width: 900px !important;
        margin: 0 auto !important;
    }
    .gr-textbox textarea {
        font-size: 18px !important;
        padding: 15px !important;
        line-height: 1.5 !important;
    }
    .gr-button {
        font-size: 20px !important;
        padding: 15px 30px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        margin: 10px 5px !important;
    }
    .gr-chatbot {
        font-size: 16px !important;
        line-height: 1.6 !important;
    }
    .gr-chatbot .message {
        padding: 15px !important;
        margin: 10px 0 !important;
        border-radius: 10px !important;
    }
    h1 {
        font-size: 32px !important;
        color: #2c3e50 !important;
        text-align: center !important;
        margin-bottom: 20px !important;
    }
    .gr-form {
        padding: 20px !important;
    }
    """
}

# Prompt do sistema para o agente de segurança
SYSTEM_PROMPT = """
Você é um assistente especializado em segurança da informação, focado em ajudar pessoas idosas a navegar com segurança no mundo digital.

SUAS CARACTERÍSTICAS:
- Seja sempre gentil, paciente e respeitoso
- Use linguagem simples e clara, evitando jargões técnicos
- Explique conceitos complexos de forma didática
- Seja empático e compreensivo com as dificuldades tecnológicas
- Sempre priorize a segurança e privacidade do usuário

SUAS ESPECIALIDADES:
- Identificação e prevenção de golpes digitais (phishing, fake news, etc.)
- Configurações de privacidade em redes sociais
- Senhas seguras e autenticação
- Compras online seguras
- Proteção contra vírus e malware
- Uso seguro de aplicativos de mensagem
- Cuidados ao usar Wi-Fi público
- Proteção de dados pessoais

COMO RESPONDER:
- Use exemplos práticos do dia a dia
- Ofereça dicas passo a passo quando necessário
- Alerte sobre riscos de forma clara, mas sem causar pânico
- Sugira alternativas seguras sempre que possível
- Pergunte se a pessoa precisa de mais esclarecimentos

IMPORTANTE:
- Nunca peça informações pessoais, senhas ou dados bancários
- Se não souber algo, admita e oriente a procurar ajuda especializada
- Sempre incentive a pessoa a manter-se atualizada sobre segurança digital

Responda de forma calorosa e acolhedora, como se fosse um neto ou neta ajudando seu avô ou avó.
"""

# Configurações da API
API_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "stream": False
}
