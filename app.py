"""
Chatbot de Segurança Digital para Idosos
Aplicação principal que inicializa o chatbot especializado
"""
import sys
import os

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.interface import ChatInterface


def main():
    """Função principal da aplicação"""
    print("🛡️ Iniciando Assistente de Segurança Digital...")
    print("📱 Preparando interface para o público idoso...")
    
    try:
        # Cria e lança a interface
        chat_interface = ChatInterface()
        chat_interface.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,
            inbrowser=True
        )
        
    except KeyboardInterrupt:
        print("\n👋 Assistente encerrado pelo usuário.")
    except Exception as e:
        print(f"❌ Erro ao iniciar o assistente: {e}")
        print("Verifique se todas as dependências estão instaladas e a API key está configurada.")


if __name__ == "__main__":
    main()
