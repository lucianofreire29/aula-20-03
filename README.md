# SmartSystem — Login e Cadastro

Aplicação desktop desenvolvida em Python para demonstrar navegação entre telas, cadastro de usuários e autenticação durante uma sessão.

## Funcionalidades

- criação de conta com validação dos campos;
- validação básica do formato do e-mail;
- senha com no mínimo seis caracteres;
- confirmação de senha;
- prevenção de e-mails duplicados;
- autenticação de usuários cadastrados;
- opção para mostrar ou ocultar senhas;
- navegação entre as telas de login e cadastro.

## Tecnologias

- Python 3
- CustomTkinter
- CTkMessagebox

## Estrutura

```text
.
├── main.py
├── tela_principal.py
├── tela_login.py
├── tela_cadastro.py
├── requirements.txt
└── README.md
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/lucianofreire29/aula-20-03.git
cd aula-20-03
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python main.py
```

## Observação

Os usuários cadastrados são mantidos somente em memória. Ao fechar o programa, os cadastros são apagados. Uma futura evolução poderá adicionar banco de dados e armazenamento seguro de senhas.

## Autor

**Luciano Freire**

- GitHub: [@lucianofreire29](https://github.com/lucianofreire29)
