"""
Interface Streamlit para o Chatbot de Segurança Digital
Versão otimizada para deploy gratuito
"""
import streamlit as st
import os
import sys
from typing import List

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.deepseek_client import DeepSeekAPIClient
from src.config import SYSTEM_PROMPT


class StreamlitChatbot:
    """Chatbot usando Streamlit"""
    
    def __init__(self):
        """Inicializa o chatbot"""
        self.client = None
        self.setup_page()
        self.initialize_client()
    
    def setup_page(self):
        """Configura a página do Streamlit"""
        st.set_page_config(
            page_title="🛡️ Assistente de Segurança Digital",
            page_icon="🛡️",
            layout="wide",
            initial_sidebar_state="collapsed"
        )
        
        # CSS personalizado para idosos
        st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            font-size: 3rem !important;
            color: #2c3e50 !important;
            text-align: center !important;
            margin-bottom: 1rem !important;
        }
        .stMarkdown {
            font-size: 1.2rem !important;
            line-height: 1.6 !important;
        }
        .stTextInput > div > div > input {
            font-size: 1.3rem !important;
            padding: 1rem !important;
            border-radius: 10px !important;
        }
        .stButton > button {
            font-size: 1.2rem !important;
            padding: 0.8rem 2rem !important;
            border-radius: 10px !important;
            font-weight: bold !important;
            margin: 0.5rem !important;
            width: 100% !important;
        }
        .stChatMessage {
            font-size: 1.1rem !important;
            padding: 1rem !important;
            margin: 0.5rem 0 !important;
        }
        .chat-container {
            max-height: 400px;
            overflow-y: auto;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
        }
        .suggestion-button {
            background-color: #f8f9fa;
            border: 2px solid #007bff;
            color: #007bff;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            font-size: 1.1rem;
        }
        .suggestion-button:hover {
            background-color: #007bff;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    
    def initialize_client(self):
        """Inicializa o cliente da API"""
        try:
            if not os.getenv("DEEPL_API_KEY"):
                st.error("⚠️ Configure a variável de ambiente DEEPL_API_KEY")
                st.stop()
            
            self.client = DeepSeekAPIClient()
            
        except Exception as e:
            st.error(f"❌ Erro ao conectar com a API: {e}")
            st.stop()
    
    def get_suggested_questions(self) -> List[str]:
        """Retorna perguntas sugeridas"""
        return [
            "Como criar uma senha segura?",
            "Como identificar mensagens falsas no WhatsApp?",
            "É seguro fazer compras online?",
            "Como proteger meus dados no Facebook?",
            "O que é phishing e como me proteger?",
            "Como saber se um site é confiável?",
            "Posso usar Wi-Fi público com segurança?",
            "Como proteger meu celular de vírus?"
        ]
    
    def display_welcome(self):
        """Exibe mensagem de boas-vindas"""
        st.markdown("""
        <div style="background-color: #e8f5e8; padding: 2rem; border-radius: 15px; margin: 1rem 0;">
            <h2 style="color: #2c5e2c; text-align: center;">👋 Olá! Bem-vindo(a)!</h2>
            <p style="font-size: 1.3rem; text-align: center; color: #2c5e2c;">
                Sou seu assistente pessoal de segurança digital!<br>
                Estou aqui para ajudá-lo(a) a navegar com segurança na internet.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def display_suggestions(self):
        """Exibe perguntas sugeridas"""
        st.markdown("### 💡 Perguntas Frequentes")
        st.markdown("*Clique em uma pergunta para começar:*")
        
        suggestions = self.get_suggested_questions()
        
        # Organiza em 2 colunas
        col1, col2 = st.columns(2)
        
        for i, suggestion in enumerate(suggestions):
            col = col1 if i % 2 == 0 else col2
            
            with col:
                if st.button(suggestion, key=f"suggestion_{i}"):
                    st.session_state.current_question = suggestion
                    st.rerun()
    
    def display_chat(self):
        """Exibe o chat"""
        # Inicializa o histórico se não existir
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Container para o chat
        chat_container = st.container()
        
        with chat_container:
            # Exibe mensagens do histórico
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
        
        # Input para nova mensagem
        user_input = st.chat_input("Digite sua pergunta sobre segurança digital...")
        
        # Processa pergunta sugerida
        if "current_question" in st.session_state:
            user_input = st.session_state.current_question
            del st.session_state.current_question
        
        # Processa mensagem do usuário
        if user_input:
            # Adiciona mensagem do usuário
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            with st.chat_message("user"):
                st.markdown(user_input)
            
            # Gera resposta do assistente
            with st.chat_message("assistant"):
                with st.spinner("🤔 Pensando na melhor resposta..."):
                    try:
                        response = self.client.chat_with_history(
                            user_message=user_input,
                            system_prompt=SYSTEM_PROMPT,
                            chat_history=[(msg["content"], "") for msg in st.session_state.messages[:-1:2]]
                        )
                        
                        st.markdown(response)
                        
                        # Adiciona resposta ao histórico
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        
                    except Exception as e:
                        error_msg = "Desculpe, estou com dificuldades para responder neste momento. Tente novamente em alguns instantes."
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    def display_sidebar(self):
        """Exibe barra lateral com controles"""
        with st.sidebar:
            st.markdown("### 🛠️ Controles")
            
            if st.button("🔄 Nova Conversa", type="secondary"):
                st.session_state.messages = []
                st.rerun()
            
            st.markdown("---")
            st.markdown("### ℹ️ Sobre")
            st.markdown("""
            Este assistente oferece orientações gerais sobre segurança digital.
            
            **⚠️ Importante:**
            - Nunca compartilhe senhas ou dados pessoais
            - Para situações urgentes, procure ajuda especializada
            """)
    
    def run(self):
        """Executa a aplicação"""
        # Título principal
        st.title("🛡️ Assistente de Segurança Digital")
        st.markdown("*Seu guia pessoal para navegar com segurança na internet*")
        
        # Barra lateral
        self.display_sidebar()
        
        # Se não há mensagens, exibe boas-vindas e sugestões
        if "messages" not in st.session_state or len(st.session_state.messages) == 0:
            self.display_welcome()
            self.display_suggestions()
            st.markdown("---")
        
        # Chat principal
        self.display_chat()
        
        # Rodapé
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 1rem;">
            💙 Desenvolvido com carinho para o público idoso<br>
            🛡️ Sua segurança digital é nossa prioridade
        </div>
        """, unsafe_allow_html=True)


def main():
    """Função principal"""
    chatbot = StreamlitChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
