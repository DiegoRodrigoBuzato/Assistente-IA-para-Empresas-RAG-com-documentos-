# 📚 RAG com LangChain + ChromaDB + OpenAI

Sistema de **Retrieval-Augmented Generation (RAG)** que permite fazer perguntas em linguagem natural sobre documentos PDF, utilizando LangChain, ChromaDB como banco vetorial e a API da OpenAI.

---

## 🧠 Como funciona

```
PDFs → Chunking → Embeddings → ChromaDB
                                  ↓
Pergunta → Busca Semântica → Contexto → LLM → Resposta
```

1. Os PDFs são carregados e divididos em chunks de texto
2. Cada chunk é transformado em um embedding via OpenAI
3. Os embeddings são persistidos no ChromaDB
4. Na consulta, a pergunta é vetorizada e os chunks mais relevantes são recuperados
5. O contexto recuperado é enviado ao modelo GPT para gerar a resposta final

---

## 💡 Por que usar RAG?

Enviar documentos inteiros para um LLM a cada pergunta é inviável: documentos longos consomem uma quantidade enorme de tokens, elevando o custo da API e, muitas vezes, degradando a qualidade das respostas — modelos tendem a "se perder" em contextos muito extensos.

Este projeto resolve esse problema com a abordagem RAG:

- **Economia de tokens**: em vez de enviar o documento completo, apenas os 3 trechos mais relevantes para a pergunta são enviados ao modelo. Um PDF de 100 páginas pode gerar centenas de chunks, mas o LLM recebe somente o essencial.
- **Respostas mais precisas**: ao fornecer um contexto cirúrgico e diretamente relacionado à pergunta, o modelo foca no que importa e alucina menos.
- **Escalabilidade**: a base de conhecimento pode crescer com dezenas de PDFs sem aumentar o custo por consulta.

> Em termos práticos: ao invés de gastar milhares de tokens enviando um documento inteiro, você gasta apenas algumas centenas com os trechos certos — e ainda obtém respostas melhores.

---

## 🗂️ Estrutura do Projeto

```
.
├── base/               # Pasta com os arquivos PDF da base de conhecimento
├── db/                 # Banco vetorial ChromaDB (gerado automaticamente)
├── criar_db.py         # Script para indexar os PDFs e criar o banco
├── main.py             # Script para consultar a base via terminal
├── .env                # Variáveis de ambiente (não versionar)
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python 3.9+
- Conta na [OpenAI](https://platform.openai.com/) com chave de API

---

## 🚀 Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**2. Crie e ative um ambiente virtual**

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Instale as dependências**

```bash
pip install langchain langchain-community langchain-chroma langchain-openai chromadb pypdf python-dotenv
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

> ⚠️ **Nunca** versione o arquivo `.env`. Adicione-o ao `.gitignore`.

---

## 📖 Como usar

### 1. Adicionar documentos

Coloque seus arquivos `.pdf` dentro da pasta `base/`.

### 2. Criar o banco vetorial

Execute o script de indexação uma única vez (ou sempre que adicionar novos PDFs):

```bash
python criar_db.py
```

O banco será salvo na pasta `db/`.

### 3. Fazer perguntas

```bash
python main.py
```

O sistema irá solicitar sua pergunta no terminal e retornará uma resposta baseada nos documentos indexados.

---

## 🔧 Configurações

| Parâmetro | Arquivo | Valor padrão | Descrição |
|---|---|---|---|
| `chunk_size` | `criar_db.py` | `2000` | Tamanho máximo de cada chunk em caracteres |
| `chunk_overlap` | `criar_db.py` | `500` | Sobreposição entre chunks |
| `k` | `main.py` | `3` | Número de chunks recuperados por consulta |
| Score mínimo | `main.py` | `0.7` | Relevância mínima para considerar um resultado |

---

## 🛡️ .gitignore recomendado

```gitignore
.env
db/
venv/
__pycache__/
*.pyc
```

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'feat: adiciona minha feature'`)
4. Envie para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
