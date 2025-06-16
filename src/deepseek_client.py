"""
Cliente para conexão com a API do DeepSeek
"""
import requests
import json
from typing import List, Dict, Any, Optional
from .config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL, DEEPSEEK_MODEL, API_CONFIG


class DeepSeekAPIClient:
    """Cliente para interagir com a API do DeepSeek"""
    
    def __init__(self):
        """Inicializa o cliente da API"""
        if not DEEPSEEK_API_KEY:
            raise ValueError("DEEPSEEK_API_KEY não encontrada nas variáveis de ambiente")
        
        self.api_key = DEEPSEEK_API_KEY
        self.api_url = DEEPSEEK_API_URL
        self.model = DEEPSEEK_MODEL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def send_message(self, messages: List[Dict[str, str]]) -> Optional[str]:
        """
        Envia mensagens para a API do DeepSeek
        
        Args:
            messages: Lista de mensagens no formato [{"role": "user", "content": "..."}]
            
        Returns:
            Resposta da API ou None em caso de erro
        """
        try:
            payload = {
                "model": self.model,
                "messages": messages,
                **API_CONFIG
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            
            data = response.json()
            return data['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição à API: {e}")
            return None
        except KeyError as e:
            print(f"Erro ao processar resposta da API: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None
    
    def chat(self, user_message: str, system_prompt: str) -> Optional[str]:
        """
        Envia uma mensagem do usuário com prompt do sistema
        
        Args:
            user_message: Mensagem do usuário
            system_prompt: Prompt do sistema com instruções
            
        Returns:
            Resposta da API ou mensagem de erro
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        response = self.send_message(messages)
        
        if response is None:
            return "Desculpe, estou com dificuldades para responder neste momento. Por favor, tente novamente em alguns instantes."
        
        return response
    
    def chat_with_history(self, user_message: str, system_prompt: str, chat_history: List[List[str]]) -> Optional[str]:
        """
        Envia mensagem considerando o histórico de conversa
        
        Args:
            user_message: Nova mensagem do usuário
            system_prompt: Prompt do sistema
            chat_history: Histórico da conversa no formato Gradio
            
        Returns:
            Resposta da API
        """
        messages = [{"role": "system", "content": system_prompt}]
        
        # Adiciona histórico de conversa
        for user_msg, assistant_msg in chat_history:
            if user_msg:
                messages.append({"role": "user", "content": user_msg})
            if assistant_msg:
                messages.append({"role": "assistant", "content": assistant_msg})
        
        # Adiciona nova mensagem
        messages.append({"role": "user", "content": user_message})
        
        response = self.send_message(messages)
        
        if response is None:
            return "Desculpe, estou com dificuldades para responder neste momento. Por favor, tente novamente em alguns instantes."
        
        return response
