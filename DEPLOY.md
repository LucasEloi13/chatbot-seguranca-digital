# 🚀 Guia de Deploy Gratuito

Este guia mostra como fazer deploy gratuito do Chatbot de Segurança Digital em diferentes plataformas.

## 📋 Resumo das Opções

| Plataforma | Versão | Prós | Contras | Limite |
|------------|--------|------|---------|---------|
| **Streamlit Cloud** | `app_streamlit.py` | Muito fácil, interface nativa | Streamlit apenas | 1 app pública |
| **Render** | `app_flask.py` | Flexível, Flask completo | Setup manual | 750h/mês |
| **Railway** | `app_flask.py` | Fácil deploy, boa performance | Limite de uso | $5/mês grátis |
| **Hugging Face** | `app_streamlit.py` | Ideal para IA, boa visibilidade | Foco em ML | Ilimitado |

## 🎯 Recomendações por Caso

### Para Demonstração Rápida
**Streamlit Cloud** - Mais fácil e rápido

### Para Uso Profissional
**Render** - Mais estável e customizável

### Para Comunidade de IA
**Hugging Face Spaces** - Melhor exposição

---

## 🔧 1. Streamlit Cloud (Recomendado)

### Preparação
```bash
# Use esta versão
cp app_streamlit.py app.py
cp requirements-streamlit.txt requirements.txt
```

### Deploy
1. **Envie para GitHub**
   ```bash
   git add .
   git commit -m "Deploy Streamlit"
   git push origin main
   ```

2. **Acesse [share.streamlit.io](https://share.streamlit.io)**

3. **Conecte seu repositório GitHub**

4. **Configure as variáveis de ambiente:**
   - `DEEPL_API_KEY` = sua_api_key_deepseek

5. **Deploy automático!** 🎉

### Exemplo de URL
`https://usuario-chatbot-seguranca-digital-app-xxx.streamlit.app`

---

## 🌐 2. Render (Flask)

### Preparação
```bash
# Use esta versão
cp app_flask.py app.py
cp requirements-flask.txt requirements.txt
```

### Deploy
1. **Acesse [render.com](https://render.com)**

2. **Conecte seu repositório GitHub**

3. **Crie um Web Service:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3

4. **Configure variáveis de ambiente:**
   - `DEEPL_API_KEY` = sua_api_key_deepseek
   - `SECRET_KEY` = uma_chave_secreta_qualquer

5. **Deploy automático!** 🎉

### Exemplo de URL
`https://chatbot-seguranca-digital.onrender.com`

---

## 🚂 3. Railway (Flask)

### Deploy
1. **Instale Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login e deploy:**
   ```bash
   railway login
   railway init
   railway add
   railway deploy
   ```

3. **Configure variáveis:**
   ```bash
   railway variables set DEEPL_API_KEY=sua_api_key
   railway variables set SECRET_KEY=chave_secreta
   ```

---

## 🤗 4. Hugging Face Spaces

### Preparação
```bash
# Renomeie arquivos
cp app_streamlit.py app.py
cp requirements-streamlit.txt requirements.txt
cp README_HF.md README.md
```

### Deploy
1. **Acesse [huggingface.co/spaces](https://huggingface.co/spaces)**

2. **Crie um novo Space:**
   - **SDK:** Streamlit
   - **Hardware:** CPU básico (gratuito)

3. **Upload dos arquivos ou conecte GitHub**

4. **Configure secrets:**
   - `DEEPL_API_KEY` = sua_api_key_deepseek

### Exemplo de URL
`https://huggingface.co/spaces/usuario/chatbot-seguranca-digital`

---

## 🔐 Configuração da API Key

### Obter API Key DeepSeek
1. Acesse [platform.deepseek.com](https://platform.deepseek.com)
2. Crie uma conta
3. Gere uma API key
4. **Importante:** Mantenha segura!

### Configurar nos Serviços
- **Streamlit Cloud:** Settings → Secrets
- **Render:** Environment → Environment Variables  
- **Railway:** Variables
- **Hugging Face:** Settings → Repository secrets

---

## 🎨 Customização para Deploy

### Streamlit
```python
# app_streamlit.py já está otimizado
# Personalize em src/config.py
```

### Flask
```python
# app_flask.py já está pronto para produção
# Templates em templates/index.html
```

### Variáveis de Ambiente
```bash
# .env (desenvolvimento local)
DEEPL_API_KEY=sua_api_key_aqui
SECRET_KEY=chave_secreta_para_flask

# PORT (automático na maioria dos serviços)
PORT=5000
```

---

## 🔧 Solução de Problemas

### Erro de Import
```bash
# Verifique se os requirements estão corretos
pip install -r requirements.txt
```

### Erro de API Key
```bash
# Teste localmente primeiro
python test_chatbot.py
```

### Problemas de Deploy
1. **Verifique logs do serviço**
2. **Confirme variáveis de ambiente**
3. **Teste localmente**
4. **Verifique requirements.txt**

---

## 📊 Monitoramento

### Logs
- **Streamlit:** Painel de admin
- **Render:** Seção Logs
- **Railway:** Dashboard
- **Hugging Face:** Logs da aplicação

### Métricas
- Tempo de resposta
- Uso de memória
- Número de usuários
- Erros de API

---

## 🎯 Próximos Passos

1. **Escolha uma plataforma**
2. **Configure API key**
3. **Faça deploy**
4. **Teste com usuários reais**
5. **Monitore e ajuste**

### Melhorias Futuras
- [ ] Sistema de cache
- [ ] Analytics de uso
- [ ] Múltiplos idiomas
- [ ] Integração com WhatsApp
- [ ] PWA (Progressive Web App)

---

## 💡 Dicas de Otimização

### Performance
- Use cache quando possível
- Limite o tamanho do histórico
- Timeout adequado na API

### Segurança
- Nunca exponha API keys
- Use HTTPS sempre
- Valide inputs do usuário

### UX para Idosos
- Botões grandes
- Contraste alto
- Textos claros
- Navegação simples

---

**🎉 Pronto! Seu chatbot estará online e acessível para ajudar idosos com segurança digital!**
