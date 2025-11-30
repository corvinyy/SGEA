# 🏛️ CASA DE ATENA 🏛️
### Sistema de Gerenciamento de Eventos Acadêmicos ###

Sistema web para gestão de eventos acadêmicos e emissão de certificados.  
Permite o cadastro e autenticação de usuários, criação e inscrição em eventos, além da geração de certificados para os participantes.

### Desenvolvedores
- **👤💻 [okiobot (Mateus Rodrigues)](https://github.com/okiobot)**
- **👤💻 [corvinyy (Lorena Araujo)](https://github.com/corvinyy)**
- **👤💻 [devlucasaf (Lucas Freitas)](https://github.com/devlucasaf)**

## ⚠️ ATENÇÃO: Os eventos apresentados neste projeto são fictícios e utilizados apenas para fins de demonstração e testes, sem qualquer relação comercial ou institucional com os organizadores originais.

### 📸 PREVIEW (Projeto em progresso!)

![Preview of the current progress](./sgea/login/static/assets/imgs/PreviewNOVA.png)

### 📸 AO CLICAR EM "VER DETALHES"
![Preview of the current progress](./sgea/login/static/assets/imgs/PreviewNOVA2.png)


### 🛠️ Status

⚙️ Em progresso

### ✨ Funcionalidades

- 👥 Cadastro e autenticação de usuários (alunos, professores, organizadores)
- 🗓️ Criação e gerenciamento de eventos (informações como tipo de evento, data, horário, quantidade de participantes)
- 📝 Inscrição de usuários em eventos
- 🎓 Emissão de certificados para participantes
- 🛠️ Aplicação de boas práticas de desenvolvimento (MVC com Django, documentação)

---

### 🛠️ Ferramentas e Tecnologias


[![Tech](https://skillicons.dev/icons?i=python,django,sqlite,js,html,css)](https://skillicons.dev)

[![Tools](https://skillicons.dev/icons?i=vscode,github)](https://skillicons.dev)


---

### 📁 Estrutura do Projeto
```bash
SGEA---Casa-de-Atena/ # repositório 
│
├── sgea/ # pasta onde vai rodar o site localmente
│   │
│   ├── login/ 
│   │   ├── static/ # arquivos estáticos (CSS, JS, imagens)
│   │   ├── templates/ #pasta com as páginas do site
│   │   │   └── (arquivos.html) 
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── managers.py  # managers personalizados 
│   │   ├── models.py # modelos/tabelas do app
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py  # lógica das rotas (renderização, API, etc)
│   │
│   ├── sgea/
│   │   ├── asgi.py
│   │   ├── settings.py # configurações globais do Django (apps, DB, static, etc)
│   │   ├── urls.py # roteamento principal do projeto
│   │   └── wsgi.py
│   │
│   ├── db.sqlite3  # banco de dados SQLite
│   └── manage.py # CLI do django (rodar servidor, criar apps, fazer migrações)
│
├── .gitignore  # arquivos e pastas ignorados pelo git
├── README.md # documentação geral do projeto
└── Documentação - Casa de Atena.pdf # documento extra detalhada do projeto
```

---

### 🚀 Como Rodar o Projeto Localmente

**1. Faça o clone do repositório** 

```bash
git clone https://github.com/okiobot/SGEA---Casa-de-Atena
```

**2. Acessar a pasta onde está o projeto Django**

```bash
cd SGEA---Casa-de-Atena 
cd sgea
```

**3. Criar e ativar um ambiente virtual (recomendado)**

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Instalar o Django e outras dependências**
```bash
pip install django
```

```bash
pip install -r requirements.txt
```

```bash
pip install djangorestframework
```

```bash
pip install djangorestframework_simplejwt
```

**5. Aplicar as migrações do banco de dados**
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

**6. Rodar o servidor local**
```bash
python manage.py runserver
```

**📌 O projeto ficará disponível em: http://127.0.0.1:8000/**

---

### Feito com ❤️ e 😡
