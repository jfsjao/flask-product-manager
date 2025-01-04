
# Sistema de Cadastro e Listagem de Produtos

Este projeto é uma aplicação simples desenvolvida com **Flask**, que permite cadastrar e listar produtos. A aplicação inclui estilização com **CSS** e interatividade com **JavaScript**.

---

## 🎯 Funcionalidades

1. **Cadastro de Produtos**:
   - Nome do Produto
   - Descrição
   - Valor
   - Disponibilidade (Sim/Não)

2. **Listagem de Produtos**:
   - Mostra os produtos cadastrados.
   - Ordenação dos produtos por valor (do menor para o maior).
   - Exibe as colunas: Nome, Valor e Disponível.

3. **Estilização e Interatividade**:
   - Interface estilizada com **CSS**.
   - Interatividade usando **JavaScript** (ex.: clique em uma linha da tabela para mostrar os detalhes do produto).

---

## 🛠️ Requisitos

Certifique-se de que possui os seguintes requisitos instalados:

- **Python 3.7+**
- **Pip** (gerenciador de pacotes Python)
- **Virtualenv** (opcional, mas recomendado)

---

## 🚀 Como Executar

### 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional)

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

Instale as dependências do projeto:

```bash
pip install flask
```

### 4. Executar a Aplicação

No terminal, inicie o servidor Flask:

```bash
python app.py
```

### 5. Acessar no Navegador

Abra o navegador e acesse:

```
http://127.0.0.1:5000/
```

---

## 📁 Estrutura do Projeto

```
/project-root
    /static
        style.css      # Arquivo CSS para estilização
        script.js      # Arquivo JavaScript para interatividade
    /templates
        cadastrar.html # Página de cadastro de produtos
        listagem.html  # Página de listagem de produtos
    app.py             # Aplicação principal Flask
```

---

## ⚙️ Explicação Técnica

1. **Backend**:
   - Desenvolvido com Flask, uma micro-framework para Python.
   - O arquivo `app.py` gerencia as rotas:
     - `/`: Página de listagem.
     - `/cadastrar`: Página de cadastro.

2. **Frontend**:
   - Utiliza HTML, CSS (em `style.css`) e JavaScript (em `script.js`).
   - A estilização inclui:
     - Tabela responsiva.
     - Botões estilizados.
     - Destaque nas linhas ao passar o mouse.

3. **Arquivos Estáticos**:
   - Os arquivos CSS e JavaScript estão localizados na pasta `static`.
   - Referenciados no HTML usando a função `url_for` do Flask.

---

## 💡 Personalizações Futuras

- Adicionar persistência de dados com um banco de dados como SQLite ou PostgreSQL.
- Implementar validação de formulário no frontend.
- Melhorar a responsividade para dispositivos móveis.

---

## 📝 Licença

Este projeto é de uso livre para fins de aprendizado e prática. Sinta-se à vontade para modificar e expandir conforme necessário.

---

Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir! 😊
