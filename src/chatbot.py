"""
Lógica de negócio do chatbot de segurança digital
"""
from typing import List, Optional, Tuple
from .deepseek_client import DeepSeekAPIClient
from .config import SYSTEM_PROMPT


class SecurityChatbot:
    """Chatbot especializado em segurança digital para idosos"""
    
    def __init__(self):
        """Inicializa o chatbot"""
        self.client = DeepSeekAPIClient()
        self.system_prompt = SYSTEM_PROMPT
        
    def process_message(self, user_message: str, chat_history: List[List[str]]) -> Tuple[str, List[List[str]]]:
        """
        Processa uma mensagem do usuário e retorna a resposta
        
        Args:
            user_message: Mensagem do usuário
            chat_history: Histórico da conversa
            
        Returns:
            Tupla com (mensagem_vazia, histórico_atualizado)
        """
        if not user_message.strip():
            return "", chat_history
        
        # Obtém resposta da API
        response = self.client.chat_with_history(
            user_message=user_message,
            system_prompt=self.system_prompt,
            chat_history=chat_history
        )
        
        # Atualiza histórico
        chat_history.append([user_message, response])
        
        return "", chat_history
    
    def get_welcome_message(self) -> str:
        """Retorna mensagem de boas-vindas"""
        return """
        Olá! 👋 Sou seu assistente pessoal de segurança digital!
        
        Estou aqui para ajudá-lo(a) a navegar com segurança na internet. Pode me perguntar sobre:
        
        🔒 **Como criar senhas seguras**
        🎭 **Como identificar golpes online**
        🛡️ **Configurações de privacidade**
        🛒 **Compras seguras na internet**
        📱 **Uso seguro de aplicativos**
        
        Fique à vontade para fazer qualquer pergunta sobre segurança digital!
        """
    
    def get_suggested_questions(self) -> List[str]:
        """Retorna lista de perguntas sugeridas"""
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
    
    def clear_chat(self) -> Tuple[List[List[str]], str]:
        """
        Limpa o histórico de chat
        
        Returns:
            Tupla com (histórico_vazio, mensagem_de_boas_vindas)
        """
        return [], self.get_welcome_message()
