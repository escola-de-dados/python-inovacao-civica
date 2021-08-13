# python-inovacao-civica

Olá! Este é o repositório do curso **Python para inovação cívica**. Aqui você encontrará os materiais complementares das aulas e os notebooks dos desafios.

## Organização do repositório

O repositório possui esse `README.md` principal, e um diretório por semana do curso. 

## Configuração de ambiente local

Nossa sugestão é que você configure um ambiente para todos os módulos, criando uma virtualenv geral, já que os módulos possuem biblotecas muito semelhantes entre si. Mas nada te impede de criar um ambiente para cada módulo isoladamente.  

* Python >= 3.7 (Caso você não tenha essa versão, você pode usar o pyenv para instalar. Você pode dar uma olhada [nesse artigo da Jéssica Temporal](https://jtemporal.com/pyenv-inicio/)).

* `requirements.txt`: cada diretório possúi um arquivo `requirements.txt`, informando todas as bibliotecas necessárias para os notebooks (iremos reunir todos eles em um só em breve, aguarde.)

Para criar um ambiente virtual, execute:
```
$ python -m venv env
```

Para ativiar o ambiente virtual `env` que você acabou de criar:
```
$ source env/bin/activate
```

Para instalar as bibliotecas:
```
$ pip install -r requirements.txt
```

## Executando os notebooks no Colab ou Binder

Vou sugerir duas opções caso você não queira executar o projeto no seu computador. A primeira sugestão é utilizar o [Google Colab](https://colab.research.google.com/). Você pode fazer o upload do notebook para o seu drive, e abrir via Google Colab. No módulo 0, na aula sobre *ferramentas para programar em python*, você pode encontrar o passo a passo de como usar o Google Colab.

A segunda sugestão é executar no Binder, faça um fork desse repositório, acesse o site do [Binder nesse link](https://mybinder.org) e informe a url do repositório. 

# Semana 0

# Semana 1

- **estrutura_controle.ipynb**
   - [] Aula 1: Variáveis e tipos de dados
   - [] Aula 2: Operadores
   - [x] Aula 3: Estrutura de controle
   - [x] Aula 4: Estrutura de repetição

- **importando_dados.ipynb**
   - [x] Aula 5: Pacotes
   - [x] Aula 6: Método readcsv
   - [x] Aula 7: Carregando tabelas

# Semana 2

- **estatistica.ipynb**
   - [x] Aula 8: Introdução a estatística
   - [x] Aula 9: Medidas de tendência central e dispersão
   - [x] Aula 10: Outliers e valores faltantes
   - [] Aula 11: Correlação
   - [x] Aula 12: Operações básicas com dados
   - [x] Aula 13: Filter e sort_values
   - [x] Aula 14: Operações com dados e apply
   - [x] Aula 15: Operações com dados e groupby
   - [] Aula 16: Conheça o Perfil Político

# Semana 3

- Colab **part-1**
   - [x] Aula 2: Acessando os dados da CEAP via API
   - [x] Aula 3: Lendo os dados da CEAP com Pandas
   - [x] Aula 4: Analisando os dados da CEAP
   - [x] Aula 6: Dados da Receita Federal
   - [x] Aula 7: Receita Federal e CEAP
- Colab **part-2**
   - [x] Aula 4: Analisando os dados da CEAP
- Colab **part-3**
   - [ ] Aula 5: Conhecendo ferramentas para usar com a Rosie e o Jarbas
- Colab **part-4**
   - [x] Aula 10: Respondendo perguntas sobre nossos dados
- Script pyhon
   - [x] Aula 8: Evoluindo nosso projeto: Criando um script Python
- Desafios
   - [x] 1: extração, leitura e transformação
   - [x] 2: análises

# Semana 4

## Instruções iniciais

Aqui, todos os arquivos de código das videoaulas estão disponíveis e organizados
por pasta referente a respectiva aula.

Para editar código, recomendamos o Visual Studio Code (só dica mesmo, qualquer
editor de texto serve).

Para realizar algumas atividades do curso, o navegador Google Chrome
(ou variantes como Chromium) é necessário.

## Pré-instalação

No Windows, a biblioteca `scrapy` necessita da instalação das [Ferramentas de
Build do Visual Studio](https://visualstudio.microsoft.com/pt-br/downloads/#build-tools-for-visual-studio-2019).
Execute o instalador e durante a instalação, selecione a opção
“Desenvolvimento para desktop com C++” e finalize o processo. A instalação
tem cerca de 6GB... É bem simples mas demora :)

## Instalação

Para executar a maioria dos códigos, é necessário instalar as dependências
especificadas no arquivo `requirements.txt` com o comando (preferencialmente
com um ambiente virtual criado):

```sh
$ pip install -r requirements.txt
```

Mas este arquivo é só para usar para este comando mesmo pois ele contém TODAS
as dependências (incluindo dependências de dependências e dependências de
dependências de dependências, e por aí vai hehehe). Se por curiosidade quiser
saber a lista de bibliotecas que realmente utilizamos, veja o arquivo
`requirements.in`.
