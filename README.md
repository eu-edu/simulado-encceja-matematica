# 🧮 Simulado ENCCEJA - Matemática (Ensino Médio)

Simulado interativo para o ENCCEJA (Exame Nacional para Certificação de Competências de Jovens e Adultos) na área de Matemática para Ensino Médio.

## 📋 Sobre o Projeto

Este projeto oferece um simulado completo com 70 questões de matemática para preparação ao ENCCEJA. O sistema apresenta:

- ✅ 70 questões de matemática variadas
- ⏱️ Timer com tempo decorrido
- 📊 Barra de progresso visual
- 🎯 Cálculo automático de aproveitamento
- 📋 Gabarito completo ao final do teste
- 🔄 Opção para refazer o simulado

## 🛠️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

### Python
- **Python 3.8 ou superior**
- Download: [python.org](https://www.python.org/downloads/)
- Durante a instalação, marque a opção "Add Python to PATH"

### Git (opcional)
- Para clonar o repositório
- Download: [git-scm.com](https://git-scm.com/downloads)

## 📦 Instalação

### 1. Obter o projeto

**Opção A: Clone via Git**
```bash
git clone https://github.com/SEU_USUARIO/simulado-encceja-matematica.git
cd simulado-encceja-matematica
```

**Opção B: Download direto**
- Baixe o arquivo ZIP do repositório
- Extraia em uma pasta de sua escolha
- Navegue até a pasta extraída

### 2. Criar ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install streamlit
```

**Ou usando requirements.txt (se disponível):**
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

### 1. Ativar o ambiente virtual (se criado)

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Executar o simulado

```bash
streamlit run enceja_math.py
```

### 3. Acessar no navegador

O Streamlit abrirá automaticamente no navegador. Caso não abra, acesse:
- **URL local:** http://localhost:8501

## 📖 Como Usar

1. **Início do Teste:** Ao executar, o simulado começará automaticamente
2. **Responder Questões:** Selecione uma das 4 alternativas (A, B, C, D)
3. **Avançar:** Clique em "Responder" para ir para a próxima questão
4. **Acompanhar Progresso:** Observe a barra de progresso e timer
5. **Resultado Final:** Após a última questão, veja seu aproveitamento
6. **Gabarito:** Expanda "Ver gabarito e suas respostas" para conferir
7. **Refazer:** Clique em "🔄 Refazer Simulado" para tentar novamente

## 📁 Estrutura do Projeto

```
simulado-encceja-matematica/
├── enceja_math.py          # Arquivo principal do simulado
├── enceja_math2.py         # Versão alternativa (se disponível)
├── README.md               # Este arquivo
├── requirements.txt        # Dependências do projeto
├── .gitignore             # Arquivos ignorados pelo Git
└── venv/                  # Ambiente virtual (não versionado)
```

## 🔧 Solução de Problemas

### Erro: "streamlit não é reconhecido"
```bash
# Certifique-se de que o ambiente virtual está ativo
pip install streamlit
```

### Erro: "Python não é reconhecido"
- Reinstale o Python marcando "Add to PATH"
- Ou use `python3` no lugar de `python`

### Porta já em uso
```bash
# Use uma porta diferente
streamlit run enceja_math.py --server.port 8502
```

### Problemas com ambiente virtual
```bash
# Desative e recrie o ambiente
deactivate
rmdir /s venv  # Windows
rm -rf venv    # Linux/Mac
python -m venv venv
```

## 📚 Conteúdo das Questões

O simulado abrange diversos tópicos de matemática do Ensino Médio:

- 🧮 Aritmética e porcentagens
- 📐 Geometria e volumes
- 📊 Estatística e médias
- 🔢 Álgebra e equações
- 📈 Funções e gráficos
- 💰 Matemática financeira
- 🔄 Sequências e progressões

## 🎯 Critérios de Avaliação

- **Excelente:** 90% ou mais (63+ acertos)
- **Bom:** 70% a 89% (49-62 acertos)
- **Regular:** 50% a 69% (35-48 acertos)
- **Insuficiente:** Menos de 50% (menos de 35 acertos)

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é destinado para fins educacionais e de estudo.

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Verifique a seção de solução de problemas acima

---

**Desenvolvido para auxiliar estudantes na preparação para o ENCCEJA** 📚✨