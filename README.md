# 🛡️ Chatbot de Segurança Digital para Idosos

Um assistente virtual especializado em segurança da informação, desenvolvido especialmente para o público idoso, com interface simples e intuitiva.

## 🎯 Funcionalidades

- **Interface Amigável**: Botões grandes, texto legível e navegação simples
- **Especialista em Segurança**: Foco em proteção digital para idosos
- **Conversação Natural**: Linguagem clara e didática
- **Perguntas Sugeridas**: Tópicos comuns pré-configurados
- **Histórico de Conversa**: Mantém contexto da conversa

## 🏗️ Arquitetura do Projeto

```
chatbot-seguranca-digital/
├── app.py                    # Versão Gradio original
├── app_streamlit.py         # Versão Streamlit (deploy fácil)
├── app_flask.py            # Versão Flask (mais flexível)
├── src/                    # Módulos organizados
│   ├── __init__.py        # Inicialização do pacote
│   ├── config.py          # Configurações centralizadas
│   ├── deepseek_client.py # Cliente da API DeepSeek
│   ├── chatbot.py         # Lógica do chatbot
│   └── interface.py       # Interface Gradio
├── templates/             # Templates HTML (Flask)
│   └── index.html        # Interface web responsiva
├── .streamlit/           # Configuração Streamlit
│   └── config.toml       # Tema e configurações
├── requirements*.txt     # Dependências por versão
├── Procfile             # Deploy Heroku/Render
├── runtime.txt          # Versão Python
├── DEPLOY.md           # Guia completo de deploy
└── README.md           # Este arquivo
```

## 🚀 Como Executar

### Desenvolvimento Local

#### 1. Instalar Dependências

```bash
# Para versão Streamlit (recomendada)
pip install -r requirements-streamlit.txt

# Para versão Flask
pip install -r requirements-flask.txt
```

#### 2. Configurar Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua API key do DeepSeek
DEEPL_API_KEY=sua_api_key_aqui
```

#### 3. Executar a Aplicação

```bash
# Versão Streamlit (interface mais simples para idosos)
streamlit run app_streamlit.py

# Versão Flask (mais customizável)
python app_flask.py

# Versão Gradio original
python app.py
```

### 🌐 Deploy Gratuito

**Opções disponíveis:**

1. **[Streamlit Cloud](https://share.streamlit.io)** - Mais fácil (Recomendado)
2. **[Render](https://render.com)** - Flask, mais flexível  
3. **[Railway](https://railway.app)** - Deploy rápido
4. **[Hugging Face Spaces](https://huggingface.co/spaces)** - Ideal para IA

**📋 Veja o guia completo:** [`DEPLOY.md`](DEPLOY.md)

A interface será aberta automaticamente no navegador em `http://localhost:8501` (Streamlit) ou `http://localhost:5000` (Flask)

## 🔧 Configurações

### Interface

O arquivo `src/config.py` contém todas as configurações da interface:

- **Tamanho de fontes**: Otimizado para leitura fácil
- **Cores e tema**: Design amigável para idosos
- **Botões**: Grandes e com ícones explicativos
- **Espaçamento**: Generoso para facilitar navegação

### API DeepSeek

- **Modelo**: `deepseek-chat`
- **Temperatura**: 0.7 (balanceada)
- **Max tokens**: 1000
- **Timeout**: 30 segundos

## 🎯 Especialidades do Assistente

O chatbot é especializado em:

- 🔐 **Senhas Seguras**: Como criar e gerenciar
- 🎭 **Identificação de Golpes**: Phishing, fake news, etc.
- 🛡️ **Privacidade**: Configurações em redes sociais
- 🛒 **Compras Online**: Práticas seguras
- 📱 **Aplicativos**: Uso seguro de WhatsApp, Facebook, etc.
- 🌐 **Navegação Web**: Sites confiáveis, Wi-Fi público
- 🦠 **Proteção**: Antivírus e malware

## 🔒 Segurança e Privacidade

- **Não coleta dados pessoais**: Nenhuma informação é armazenada
- **Conexão segura**: Comunicação criptografada com a API
- **Sem logs**: Conversas não são registradas
- **Orientações éticas**: Nunca solicita senhas ou dados bancários

## 🛠️ Desenvolvimento

### Estrutura Modular

O projeto foi desenvolvido com foco na modularidade:

- **`config.py`**: Centralizatonas configurações
- **`deepseek_client.py`**: Isolamento da lógica de API
- **`chatbot.py`**: Regras de negócio do assistente
- **`interface.py`**: Separação da camada de apresentação

### Extensibilidade

Para adicionar novas funcionalidades:

1. **Novos prompts**: Edite `SYSTEM_PROMPT` em `config.py`
2. **Perguntas sugeridas**: Modifique `get_suggested_questions()` em `chatbot.py`
3. **Estilo da interface**: Ajuste `INTERFACE_CONFIG` em `config.py`
4. **Lógica personalizada**: Estenda a classe `SecurityChatbot`

## 📋 Dependências

- **gradio**: Interface web interativa
- **requests**: Comunicação com API REST
- **python-dotenv**: Gerenciamento de variáveis de ambiente

---

**⚠️ Aviso**: Este assistente oferece orientações gerais sobre segurança digital. Para situações específicas ou urgentes, consulte um especialista em tecnologia.
