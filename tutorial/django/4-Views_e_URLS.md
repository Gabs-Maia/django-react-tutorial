# VIEWS

Se você já é familiarizado com a arquitetura MVC, `Views` é a camada que age como um controller. Um controller é a camada da aplicação que, basicamente, lida com o mapeamento de 'end-points', ou seja, a caminho que levará o usuário a certo lugar em seu site. 
```
www.examplo.com.br/produtos
```
Aqui, `/produtos` é o que te levará para a página de produtos de nosso exemplo. Esse trabalho de indicar onde o aplicativo deve te levar é o que faz uma `View`/`Controller`. 

Já como iremos utilizar React.js para a confecção do front-end, é importante salientar a utilização de `serializers` (serializadores). Basicamente, um serializador irá transformar o seu 'arquivo' (dados) em uma corrent/fluxo de bytes; isso permite que suas informações sejam facilmente traduzidas de um formato para o outro. 

No contexto do Django, no entanto, serializadores transforma objetos-django em objetos-python. Apesar da diferença, falando de conceito, os processos muito se parecem (não são a mesma coisa/procedimento).

`serializers.py`

```python
from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'language_name', 'language_family', 'region_origin', 'sentences', 'words')
```
- `serializers` : importado do Django `rest_framework`.
- `Meta`: é uma convenção do django que ajuda a `super-classe` com a disponibilização de meta-dados. 
- `fields`: é campo que indica o que deve ser contido no objeto serializado.  

Com o serializador pronto, podemos seguir para a confecção de nossa View 

```python 
class LanguageView(viewsets.ModelViewSet):
   serializer_class = LanguageSerializer
   queryset = Language.objects.all()

```
- `serializer_class`: aqui estamos definindo, na classe, o serializador utilizado.
- `queryset`: iniciamos uma query (pesquisa) que retorna todos objetos criados. 

Com nossas Views criadas, precisamos apena de mais uma coisa, registrar cada uma delas em nossas URLs.

# URLS

```python
router = routers. DefaultRouter()
router.register(r'language', views.LanguageView, 'language')
router.register(r'words', views.WordsViewSet, 'words')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls))
]
```
-`DefaultRouter()`: Irá gerar, de maneira automática, URLs para todas a `ViewSets`declaradas até agora. Além disso, define URL raiz, padrão, para sua API.
-`router.register()`: É o que irá nossa View no router. (`r'language'`: prefixo de nossa URL | `viewsets.ModelViewSet`: nossa class | 'language': o nome base de nossa URL)
-`path()`: dentro de `urlpatterns` utilizamos o `path()` para construir os caminhos que nossa aplicação utilizará para separar o domínio em diferentes partes. 

Com tudo produzido, vamos testar nossa aplicação!

## TESTANDO NOSSA APLICAÇÃO:

Novamente, abra o seu terminal e rode o servidor ( não se esqueça do comando):

```
python manage.py runserver
```

Vá na barra URL do navegador aberto e complemente a sua URL com o end-point `/amdmin`. 

Esta é a página que irá abrir:

![alt text](..\django\img\image.png)

Os links em vermelho irão te levar à páginas com as informações correspondentes a cada objeto... Clica nelas, descubra, se divirta!