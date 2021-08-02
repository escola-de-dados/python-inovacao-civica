# python-inovacao-civica

Olá! Este é o repositório do curso **Python para inovação cívica**. Aqui você encontrará os materiais complementares das aulas, e os notebooks dos desafios.

## Organização do repositório

O repositório possui esse `README.md` principal, e um diretório por módulo. Os diretórios estão nomeados de acordo com os módulos correspondentes.

## Configuração de ambiente local

Nossa sugestão é que você configure um ambiente para todos os módulos, criando uma virtualenv geral, já que os módulos possuem biblotecas muito semelhantes entre si. Mas nada te impede de criar um ambiente para cada módulo isoladamente.  

* Python >= 3.7 (Caso você não tenha essa versão, você pode usar o pyenv para instalar. Sugiro dar uma olhada [nesse artigo da Jéssica Temporal](https://jtemporal.com/pyenv-inicio/)).
* `requirements.txt`: cada diretório possúi um arquivo `requirements.txt`, informando todas as bibliotecas necessárias para os notebooks.

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

A segunda sugestão é executar no Binder, faça um fork desse repositório, acesso o site do [Binder nesse link](https://mybinder.org) e informa a url do repositório. 
