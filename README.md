# Análise Quadro de Medalhas das Olimpíadas

Este projeto é uma aplicação Streamlit para análise do quadro de medalhas das Olimpíadas. Ele permite visualizar dados históricos de medalhas, explorar a distribuição de medalhas por país e ano, e visualizar essas informações em gráficos interativos.

## Estrutura do Projeto

```
__pycache__/
.gitignore
.streamlit/
    config.toml
main.py
page1.py
page2.py
page3.py
Summer_olympic_Medals.csv
utils.py
```

### Arquivos e Diretórios

- [`__pycache__/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2F__pycache__%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/__pycache__/"): Diretório gerado automaticamente pelo Python para armazenar arquivos compilados.
- [`.gitignore`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/.gitignore"): Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- [`.streamlit/config.toml`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2F.streamlit%2Fconfig.toml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/.streamlit/config.toml"): Arquivo de configuração do Streamlit, definindo o tema da aplicação.
- [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/main.py"): Arquivo principal que inicializa a aplicação Streamlit e define a navegação entre as páginas.
- [`page1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fpage1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/page1.py"): Define a página de visão geral das medalhas.
- [`page2.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fpage2.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/page2.py"): Define a página de visão específica por país.
- [`page3.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fpage3.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/page3.py"): Define a página de mapa mundi das medalhas.
- [`Summer_olympic_Medals.csv`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2FSummer_olympic_Medals.csv%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/Summer_olympic_Medals.csv"): Arquivo CSV contendo os dados das medalhas olímpicas.
- [`utils.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Futils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/utils.py"): Contém funções utilitárias para carregar e manipular os dados.

## Configuração

### Tema

O tema da aplicação é configurado no arquivo [`.streamlit/config.toml`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2F.streamlit%2Fconfig.toml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/.streamlit/config.toml"):

## Funcionalidades

### Página Principal ([`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/main.py"))

A página principal define a navegação entre as diferentes páginas da aplicação.

### Página de Visão Geral ([`page1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fpage1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/page1.py"))

Exibe um gráfico de barras com o total de medalhas por país em um intervalo de tempo selecionado.

### Página de Visão Específica ([`page2.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fpage2.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/page2.py"))

Exibe gráficos de linhas e barras com a evolução das medalhas de um país específico ao longo dos anos.

### Página de Mapa Mundi ([`page3.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Fpage3.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/page3.py"))

Exibe um mapa mundi com a distribuição de medalhas por país em um ano específico.

### Utilitários ([`utils.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ftr%2FDocumentos%2FPython%2FProjetos%2FMedalhas_olimpicas%2Futils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22074f1a6c-07d6-449d-8124-3337ad2b21cd%22%5D "/home/tr/Documentos/Python/Projetos/Medalhas_olimpicas/utils.py"))

Contém funções para carregar e manipular os dados.

## Como Executar

1. Clone o repositório:
   - git clone https://github.com/thiagoregueira/Quadro_medalhas_Olimpicas_Gerais.git
   - cd Quadro_medalhas_Olimpicas_Gerais
  
2. Crie um ambiente virtual e ative-o:
   - python -m venv venv
   - source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências necessárias:
   - pip install -r requirements.txt

4. Execute a aplicação:
   - streamlit run main.py

## Licença

Este projeto está licenciado sob a licença MIT.
