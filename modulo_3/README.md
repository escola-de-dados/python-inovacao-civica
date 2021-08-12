# Módulo 3 - Querido Diário, vou aprender a raspar dados

Olá! Esse é o espaço com o desafio e materiais auxiliares do módulo 3.

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
