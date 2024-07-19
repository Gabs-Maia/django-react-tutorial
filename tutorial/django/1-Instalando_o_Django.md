# INTRODUÇÃO: 

Django em um framework, como uma caixa de ferramentas, que permite a criação de serviços e aplicativos Web com grande robustes. Jutamente ao python o framework já disponibiliza frames e templates (algo pré-pronto) que permitem a dissolução da maioria das configurações necessárias em, apenas, algumas linhas de código. Dessa forma, com o Django, a programador já pode começar a produzir sua aplicação sem se preocupar com a mioria dos outros aparatos e artefatos que precisam ser configurados.

Já como estamos trabalhando em um abiemtne Python, é de extrema importância trabalharmos em um ambiente virtual. Caso você não saiba a definição de um ambiente virtual, não tem problema, é bem simples e já já será respondio.

## AMBIENTE VIRTUAL: DEFINIÇÃO E CRIAÇÃO

Primeiro vamos criar um ambiente virtual:

```example
python -m venv nome_do_projeto
```

Um ambiente virtual nada mais é do que um espaço virtual criado dentro do seu computador. Nesse espaço todas as bibliotecas instaladas serão contidas virtualmente, isso significa que o que for instalado aqui não será instalado em sua máquina, no seu computador.

Após instalado, acesse a nova área criada:
```example
nome_do_projeto\Scripts\Activate.ps1
```


Agora podemos instalar o que iremos utilizar:
```example
- pip install django
- pip install djangorestframework
- pip install pandas
- pip install mysqlclient 
```

A biblioteca Pandas é utilizada para o confecção e manipulação de planilhas, como por exemplo, documentos excel e/ou .csv

Mysql é para trabalharmos com o banco de dados. 

### SALVANDO AS ALTERAÇÕES:

Caso você queira utilizar o projeto em uma outra máquina, ou caso alguém utilize o seu código, é importante que as bibliotecas estejam listadas e disponíveis em um arquivo.

*digite no terminal*
```
pip freeze > requirements.txt
```

Dessa forma, quando vc quiser reutilizar o projeto, um simples comando instalará todas as bibliotecas utilizadas.

```
pip intalls -r requirements.txt
```
