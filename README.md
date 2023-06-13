# python-inovacao-civica

Olá! Este é o repositório do curso **Python para inovação cívica**. Aqui você encontrará os materiais complementares das aulas e os notebooks dos desafios.

## Organização do repositório

O repositório possui esse `README.md` principal, e um diretório por semana do curso.

## Pré-configuração
No Windows, a biblioteca `scrapy` necessita da instalação das [Ferramentas de Build do Visual Studio](https://visualstudio.microsoft.com/pt-br/downloads/#build-tools-for-visual-studio-2019) e ela é utilizada no projeto Querido Diário. Execute o instalador e durante a instalação, selecione a opção “Desenvolvimento para desktop com C++” e finalize o processo. A instalação tem cerca de 6GB... É bem simples mas demora :)

## Configuração de ambiente local

Nossa sugestão é que você configure um ambiente para todos os módulos, criando uma virtualenv geral, já que os módulos possuem biblotecas muito semelhantes entre si. Mas nada te impede de criar um ambiente para cada módulo isoladamente.

* Python >= 3.7 (Caso você não tenha essa versão, você pode usar o pyenv para instalar. Se for o seu caso, você pode conferir [esse artigo da Jéssica Temporal](https://jtemporal.com/pyenv-inicio/)).

* Na raiz do projeto existem dois arquivos: `requirements.txt` e `requirements.in`. Estes arquivos contêm as dependências (bibliotecas que precisamos para executar os códigos) para todo o curso e para usá-los siga as instruções a seguir:

Para criar um ambiente virtual, execute:

```
$ python3 -m venv env
```

Para ativar o ambiente virtual `env` que você acabou de criar:
```
$ source env/bin/activate
```

Para instalar as bibliotecas:
```
$ pip install -r requirements.txt
```

Recomendamos usar este arquivo pa mesmo pois ele contém TODAS as dependências (incluindo dependências de dependências e dependências de
dependências de dependências, e por aí vai). Se por curiosidade quiser saber a lista de bibliotecas que realmente utilizamos diretamente, sem contar as dependências aninhadas, veja o arquivo `requirements.in`.

Se tiver alguma dificuldade com essa instalação, nos envie o erro para que possamos ajudar. Também é possível tentar instalar as dependências a partir do `requirements.in` da seguinte forma:

```
$ pip install -r requirements.in
```

## Executando os notebooks

Para executar os códigos no seu computador, recomendamos o [Visual Studio Code](https://code.visualstudio.com/). Outra opção para trabalhar locamente é [Jupyter Notebook](https://jupyter.org/try)

Há também a opção de utilizar notebooks online, como o [Google Colab](https://colab.research.google.com/). Você pode fazer o upload do notebook para o seu Drive e abrir via Google Colab. No módulo 0, na aula sobre *ferramentas para programar em Python*, você pode encontrar o passo a passo de como usar o Google Colab.

A segunda sugestão é executar via o Binder. Neste caso, faça um fork desse repositório, acesse o site do [Binder nesse link](https://mybinder.org) e informe a URL do repositório.

# Semana 0

   - [ ] Aula 0: Apresentação do curso
   - [ ] Aula 1: Inovação cívica e tecnologia no Brasil
   - [ ] Aula 3: O maravilhoso mundo das tecnologias abertas
   - [ ] Aula 4: Git e Github: Primeiros passos
   - [ ] Aula 5: Introdução ao pensamento computacional
   - [ ] Aula 6: Benefícios e aplicações práticas do pensamento computacional
   - [ ] Aula 7: Como aprender linguagem de programação
   - [ ] Aula 8: Linguagens do curso
   - [ ] Aula 9: Configurar um ambiente de desenvolvimento local
   - [ ] Aula 10: Ferramentas para programação em python
   - [ ] Aula 11: Como funciona a internet
   - [ ] Aula 12: Introdução a API
   - [ ] Aula 13: Interagindo com APIs

- **desafio.ipynb**
   - [x] Desafio: Como aprender linguagens de programação
- **desafio_gabarito.ipynb**
   - [ ] Resolução do desafio: Como aprender linguagens de programação


# Semana 1

- **estrutura_controle.ipynb**
   - [ ] Aula 1: Variáveis e tipos de dados
   - [ ] Aula 2: Operadores
   - [x] Aula 3: Estrutura de controle
   - [x] Aula 4: Estrutura de repetição

- **importando_dados.ipynb**
   - [x] Aula 5: Pacotes
   - [x] Aula 6: Método readcsv
   - [x] Aula 7: Carregando tabelas

- **desafio.ipynb**
   - [x] Desafio

- **desafio_gabarito.ipynb**
   - [ ] Resolução do desafio

# Semana 2

- **estatistica.ipynb**
   - [x] Aula 8: Introdução a estatística
   - [x] Aula 9: Medidas de tendência central e dispersão
   - [x] Aula 10: Outliers e valores faltantes
   - [ ] Aula 11: Correlação
   - [x] Aula 12: Operações básicas com dados
   - [x] Aula 13: Filter e sort_values
   - [x] Aula 14: Operações com dados e apply
   - [x] Aula 15: Operações com dados e groupby
   - [ ] Aula 16: Conheça o Perfil Político

- **desafio.ipynb**
   - [x] Desafio

- **desafio_gabarito.ipynb**
   - [ ] Resolução do desafio

# Semana 3

- **ceap_api.ipynb**
   - [ ] Aula 1: Entendendo os dados da CEAP
   - [x] Aula 2: Acessando os dados da CEAP via API
   - [x] Aula 3: Lendo os dados da CEAP com Pandas
   - [X] Aula 4: Organizando e visualizando dados
   - [X] Aula 5: Analisando os dados da CEAP
   - [ ] Aula 6: Conhecendo ferramentas para usar com a Rosie e o Jarbas
   - [X] Aula 7: Dados da Receita Federal

- **desafio.ipynb**
   - [x] Desafio: Extração, leitura e transformação de dados

- **desafio_gabarito.ipynb**
   - [ ] Resolução do desafio: Extração, leitura e transformação de dados


# Semana 4

- **merge.ipynb**
   - [x] Aula 8: Receita Federal e CEAP

- **script.py**
   - [x] Aula 9: Evoluindo nosso projeto: Criando um script Python

- **sort_values_bruto.ipynb**
   - [x] Aula 10: Respondendo perguntas sobre nossos dados
- **sort_values_limpo.ipynb**
   - [x] Aula 10: Respondendo perguntas sobre nossos dados
   - [ ] Aula 11: Introdução ao Github
   - [ ] Aula 12: Salvando nosso projeto no Git
   - [ ] Aula 13: Por dentro do Serenata de Amor

- **desafio1.ipynb**
   - [x] Desafio: Cruzamento dos dados da CEAP com os dados da Receita Federal

**desafio1_gabarito.ipynb**
   - [ ] Resolução do desafio: Cruzamento dos dados da CEAP com os dados da Receita Federal

- **scraping.ipynb**
   - [x] Introdução a webscraping com Pandas

- **desafio2.ipynb**
   - [x] Desafio: Webscraping simples
   - [ ] Resolução do desafio: Webscraping simples


# Semana 5

- **api_qd.py**
   - [ ] Aula 1: Apresentando o Querido Diário
   - [x] Aula 2: Por dentro do Querido Diário

- **variaveis_funcoes.py**
   - [x] Aula 3: Introdução a Orientação a Objetos

- **classes.py**
   - [x] Aula 3: Introdução a Orientação a Objetos

- **heranca.py**
   - [x] Aula 3: Introdução a Orientação a Objetos

- **sobreposicao.py**
   - [x] Aula 3: Introdução a Orientação a Objetos

- **projeto_inovacao**
   - [x] Aula 4: Por dentro do raspador do Querido Diário
   - [ ] Aula 5: Analisando páginas web - Inspecionando elementos
   - [ ] Aula 6: Analisando páginas web - Inspecionando a rede
   - [ ] Aula 7: Selecionando elementos com XPath

- **expressoes_regulares.py**
   - [x] Aula 8: Expressões regulares

- **ba_caetite.py**
   - [x] Aula 9: Traduzindo a análise para um raspador

- **caetite.py**
   - [x] Aula 10: Indo além

- **caetite_selenium.py**
   - [x] Aula 10: Indo além

- **extract_text_with_apache_tika.ipynb**
   - [x] Aula 10: Indo além

- **desafio/desafio1.ipynb**
   - [x] Desafio: Wikipédia com XPath
   - [ ] Resolução do desafio: Wikipédia com XPath

# Semana 6

- **desafio/desafio2.ipynb**
   - [x] Desafio: Raspador de diários
   - [ ] Resolução do desafio: Raspador de diários




Para realizar algumas atividades deste módulo, o navegador Google Chrome (ou variantes como Chromium) é necessário.
