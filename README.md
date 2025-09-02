# Pipeline de Dados com Python, MongoDB e MySQL

Este projeto foi desenvolvido como parte dos estudos do curso de "Pipeline de dados: integrando Python com MongoDB e MySQL" da Alura. O objetivo é construir um pipeline de dados completo utilizando Python, MongoDB Atlas e MySQL, aplicando boas práticas de organização e modularização de código.

## Objetivos do Projeto

- Construir um pipeline de dados com Python
- Configurar e conectar ao MongoDB Atlas usando Pymongo
- Realizar transformações nos dados extraídos
- Instalar e configurar o MySQL no WSL
- Conectar o MySQL ao Python
- Estruturar o código Python em funções reutilizáveis

## Estrutura do Projeto

```
.
├── data/                  # Dados originais em CSV
│   ├── tabela_livros.csv
│   └── tb_2021_em_diante.csv
├── data_python/           # Dados processados/exportados em CSV
│   ├── tabela_livros.csv
│   └── tb_2021_em_diante.csv
├── notebooks/             # Notebooks Jupyter para extração, transformação e carga
│   ├── extract_and_save_data.ipynb
│   ├── save_data_mysql.ipynb
│   └── transform_data.ipynb
├── scripts/               # Scripts Python organizados em funções
│   ├── extract_data.py
│   ├── load_data.py
│   └── transform_data.py
├── venv/                  # Ambiente virtual Python
├── .env                   # Variáveis de ambiente (senhas, conexões)
├── .gitignore             # Arquivos e pastas ignorados pelo Git
└── README.md              # Documentação do projeto
```

## Pré-requisitos

- Python 3.8+
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- MySQL instalado no WSL (Windows Subsystem for Linux)
- [Pymongo](https://pymongo.readthedocs.io/en/stable/)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- Jupyter Notebook

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/pipeline-python-mongo-mysql.git
   cd pipeline-python-mongo-mysql
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate     # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```sh
   pip install pymongo 
   ```
   ```sh
   pip install mysql-connector-python
   ```
   ```sh
   pip install pandas
   ```
   ```sh
   pip install jupyter
   ```
   ```sh
   pip install python-dotenv
   ```

4. Configure o arquivo `.env` com suas credenciais do MongoDB Atlas e MySQL:
   ```
   DB_PASSWORD=suasenha_mongodb
   MYSQL_PASSWORD=suasenha_mysql
   ```

## Como Executar

### 1. Extração de Dados

- Utilize o notebook `notebooks/extract_and_save_data.ipynb` ou o script `scripts/extract_data.py` para extrair dados e salvar no MongoDB Atlas.

### 2. Transformação de Dados

- Realize transformações utilizando o notebook `notebooks/transform_data.ipynb` ou o script `scripts/transform_data.py`.

### 3. Carga de Dados no MySQL

- Carregue os dados transformados no MySQL usando o notebook `notebooks/save_data_mysql.ipynb` ou o script `scripts/load_data.py`.

## Principais Funcionalidades

- Conexão segura com MongoDB Atlas e MySQL usando variáveis de ambiente
- Extração, transformação e carga (ETL) de dados estruturados
- Manipulação de dados com Pandas
- Organização do código em funções para facilitar manutenção e reuso

## Referências

- [Curso Engenharia de Dados com Python e MongoDB - Alura](https://www.alura.com.br/)
- [Documentação Pymongo](https://pymongo.readthedocs.io/en/stable/)
- [Documentação MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

## Licença

Este projeto é apenas para fins de estudo e aprendizado. Não é destinado a uso em produção.