# teste_engenharia_de_dados_victor_tintel
Esse é um trabalho feito para Etapa de Case Técnico - Pessoa Engenheira de Dados Júnior


Esse trabalho está sendo entregue em dois formatos, tanto em formato .PY(feito no Visual Studio Code) quanto em formato .IPYNB(Feito no Jupyter Notebook). Para poder testar o código no VSCODE, é preciso ter o Visual Studio Code instalado na máquina, e no formato .IPYNB eu instalei e aconselho ter o Anaconda, porém caso fique muito pesado na máquina pode se abrir pelo GOOGLE COLAB.

No trabalho em si dentro das ferramentas para rodar o código é preciso fazer algumas instalações, então vou colocar elas aqui: vai precisar fazer o ( import pandas as pd) para poder criar um DataFrame, portanto a instalação dele é através do ( pip install pandas ) ; para fazer o webscraping vai precisar fazer a instalação do BeautifulSoup através do ( pip install bs4 ) ; também a instalação do Selenium com o comando ( pip install selenium ) e para finalizar as principais instalações, para poder fazer o import requests, vai precisar fazer ( pip install requests ).

Para começar o trabalho que foi pedido, escolhi 10 bandas que no site é chamado de artistas e fui fazendo a coleta de dados de cada uma delas com o gênero escolhido que foi o rock, nome, número de membros, sites, nome do álbum, data de lançamento do álbum, gravadora do álbum, faixas do álbum, duração de cada faixa do álbum, estilo de cada álbum. 
Depois da coleta dos dados das 10 bandas/artistas pedidos, eu coloquei os dados sempre dentro de uma lista para poder depois jogar em um DataFrame, portanto, criei um DataFrame para cada um desses artistas coletados. Dentro do DataFrame dei uma organizada nos dados, através do comando .T eu transformei as linhas em colunas, renomeei cada uma das colunas para facilitar a visualização e substitui os valores “NONE” por “-“.
Por fim eu exportei os dados no formato JSON como foi pedido porém também exportei os dados em formato excel. 

Considerações Finais: Espero poder ter mostrado um pouco do que aprendi nesse tempo que tenho estudado e me dedicado, quero muito ter a oportunidade de conseguir essa vaga e daqui a um tempo trabalhando nessa empresa e me desenvolvendo, poder voltar a rever esse código e entender o que eu posso melhorar, o que eu fiz de errado para poder todos os dias estar melhorando e aprendendo para estar cada vez escrevendo códigos mais avançados e otimizados.
