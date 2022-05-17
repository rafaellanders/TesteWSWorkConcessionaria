# TesteWSWorkConcessionaria
Teste para a WS Work 
neste arquivo, explicarei cada passo realizado por mim para este projeto

 setup/settings.py -->  foi onde configurei todas as permissões e o crud (por meio desta pasta, posso deixar algumas definições como 'default' do django rest framework), fiz a ligação com o banco de dados e alterei os padrões de hora e idioma para o portugues e o horario de brasilia.
 na linha 155, tem a permissão do CORS, que funciona simplesmente pela mudança de porta de host.
 
 setup/urls.py --> Por meio de routers, implementei os endpoints solicitados no teste. O objeto router é feito para receber views como instâncias e simplificar o processo de rotas. Como pode ser visto no arquivo, em poucas linhas criei os endpoints.
 A lista de veiculos ficou em outra URL pois os routers não funcionam para todo tipo de view. Como foi necessário uma view apenas para realizar a listagem dos veiculos,
 foi mais simples criar um endpoint por meio do método "as_view" que também é um método genérico do django.

 testeWS/admin --> O django tem um formato de administrador built in, o que significa que ao registrar os modelos nele, você cria uma interface que comanda o seu aplicativo de forma mais intuitiva.

 testeWS/models --> Aqui onde defini meus modelos, fiz alguns comentarios em linhas para não deixar esse leia-me muito grande.
  
 testews/serializers --> O django rest framework tem uma série de serializadores embutidos, os serializadores são como os forms de outras linguagens. O uso de serializadores
 simplifica parte do trabalho de criar um aplicativo no django e também, na minha opinião torna o processo mais intuitivo e reversível, uma vez que há como desserializar facilmente também.
 
 testeWS/views --> As views do django são uma espécie de controlador class based. As vantagens de serem class based são simples, você pode chamar uma série de objetos para suas instancias,
 e elas também são compativeis com function-based views. Neste código, optei por uma abordagem mais simplista, usando model viewsets pude implementar os 3 modelos com seus respectivos
 cruds e também uma listAPIview genérica, que é uma view onde só se pode visualizar dados, sem mais permissões, seguindo o protocolo do teste.
 
 Por fim, alguns comentários gerais:
 Deixei um arquivo 'requirements.txt' para caso venham a rodar esse código em uma venv diferente, segui, nos limites de minha sabedoria os protocolos de programação de pythonistas
 e desejo bons sentimentos a quem ler isto. :)

