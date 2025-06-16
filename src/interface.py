"""
Interface do usuário usando Gradio
"""
import gradio as gr
from typing import List, Tuple
from .chatbot import SecurityChatbot
from .config import INTERFACE_CONFIG


class ChatInterface:
    """Interface do chatbot usando Gradio"""
    
    def __init__(self):
        """Inicializa a interface"""
        self.chatbot = SecurityChatbot()
        self.interface = None
        
    def create_interface(self) -> gr.Blocks:
        """Cria a interface do Gradio"""
        
        with gr.Blocks(
            title=INTERFACE_CONFIG["title"],
            theme=gr.themes.Soft(),
            css=INTERFACE_CONFIG["css_custom"]
        ) as interface:
            
            # Título
            gr.Markdown(f"# {INTERFACE_CONFIG['title']}")
            gr.Markdown(f"*{INTERFACE_CONFIG['description']}*")
            
            # Chatbot principal
            chatbot_component = gr.Chatbot(
                value=[[None, self.chatbot.get_welcome_message()]],
                height=500,
                show_label=False,
                avatar_images=["👤", "🤖"]
            )
            
            # Área de input
            with gr.Row():
                with gr.Column(scale=4):
                    msg_input = gr.Textbox(
                        placeholder="Digite sua pergunta sobre segurança digital...",
                        show_label=False,
                        container=False
                    )
                with gr.Column(scale=1):
                    send_btn = gr.Button("Enviar 📤", variant="primary")
            
            # Botões de ação
            with gr.Row():
                clear_btn = gr.Button("🔄 Nova Conversa", variant="secondary")
                
            # Perguntas sugeridas
            gr.Markdown("### 💡 Perguntas Frequentes")
            suggestions = self.chatbot.get_suggested_questions()
            
            # Cria botões para as perguntas sugeridas
            suggestion_buttons = []
            for i in range(0, len(suggestions), 2):
                with gr.Row():
                    if i < len(suggestions):
                        btn1 = gr.Button(suggestions[i], variant="outline")
                        suggestion_buttons.append((btn1, suggestions[i]))
                    if i + 1 < len(suggestions):
                        btn2 = gr.Button(suggestions[i + 1], variant="outline")
                        suggestion_buttons.append((btn2, suggestions[i + 1]))
            
            # Configura eventos dos botões de sugestão
            for btn, suggestion_text in suggestion_buttons:
                btn.click(
                    fn=lambda text=suggestion_text: (text, []),
                    outputs=[msg_input]
                )
            
            # Eventos
            send_btn.click(
                fn=self._handle_message,
                inputs=[msg_input, chatbot_component],
                outputs=[msg_input, chatbot_component]
            )
            
            msg_input.submit(
                fn=self._handle_message,
                inputs=[msg_input, chatbot_component],
                outputs=[msg_input, chatbot_component]
            )
            
            clear_btn.click(
                fn=self._clear_chat,
                outputs=[chatbot_component, msg_input]
            )
            
            # Rodapé
            gr.Markdown("""
            ---
            **⚠️ Lembre-se:** Este assistente oferece orientações gerais sobre segurança digital. 
            Para situações específicas ou urgentes, consulte um especialista em tecnologia.
            """)
        
        self.interface = interface
        return interface
    
    def _handle_message(self, user_message: str, chat_history: List[List[str]]) -> Tuple[str, List[List[str]]]:
        """Processa mensagem do usuário"""
        return self.chatbot.process_message(user_message, chat_history)
    
    def _clear_chat(self) -> Tuple[List[List[str]], str]:
        """Limpa o chat"""
        history, welcome_msg = self.chatbot.clear_chat()
        return [[None, welcome_msg]], ""
    
    def launch(self, **kwargs):
        """Lança a interface"""
        if self.interface is None:
            self.create_interface()
        
        return self.interface.launch(**kwargs)
