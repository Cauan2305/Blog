# Blog
*Um Blog Simples de Postagens, Está Sendo Usado DjangoRest , Uma API pegando os comentarios e os post e tambem fiz um Crud com postagens Estou usando a autenticação por session*
*Url Do Projeto : http://blogdjango.pythonanywhere.com/*
* Registra Um usuario ou vai em login e logue com esse usuario teste *
* Usuario : teste
* Senha : cauan123
## Como Rodar Projeto 
*Primeiros Vamos Instalar as Depedençias do Projeto*
```
pip install -r requirements.txt

```

*Vamos Fazer Migrações do Banco de dados *
```
python manage.py makemigrations

```

```
python manage.py migrate
```


* Agora vamos Rodar um Servidor*
```
python manage.py runserver

```

### Agora Acesse http://127.0.0.1:8000/