import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# PRIMEIRA BANDA DE ROCK METALLICA

pagina_1 = webdriver.Chrome()

pagina_1.get("https://www.discogs.com/pt_BR/artist/18839-Metallica?superFilter=Releases&subFilter=Albums")

page_content_1 = pagina_1.page_source

pagina_artista_1 = BeautifulSoup(page_content_1, "html.parser")

# NOME DA BANDA
nome_artista_1 = pagina_artista_1.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_1 = [nome_artista_1[0].text]

# LISTA DE MEMBROS DA BANDA
membros_artista_1 = pagina_artista_1.find_all("span", {"class":""})
lista_membros_artista_1 = [membros_artista_1[4].text, membros_artista_1[5].text,membros_artista_1[6].text,membros_artista_1[7].text]

# LISTA DE SITES DA BANDA
sites_artista_1 = pagina_artista_1.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_1 = [sites_artista_1[0]["href"], sites_artista_1[1]["href"],sites_artista_1[2]["href"],sites_artista_1[3]["href"],
                        sites_artista_1[4]["href"],sites_artista_1[5]["href"],sites_artista_1[6]["href"],sites_artista_1[7]["href"],
                        sites_artista_1[8]["href"],sites_artista_1[9]["href"],sites_artista_1[10]["href"],sites_artista_1[11]["href"],
                        sites_artista_1[12]["href"],sites_artista_1[13]["href"],sites_artista_1[14]["href"]]

#####################################################################################

metallica_album_1 = webdriver.Chrome()

metallica_album_1.get("https://www.discogs.com/master/6387-Metallica-Kill-Em-All")

metallcica_album_page_content_1 = metallica_album_1.page_source

metallica_pagina_algum_1 = BeautifulSoup(metallcica_album_page_content_1, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_1 = metallica_pagina_algum_1.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_1 = [nome_album_1[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALGUM
ano_lancamento_album_1 = metallica_pagina_algum_1.find_all("time", {"datetime":"1983"})
lista_ano_lancamento_album_1 = [ano_lancamento_album_1[0].text]

# PEGAR A GRAVADORA DO ALBUM
gravadora_album_1 = metallica_pagina_algum_1.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_1 = [gravadora_album_1[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_1 = metallica_pagina_algum_1.find_all("a", {"class":"link_1ctor"})
lista_genero_album_1 = [genero_album_1[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_1 = metallica_pagina_algum_1.find_all("a", {"class":"link_1ctor"})

# COLOCAR OS TIPOS DE ESTILO DENTRO DE UMA LISTA
lista_estilo_album = [estilo_album_1[3].text,estilo_album_1[4].text]

###############################################################################################

faixas_album = metallica_pagina_algum_1.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album = [faixas_album[0].text, faixas_album[1].text, faixas_album[2].text, faixas_album[3].text, faixas_album[4].text,
                     faixas_album[5].text, faixas_album[6].text, faixas_album[7].text, faixas_album[8].text, faixas_album[9].text]

duracao_faixas_album = metallica_pagina_algum_1.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album = [duracao_faixas_album[0].text, duracao_faixas_album[1].text, duracao_faixas_album[2].text, duracao_faixas_album[3].text,
                              duracao_faixas_album[4].text,
                     duracao_faixas_album[5].text, duracao_faixas_album[6].text, duracao_faixas_album[7].text, 
                              duracao_faixas_album[8].text, duracao_faixas_album[9].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_1)
print()
print("NOME DA BANDA:", lista_nome_artista_1)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_1)
print()
print("SITES DA BANDA:", lista_sites_artista_1)
print()
print("NOME DO ÁLBUM:",lista_nome_album_1)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_1)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_1 )
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album)

# SEGUNDA BANDA DE ROCK FOO FIGHTERS

pagina_2 = webdriver.Chrome()

pagina_2.get("https://www.discogs.com/pt_BR/artist/198282-Foo-Fighters?superFilter=Releases&subFilter=Albums")

page_content_2 = pagina_2.page_source

pagina_artista_2 = BeautifulSoup(page_content_2, "html.parser")

nome_artista_2 = pagina_artista_2.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_2 = [nome_artista_2[0].text]

membros_artista_2 = pagina_artista_2.find_all("span", {"class":""})
lista_membros_artista_2 = [membros_artista_2[2].text,membros_artista_2[3].text,membros_artista_2[4].text, membros_artista_2[5].text,membros_artista_2[6].text,membros_artista_2[7].text]

sites_artista_2 = pagina_artista_2.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_2 = [sites_artista_2[0]["href"], sites_artista_2[1]["href"],sites_artista_2[2]["href"],sites_artista_2[3]["href"],
                        sites_artista_2[4]["href"],sites_artista_2[5]["href"],sites_artista_2[6]["href"],sites_artista_2[7]["href"]]
###############################################################################################
foo_fighters_album_2 = webdriver.Chrome()

foo_fighters_album_2.get("https://www.discogs.com/master/62100-Foo-Fighters-Foo-Fighters")

foo_fighters_album_page_content_2 = foo_fighters_album_2.page_source

foo_fighters_pagina_algum_2 = BeautifulSoup(foo_fighters_album_page_content_2, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_2 = foo_fighters_pagina_algum_2.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_2 = [nome_album_2[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALGUM
ano_lancamento_album_2 = foo_fighters_pagina_algum_2.find_all("time", {"datetime":"1995"})
lista_ano_lancamento_album_2 = [ano_lancamento_album_2[0].text]

# PEGAR A GRAVADORA DO ALBUM
gravadora_album_2 = foo_fighters_pagina_algum_2.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_2 = [gravadora_album_2[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_2 = foo_fighters_pagina_algum_2.find_all("a", {"class":"link_1ctor"})
lista_genero_album_2 = [genero_album_2[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_2 = foo_fighters_pagina_algum_2.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_2 = [estilo_album_2[3].text, estilo_album_2[4].text]

# COLOCAR OS TIPOS DE ESTILO DENTRO DE UMA LISTA
lista_estilo_album = [estilo_album_2[3].text,estilo_album_2[4].text]

###############################################################################################

faixas_album_2 = foo_fighters_pagina_algum_2.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_2 = [faixas_album_2[0].text, faixas_album_2[1].text, faixas_album_2[2].text, faixas_album_2[3].text, faixas_album_2[4].text,
                     faixas_album_2[5].text, faixas_album_2[6].text, faixas_album_2[7].text, faixas_album_2[8].text, faixas_album_2[9].text,
                       faixas_album_2[10].text,faixas_album_2[11].text]

duracao_faixas_album_2 = foo_fighters_pagina_algum_2.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_2 = [duracao_faixas_album_2[0].text, duracao_faixas_album_2[1].text, duracao_faixas_album_2[2].text, duracao_faixas_album_2[3].text,
                              duracao_faixas_album_2[4].text,
                     duracao_faixas_album_2[5].text, duracao_faixas_album_2[6].text, duracao_faixas_album_2[7].text, 
                              duracao_faixas_album_2[8].text, duracao_faixas_album_2[9].text,duracao_faixas_album_2[10].text,duracao_faixas_album_2[11].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_2)
print()
print("NOME DA BANDA:", lista_nome_artista_2)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_2)
print()
print("SITES DA BANDA:", lista_sites_artista_2)
print()
print("NOME DO ÁLBUM:",lista_nome_album_2)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_2)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_2)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_2)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_2)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_2)

# TERCEIRA BANDA DE ROCK AC/DC

pagina_3 = webdriver.Chrome()

pagina_3.get("https://www.discogs.com/pt_BR/artist/84752-ACDC?superFilter=Releases&subFilter=Albums")

page_content_3 = pagina_3.page_source

pagina_artista_3 = BeautifulSoup(page_content_3, "html.parser")

# NOME DO ARTISTA
nome_artista_3 = pagina_artista_3.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_3 = [nome_artista_3[0].text]

# MEMBROS DO ARTISTA
membros_artista_3 = pagina_artista_3.find_all("span", {"class":""})
lista_membros_artista_3 = [membros_artista_3[1].text,membros_artista_3[2].text,membros_artista_3[3].text,
                           membros_artista_3[4].text,membros_artista_3[5].text.replace("(7)","")]
# SITE DO ARTISTA                           
sites_artista_3 = pagina_artista_3.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_3 = [sites_artista_3[0]["href"], sites_artista_3[1]["href"],sites_artista_3[2]["href"],sites_artista_3[3]["href"],
                        sites_artista_3[4]["href"],sites_artista_3[5]["href"],sites_artista_3[6]["href"],sites_artista_3[7]["href"]]

###############################################################################################

ac_dc_album_3 = webdriver.Chrome()

ac_dc_album_3.get("https://www.discogs.com/master/8412-ACDC-Dirty-Deeds-Done-Dirt-Cheap")

ac_dc_album_page_content_3 = ac_dc_album_3.page_source

ac_dc_pagina_algum_3 = BeautifulSoup(ac_dc_album_page_content_3, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_3 = ac_dc_pagina_algum_3.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_3 = [nome_album_3[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALGUM
ano_lancamento_album_3 = ac_dc_pagina_algum_3.find_all("time", {"datetime":"1976"})
lista_ano_lancamento_album_3 = [ano_lancamento_album_3[0].text]

# PEGAR A GRAVADORA DO ALBUM
gravadora_album_3 = ac_dc_pagina_algum_3.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_3 = [gravadora_album_3[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_3 = ac_dc_pagina_algum_3.find_all("a", {"class":"link_1ctor"})
lista_genero_album_3 = [genero_album_3[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_3 = ac_dc_pagina_algum_3.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_3 = [estilo_album_3[3].text, estilo_album_3[4].text]

# COLOCAR OS TIPOS DE ESTILO DENTRO DE UMA LISTA
lista_estilo_album = [estilo_album_3[3].text,estilo_album_3[4].text]

###############################################################################################

faixas_album_3 = ac_dc_pagina_algum_3.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_3 = [faixas_album_3[0].text, faixas_album_3[1].text, faixas_album_3[2].text, faixas_album_3[3].text, faixas_album_3[4].text,
                     faixas_album_3[5].text, faixas_album_3[6].text, faixas_album_3[7].text,faixas_album_3[8].text]

duracao_faixas_album_3 = ac_dc_pagina_algum_3.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_3 = [duracao_faixas_album_3[0].text, duracao_faixas_album_3[1].text, duracao_faixas_album_3[2].text, duracao_faixas_album_3[3].text,
                              duracao_faixas_album_3[4].text,
                     duracao_faixas_album_3[5].text, duracao_faixas_album_3[6].text, duracao_faixas_album_3[7].text,duracao_faixas_album_3[8].text]

###############################################################################################


print("GÊNERO:",lista_genero_album_3)
print()
print("NOME DA BANDA:", lista_nome_artista_3)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_3)
print()
print("SITES DA BANDA:", lista_sites_artista_3)
print()
print("NOME DO ÁLBUM:",lista_nome_album_3)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_3)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_3)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_3)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_3)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_3)

# QUARTA BANDA DE ROCK THE ROLLING STONES

pagina_4 = webdriver.Chrome()

pagina_4.get("https://www.discogs.com/artist/20991-The-Rolling-Stones?superFilter=Releases&subFilter=Albums")

page_content_4 = pagina_4.page_source

pagina_artista_4 = BeautifulSoup(page_content_4, "html.parser")

# NOME DO ARTISTA
nome_artista_4 = pagina_artista_4.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_4 = [nome_artista_4[0].text]

# MEMBROS DO ARTISTA
membros_artista_4 = pagina_artista_4.find_all("span", {"class":""})
lista_membros_artista_4 = [membros_artista_4[8].text,membros_artista_4[9].text,membros_artista_4[10].text]

# SITE DO ARTISTA                           
sites_artista_4 = pagina_artista_4.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_4 = [sites_artista_4[0]["href"], sites_artista_4[1]["href"],sites_artista_4[2]["href"],sites_artista_4[3]["href"],
                        sites_artista_4[4]["href"],sites_artista_4[5]["href"],sites_artista_4[6]["href"],sites_artista_4[7]["href"],
                        sites_artista_4[8]["href"],sites_artista_4[9]["href"],sites_artista_4[10]["href"],sites_artista_4[11]["href"],
                        sites_artista_4[12]["href"],sites_artista_4[13]["href"],sites_artista_4[14]["href"],sites_artista_4[15]["href"],
                        sites_artista_4[16]["href"],sites_artista_4[17]["href"],sites_artista_4[18]["href"],sites_artista_4[19]["href"],
                        sites_artista_4[20]["href"],sites_artista_4[21]["href"],sites_artista_4[22]["href"],sites_artista_4[23]["href"],
                        sites_artista_4[24]["href"],sites_artista_4[25]["href"],sites_artista_4[26]["href"],sites_artista_4[27]["href"],
                        sites_artista_4[28]["href"],sites_artista_4[29]["href"],sites_artista_4[30]["href"]]

###############################################################################################

rolling_album_4 = webdriver.Chrome()

rolling_album_4.get("https://www.discogs.com/master/30169-The-Rolling-Stones-12-X-5")

rolling_album_page_content_4 = rolling_album_4.page_source

rolling_pagina_algum_4 = BeautifulSoup(rolling_album_page_content_4, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_4 = rolling_pagina_algum_4.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_4 = [nome_album_4[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALGUM
ano_lancamento_album_4 = rolling_pagina_algum_4.find_all("time", {"datetime":"1964"})
lista_ano_lancamento_album_4 = [ano_lancamento_album_4[0].text]

# PEGAR A GRAVADORA DO ALBUM
gravadora_album_4 = rolling_pagina_algum_4.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_4 = [gravadora_album_4[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_4 = rolling_pagina_algum_4.find_all("a", {"class":"link_1ctor"})
lista_genero_album_4 = [genero_album_4[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_4 = rolling_pagina_algum_4.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_4 = [estilo_album_4[2].text, estilo_album_4[3].text]

# COLOCAR OS TIPOS DE ESTILO DENTRO DE UMA LISTA
lista_estilo_album = [estilo_album_4[3].text,estilo_album_4[4].text]

###############################################################################################

faixas_album_4 = rolling_pagina_algum_4.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_4 = [faixas_album_4[0].text, faixas_album_4[1].text, faixas_album_4[2].text, faixas_album_4[3].text, faixas_album_4[4].text,
                     faixas_album_4[5].text, faixas_album_4[6].text, faixas_album_4[7].text,faixas_album_4[8].text,faixas_album_4[9].text,
                       faixas_album_4[10].text,faixas_album_4[11].text]

duracao_faixas_album_4 = rolling_pagina_algum_4.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_4 = [duracao_faixas_album_4[0].text, duracao_faixas_album_4[1].text, duracao_faixas_album_4[2].text, duracao_faixas_album_4[3].text,
                              duracao_faixas_album_4[4].text,
                     duracao_faixas_album_4[5].text, duracao_faixas_album_4[6].text, duracao_faixas_album_4[7].text,duracao_faixas_album_4[8].text,
                               duracao_faixas_album_4[9].text,duracao_faixas_album_4[10].text,duracao_faixas_album_4[11].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_4)
print()
print("NOME DA BANDA:", lista_nome_artista_4)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_4)
print()
print("SITES DA BANDA:", lista_sites_artista_4)
print()
print("NOME DO ÁLBUM:",lista_nome_album_4)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_4)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_4)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_4)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_4)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_4)

# QUINTA BANDA DE RED HOT CHILI PEPPERS

pagina_5 = webdriver.Chrome()

pagina_5.get("https://www.discogs.com/artist/92476-Red-Hot-Chili-Peppers?superFilter=Releases&subFilter=Albums")

page_content_5 = pagina_5.page_source

pagina_artista_5= BeautifulSoup(page_content_5, "html.parser")

# NOME DO ARTISTA
nome_artista_5 = pagina_artista_5.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_5= [nome_artista_5[0].text]

# MEMBROS DO ARTISTA
membros_artista_5 = pagina_artista_5.find_all("span", {"class":""})
lista_membros_artista_5 = [membros_artista_5[1].text,membros_artista_5[2].text,membros_artista_5[3].text,membros_artista_5[4].text]

# SITE DO ARTISTA                           
sites_artista_5 = pagina_artista_5.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_5 = [sites_artista_5[0]["href"], sites_artista_5[1]["href"],sites_artista_5[2]["href"],sites_artista_5[3]["href"],
                        sites_artista_5[4]["href"],sites_artista_5[5]["href"],sites_artista_5[6]["href"],sites_artista_5[7]["href"]]

###############################################################################################

red_album_5 = webdriver.Chrome()

red_album_5.get("https://www.discogs.com/master/42499-The-Red-Hot-Chili-Peppers-The-Red-Hot-Chili-Peppers")

red_album_page_content_5 = red_album_5.page_source

red_pagina_algum_5 = BeautifulSoup(red_album_page_content_5, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_5 = red_pagina_algum_5.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_5 = [nome_album_5[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALGUM
ano_lancamento_album_5 = red_pagina_algum_5.find_all("time", {"datetime":"1984"})
lista_ano_lancamento_album_5 = [ano_lancamento_album_5[0].text]

# PEGAR A GRAVADORA DO ALBUM
gravadora_album_5 = red_pagina_algum_5.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_5 = [gravadora_album_5[1].text.replace("(3)","")]

# PEGAR O GÊNERO DO ALBUM
genero_album_5 = red_pagina_algum_5.find_all("a", {"class":"link_1ctor"})
lista_genero_album_5 = [genero_album_5[3].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_5 = red_pagina_algum_5.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_5 = [estilo_album_5[6].text, estilo_album_5[5].text]

###############################################################################################

faixas_album_5 = red_pagina_algum_5.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_5 = [faixas_album_5[0].text, faixas_album_5[1].text, faixas_album_5[2].text, faixas_album_5[3].text, faixas_album_5[4].text,
                     faixas_album_5[5].text, faixas_album_5[6].text, faixas_album_5[7].text,faixas_album_5[8].text,faixas_album_5[9].text,
                       faixas_album_5[10].text]

duracao_faixas_album_5 = red_pagina_algum_5.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_5 = [duracao_faixas_album_5[0].text, duracao_faixas_album_5[1].text, duracao_faixas_album_5[2].text, duracao_faixas_album_5[3].text,
                              duracao_faixas_album_5[4].text,
                     duracao_faixas_album_5[5].text, duracao_faixas_album_5[6].text, duracao_faixas_album_5[7].text,duracao_faixas_album_5[8].text,
                               duracao_faixas_album_5[9].text,duracao_faixas_album_5[10].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_5)
print()
print("NOME DA BANDA:", lista_nome_artista_5)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_5)
print()
print("SITES DA BANDA:", lista_sites_artista_5)
print()
print("NOME DO ÁLBUM:",lista_nome_album_5)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_5)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_5)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_5)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_5)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_5)

# SEXTA BANDA DE ROCK GREEN DAY

pagina_6 = webdriver.Chrome()

pagina_6.get("https://www.discogs.com/artist/251593-Green-Day?superFilter=Releases&subFilter=Albums")

page_content_6 = pagina_6.page_source

pagina_artista_6 = BeautifulSoup(page_content_6, "html.parser")

# NOME DO ARTISTA
nome_artista_6 = pagina_artista_6.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_6= [nome_artista_6[0].text]

# MEMBROS DO ARTISTA
membros_artista_6 = pagina_artista_6.find_all("span", {"class":""})
lista_membros_artista_6 = [membros_artista_6[2].text,membros_artista_6[3].text,membros_artista_6[4].text]

# SITE DO ARTISTA                           
sites_artista_6 = pagina_artista_6.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_6 = [sites_artista_6[0]["href"], sites_artista_6[1]["href"],sites_artista_6[2]["href"],sites_artista_6[3]["href"],
                        sites_artista_6[4]["href"],sites_artista_6[5]["href"],sites_artista_6[6]["href"],sites_artista_6[7]["href"],
                        sites_artista_6[8]["href"]]

###############################################################################################

gren_album_6 = webdriver.Chrome()

gren_album_6.get("https://www.discogs.com/master/33170-Green-Day-Dookie")

gren_album_page_content_6 = gren_album_6.page_source

gren_pagina_album_6 = BeautifulSoup(gren_album_page_content_6, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_6 = gren_pagina_album_6.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_6 = [nome_album_6[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALBUM
ano_lancamento_album_6 = gren_pagina_album_6.find_all("time", {"datetime":"1994"})
lista_ano_lancamento_album_6 = [ano_lancamento_album_6[0].text]


# PEGAR A GRAVADORA DO ALBUM
gravadora_album_6 = gren_pagina_album_6.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_6 = [gravadora_album_6[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_6 = gren_pagina_album_6.find_all("a", {"class":"link_1ctor"})
lista_genero_album_6 = [genero_album_6[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_6 = gren_pagina_album_6.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_6 = [estilo_album_6[3].text, estilo_album_6[4].text]

###############################################################################################

faixas_album_6 = gren_pagina_album_6.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_6 = [faixas_album_6[0].text, faixas_album_6[1].text, faixas_album_6[2].text, faixas_album_6[3].text, faixas_album_6[4].text,
                     faixas_album_6[5].text, faixas_album_6[6].text, faixas_album_6[7].text,faixas_album_6[8].text,faixas_album_6[9].text,
                       faixas_album_6[10].text,  faixas_album_6[11].text,  faixas_album_6[12].text,  faixas_album_6[13].text,  faixas_album_6[14].text]

duracao_faixas_album_6 = gren_pagina_album_6.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_6 = [duracao_faixas_album_6[0].text, duracao_faixas_album_6[1].text, duracao_faixas_album_6[2].text, duracao_faixas_album_6[3].text,
                              duracao_faixas_album_6[4].text,
                     duracao_faixas_album_6[5].text, duracao_faixas_album_6[6].text, duracao_faixas_album_6[7].text,duracao_faixas_album_6[8].text,
                               duracao_faixas_album_6[9].text,duracao_faixas_album_6[10].text,duracao_faixas_album_6[11].text,
                              duracao_faixas_album_6[12].text,duracao_faixas_album_6[13].text,duracao_faixas_album_6[14].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_6)
print()
print("NOME DA BANDA:", lista_nome_artista_6)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_6)
print()
print("SITES DA BANDA:", lista_sites_artista_6)
print()
print("NOME DO ÁLBUM:",lista_nome_album_6)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_6)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_6)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_6)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_6)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_6)

# SETIMA BANDA DE ROCK GUNS N ROSES

pagina_7 = webdriver.Chrome()

pagina_7.get("https://www.discogs.com/artist/124535-Guns-N-Roses?superFilter=Releases&subFilter=Albums")

page_content_7 = pagina_7.page_source

pagina_artista_7 = BeautifulSoup(page_content_7, "html.parser")

# NOME DO ARTISTA
nome_artista_7 = pagina_artista_7.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_7= [nome_artista_7[0].text]

# MEMBROS DO ARTISTA
membros_artista_7 = pagina_artista_7.find_all("span", {"class":""})
lista_membros_artista_7 = [membros_artista_7[1].text,membros_artista_7[7].text,membros_artista_7[2].text,membros_artista_7[3].text,
                          membros_artista_7[4].text,membros_artista_7[5].text,membros_artista_7[6].text]

# SITE DO ARTISTA                           
sites_artista_7 = pagina_artista_7.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_7 = [sites_artista_7[0]["href"], sites_artista_7[1]["href"],sites_artista_7[2]["href"],sites_artista_7[3]["href"],
                        sites_artista_7[4]["href"],sites_artista_7[5]["href"],sites_artista_7[6]["href"],sites_artista_7[7]["href"],
                        sites_artista_7[8]["href"]]


###############################################################################################

guns_album_7 = webdriver.Chrome()

guns_album_7.get("https://www.discogs.com/master/9586-Guns-N-Roses-Use-Your-Illusion-II")

guns_album_page_content_7 = guns_album_7.page_source

guns_pagina_album_7 = BeautifulSoup(guns_album_page_content_7, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_7 = guns_pagina_album_7.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_7 = [nome_album_7[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALBUM
ano_lancamento_album_7 = guns_pagina_album_7.find_all("time", {"datetime":"1991"})
lista_ano_lancamento_album_7 = [ano_lancamento_album_7[0].text]


# PEGAR A GRAVADORA DO ALBUM
gravadora_album_7 = guns_pagina_album_7.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_7 = [gravadora_album_7[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_7 = guns_pagina_album_7.find_all("a", {"class":"link_1ctor"})
lista_genero_album_7 = [genero_album_7[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_7 = guns_pagina_album_7.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_7 = [estilo_album_7[3].text, estilo_album_7[4].text, estilo_album_7[5].text]

###############################################################################################

faixas_album_7 = guns_pagina_album_7.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_7 = [faixas_album_7[0].text, faixas_album_7[1].text, faixas_album_7[2].text, faixas_album_7[3].text, faixas_album_7[4].text,
                     faixas_album_7[5].text, faixas_album_7[6].text, faixas_album_7[7].text,faixas_album_7[8].text,faixas_album_7[9].text,
                       faixas_album_7[10].text,  faixas_album_7[11].text,  faixas_album_7[12].text,  faixas_album_7[13].text]

duracao_faixas_album_7 = guns_pagina_album_7.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_7 = [duracao_faixas_album_7[0].text, duracao_faixas_album_7[1].text, duracao_faixas_album_7[2].text, duracao_faixas_album_7[3].text,
                              duracao_faixas_album_7[4].text,
                     duracao_faixas_album_7[5].text, duracao_faixas_album_7[6].text, duracao_faixas_album_7[7].text,duracao_faixas_album_7[8].text,
                               duracao_faixas_album_7[9].text,duracao_faixas_album_7[10].text,duracao_faixas_album_7[11].text,
                              duracao_faixas_album_7[12].text,duracao_faixas_album_7[13].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_7)
print()
print("NOME DA BANDA:", lista_nome_artista_7)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_7)
print()
print("SITES DA BANDA:", lista_sites_artista_7)
print()
print("NOME DO ÁLBUM:",lista_nome_album_7)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_7)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_7)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_7)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_7)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_7)

# OITAVA BANDA DE ROCK COLDPLAY

pagina_8 = webdriver.Chrome()

pagina_8.get("https://www.discogs.com/artist/29735-Coldplay?superFilter=Releases&subFilter=Albums")

page_content_8 = pagina_8.page_source

pagina_artista_8 = BeautifulSoup(page_content_8, "html.parser")

# NOME DO ARTISTA
nome_artista_8 = pagina_artista_8.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_8= [nome_artista_8[0].text]

# MEMBROS DO ARTISTA
membros_artista_8 = pagina_artista_8.find_all("span", {"class":""})
lista_membros_artista_8 = [membros_artista_8[5].text,membros_artista_8[7].text,membros_artista_8[6].text,membros_artista_8[3].text,
                          membros_artista_8[4].text]

# SITE DO ARTISTA                           
sites_artista_8 = pagina_artista_8.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_8 = [sites_artista_8[0]["href"], sites_artista_8[1]["href"],sites_artista_8[2]["href"],sites_artista_8[3]["href"],
                        sites_artista_8[4]["href"],sites_artista_8[5]["href"]]

###############################################################################################

cold_album_8 = webdriver.Chrome()

cold_album_8.get("https://www.discogs.com/master/3334-Coldplay-Parachutes")

cold_album_page_content_8 = cold_album_8.page_source

cold_pagina_album_8 = BeautifulSoup(cold_album_page_content_8, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_8 = cold_pagina_album_8.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_8 = [nome_album_8[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALBUM
ano_lancamento_album_8 = cold_pagina_album_8.find_all("time", {"datetime":"2000"})
lista_ano_lancamento_album_8 = [ano_lancamento_album_8[0].text]


# PEGAR A GRAVADORA DO ALBUM
gravadora_album_8 = cold_pagina_album_8.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_8 = [gravadora_album_8[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_8 = cold_pagina_album_8.find_all("a", {"class":"link_1ctor"})
lista_genero_album_8 = [genero_album_8[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_8 = cold_pagina_album_8.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_8 = [estilo_album_8[3].text, estilo_album_8[4].text]

###############################################################################################

faixas_album_8 = cold_pagina_album_8.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_8 = [faixas_album_8[0].text, faixas_album_8[1].text, faixas_album_8[2].text, faixas_album_8[3].text, faixas_album_8[4].text,
                     faixas_album_8[5].text, faixas_album_8[6].text, faixas_album_8[7].text,faixas_album_8[8].text,faixas_album_8[9].text,
                       faixas_album_8[10].text]

duracao_faixas_album_8 = cold_pagina_album_8.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_8 = [duracao_faixas_album_8[0].text, duracao_faixas_album_8[1].text, duracao_faixas_album_8[2].text, duracao_faixas_album_8[3].text,
                              duracao_faixas_album_8[4].text,
                     duracao_faixas_album_8[5].text, duracao_faixas_album_8[6].text, duracao_faixas_album_8[7].text,duracao_faixas_album_8[8].text,
                               duracao_faixas_album_8[9].text,duracao_faixas_album_8[10].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_8)
print()
print("NOME DA BANDA:", lista_nome_artista_8)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_8)
print()
print("SITES DA BANDA:", lista_sites_artista_8)
print()
print("NOME DO ÁLBUM:",lista_nome_album_8)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_8)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_8)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_8)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_8)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_8)

# NONA BANDA DE ROCK COLDPLAY

pagina_9 = webdriver.Chrome()

pagina_9.get("https://www.discogs.com/artist/40029-Linkin-Park?superFilter=Releases&subFilter=Albums")

page_content_9 = pagina_9.page_source

pagina_artista_9 = BeautifulSoup(page_content_9, "html.parser")

# NOME DO ARTISTA
nome_artista_9 = pagina_artista_9.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_9 = [nome_artista_9[0].text]

# MEMBROS DO ARTISTA
membros_artista_9 = pagina_artista_9.find_all("span", {"class":""})
lista_membros_artista_9 = [membros_artista_9[4].text,membros_artista_9[5].text,membros_artista_9[6].text,membros_artista_9[7].text,
                          membros_artista_9[8].text,membros_artista_9[9].text]

# SITE DO ARTISTA                           
sites_artista_9 = pagina_artista_9.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_9 = [sites_artista_9[0]["href"], sites_artista_9[1]["href"],sites_artista_9[2]["href"],sites_artista_9[3]["href"],
                        sites_artista_9[4]["href"],sites_artista_9[5]["href"],sites_artista_9[6]["href"]]

###############################################################################################

park_album_9 = webdriver.Chrome()

park_album_9.get("https://www.discogs.com/master/74519-Linkin-Park-Hybrid-Theory")

park_album_page_content_9 = park_album_9.page_source

park_pagina_album_9 = BeautifulSoup(park_album_page_content_9, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_9 = park_pagina_album_9.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_9 = [nome_album_9[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALBUM
ano_lancamento_album_9 = park_pagina_album_9.find_all("time", {"datetime":"2000"})
lista_ano_lancamento_album_9 = [ano_lancamento_album_9[0].text]


# PEGAR A GRAVADORA DO ALBUM
gravadora_album_9 = park_pagina_album_9.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_9 = [gravadora_album_9[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_9 = park_pagina_album_9.find_all("a", {"class":"link_1ctor"})
lista_genero_album_9 = [genero_album_9[4].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_9 = park_pagina_album_9.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_9 = [estilo_album_9[5].text, estilo_album_9[6].text]

###############################################################################################

faixas_album_9 = park_pagina_album_9.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_9 = [faixas_album_9[0].text, faixas_album_9[1].text, faixas_album_9[2].text, faixas_album_9[3].text, faixas_album_9[4].text,
                     faixas_album_9[5].text, faixas_album_9[6].text, faixas_album_9[7].text,faixas_album_9[8].text,faixas_album_9[9].text,
                       faixas_album_9[10].text,faixas_album_9[11].text]

duracao_faixas_album_9= park_pagina_album_9.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_9 = [duracao_faixas_album_9[0].text, duracao_faixas_album_9[1].text, duracao_faixas_album_9[2].text, duracao_faixas_album_9[3].text,
                              duracao_faixas_album_9[4].text,
                     duracao_faixas_album_9[5].text, duracao_faixas_album_9[6].text, duracao_faixas_album_9[7].text,duracao_faixas_album_9[8].text,
                               duracao_faixas_album_9[9].text,duracao_faixas_album_9[10].text,duracao_faixas_album_9[11].text]

###############################################################################################

print("GÊNERO:",lista_genero_album_9)
print()
print("NOME DA BANDA:", lista_nome_artista_9)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_9)
print()
print("SITES DA BANDA:", lista_sites_artista_9)
print()
print("NOME DO ÁLBUM:",lista_nome_album_9)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_9)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_9)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_9)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_9)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_9)

# DÉCIMA BANDA DE ROCK ARTIC MONKEYS

pagina_10 = webdriver.Chrome()

pagina_10.get("https://www.discogs.com/artist/391170-Arctic-Monkeys?superFilter=Releases&subFilter=Albums")

page_content_10 = pagina_10.page_source

pagina_artista_10 = BeautifulSoup(page_content_10, "html.parser")

# NOME DO ARTISTA
nome_artista_10 = pagina_artista_10.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_artista_10 = [nome_artista_10[0].text]

# MEMBROS DO ARTISTA
membros_artista_10 = pagina_artista_10.find_all("span", {"class":""})
lista_membros_artista_10 = [membros_artista_10[4].text,membros_artista_10[5].text.replace("(2)",""),membros_artista_10[2].text,membros_artista_10[3].text]

# SITE DO ARTISTA                           
sites_artista_10 = pagina_artista_10.find_all("a", {"class":"link_1ctor link_3fSf-"})

lista_sites_artista_10 = [sites_artista_10[0]["href"], sites_artista_10[1]["href"],sites_artista_10[2]["href"],sites_artista_10[3]["href"],
                        sites_artista_10[4]["href"],sites_artista_10[5]["href"],sites_artista_10[6]["href"],sites_artista_10[7]["href"]]

###############################################################################################

artic_album_10 = webdriver.Chrome()

artic_album_10.get("https://www.discogs.com/master/76279-Arctic-Monkeys-Whatever-People-Say-I-Am-Thats-What-Im-Not")

artic_album_page_content_10 = artic_album_10.page_source

artic_pagina_album_10 = BeautifulSoup(artic_album_page_content_10, "html.parser")

# PEGAR O NOME DO ALBUM
nome_album_10 = artic_pagina_album_10.find_all("h1", {"class":"MuiTypography-root MuiTypography-headLineXL title_1q3xW css-12sap66"})
lista_nome_album_10 = [nome_album_10[0].text]

# PEGAR O ANO DE LANÇAMENTO DO ALBUM
ano_lancamento_album_10 = artic_pagina_album_10.find_all("time", {"datetime":"2006"})
lista_ano_lancamento_album_10 = [ano_lancamento_album_10[0].text]


# PEGAR A GRAVADORA DO ALBUM
gravadora_album_10 = artic_pagina_album_10.find_all("a", {"class":"MuiTypography-root MuiTypography-labelSmall MuiLink-root MuiLink-underlineAlways css-glhfjc"})
lista_gravadora_album_10 = [gravadora_album_10[1].text]

# PEGAR O GÊNERO DO ALBUM
genero_album_10 = artic_pagina_album_10.find_all("a", {"class":"link_1ctor"})
lista_genero_album_10 = [genero_album_10[2].text]

# PEGAR O ESTILO DO ALBUM
estilo_album_10 = artic_pagina_album_10.find_all("a", {"class":"link_1ctor"})
lista_estilo_album_10 = [estilo_album_10[3].text]

###############################################################################################

faixas_album_10 = artic_pagina_album_10.find_all("td", {"class":"trackTitleNoArtist_ANE8Q"})
lista_faixas_album_10 = [faixas_album_10[0].text, faixas_album_10[1].text, faixas_album_10[2].text, faixas_album_10[3].text, faixas_album_10[4].text,
                     faixas_album_10[5].text, faixas_album_10[6].text, faixas_album_10[7].text,faixas_album_10[8].text,faixas_album_10[9].text,
                       faixas_album_10[10].text,faixas_album_10[11].text,faixas_album_10[12].text]

duracao_faixas_album_10 = artic_pagina_album_10.find_all("td", {"class":"duration_25zMZ"})
lista_duracao_faixas_album_10 = [duracao_faixas_album_10[0].text, duracao_faixas_album_10[1].text, duracao_faixas_album_10[2].text, 
                                 duracao_faixas_album_10[3].text,
                              duracao_faixas_album_10[4].text,
                     duracao_faixas_album_10[5].text, duracao_faixas_album_10[6].text, duracao_faixas_album_10[7].text,duracao_faixas_album_10[8].text,
                               duracao_faixas_album_10[9].text,duracao_faixas_album_10[10].text,duracao_faixas_album_10[11].text,
                                duracao_faixas_album_10[12].text]

###############################################################################################


print("GÊNERO:",lista_genero_album_10)
print()
print("NOME DA BANDA:", lista_nome_artista_10)
print()
print("MEMBROS DA BANDA:", lista_membros_artista_10)
print()
print("SITES DA BANDA:", lista_sites_artista_10)
print()
print("NOME DO ÁLBUM:",lista_nome_album_10)
print()
print("ESTILO DO ÁLBUM:",lista_estilo_album_10)
print()
print("ANO DE LANÇAMENTO DO ÁLBUM:",lista_ano_lancamento_album_10)
print()
print("GRAVADORA DO ÁLBUM:",lista_gravadora_album_10)
print()
print("FAIXAS DO ÁLBUM:",lista_faixas_album_10)
print()
print("DURAÇÃO DE CADA FAIXA DO ÁLBUM:",lista_duracao_faixas_album_10)

# PRIMEIRA BANDA DE ROCK METALLICA
lista_completa_1 = [lista_genero_album_1, lista_nome_artista_1, lista_membros_artista_1, lista_sites_artista_1, lista_nome_album_1, lista_estilo_album,
                 lista_ano_lancamento_album_1, lista_gravadora_album_1, lista_faixas_album, lista_duracao_faixas_album]

# SEGUNDA BANDA DE ROCK FOO FIGHTERS
lista_completa_2 = [lista_genero_album_2, lista_nome_artista_2, lista_membros_artista_2, lista_sites_artista_2, lista_nome_album_2, lista_estilo_album_2,
                 lista_ano_lancamento_album_2, lista_gravadora_album_2, lista_faixas_album_2, lista_duracao_faixas_album_2]

# TERCEIRA BANDA DE ROCK AC/DC
lista_completa_3 = [lista_genero_album_3, lista_nome_artista_3, lista_membros_artista_3, lista_sites_artista_3, lista_nome_album_3, lista_estilo_album_3,
                 lista_ano_lancamento_album_3, lista_gravadora_album_3, lista_faixas_album_3, lista_duracao_faixas_album_3]

# QUARTA BANDA DE ROCK THE ROLLING STONES 
lista_completa_4 = [lista_genero_album_4, lista_nome_artista_4, lista_membros_artista_4, lista_sites_artista_4, lista_nome_album_4, lista_estilo_album_4,
                 lista_ano_lancamento_album_4, lista_gravadora_album_4, lista_faixas_album_4, lista_duracao_faixas_album_4]

# QUINTA BANDA DE RED HOT CHILI PEPPERS
lista_completa_5 = [lista_genero_album_5, lista_nome_artista_5, lista_membros_artista_5, lista_sites_artista_5, lista_nome_album_5, lista_estilo_album_5,
                 lista_ano_lancamento_album_5, lista_gravadora_album_5, lista_faixas_album_5, lista_duracao_faixas_album_5]
                 
# SEXTA BANDA DE ROCK GREEN DAY
lista_completa_6 = [lista_genero_album_6, lista_nome_artista_6, lista_membros_artista_6, lista_sites_artista_6, lista_nome_album_6, lista_estilo_album_6,
                 lista_ano_lancamento_album_6, lista_gravadora_album_6, lista_faixas_album_6, lista_duracao_faixas_album_6]

# SETIMA BANDA DE ROCK GUNS N ROSES
lista_completa_7 = [lista_genero_album_7, lista_nome_artista_7, lista_membros_artista_7, lista_sites_artista_7, lista_nome_album_7, lista_estilo_album_7,
                 lista_ano_lancamento_album_7, lista_gravadora_album_7, lista_faixas_album_7, lista_duracao_faixas_album_7]

# OITAVA BANDA DE ROCK COLDPLAY
lista_completa_8 = [lista_genero_album_8, lista_nome_artista_8, lista_membros_artista_8, lista_sites_artista_8, lista_nome_album_8, lista_estilo_album_8,
                 lista_ano_lancamento_album_8, lista_gravadora_album_8, lista_faixas_album_8, lista_duracao_faixas_album_8]

# NONA BANDA DE ROCK COLDPLAY
lista_completa_9 = [lista_genero_album_9, lista_nome_artista_9, lista_membros_artista_9, lista_sites_artista_9, lista_nome_album_9, lista_estilo_album_9,
                 lista_ano_lancamento_album_9, lista_gravadora_album_9, lista_faixas_album_9, lista_duracao_faixas_album_9]

# DÉCIMA BANDA DE ROCK ARTIC MONKEYS
lista_completa_10 = [lista_genero_album_10, lista_nome_artista_10, lista_membros_artista_10, lista_sites_artista_10, lista_nome_album_10, lista_estilo_album_10,
                 lista_ano_lancamento_album_10, lista_gravadora_album_10, lista_faixas_album_10, lista_duracao_faixas_album_10]


# BANDA DE ROCK METALLICA
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_1 = pd.DataFrame(lista_completa_1)

banda_1_oficial = banda_1.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_1_of = banda_1_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_1_of = banda_1_of.fillna("-")
banda_1_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_1_of.to_json("dados_banda_1.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_1_of.to_excel("dados_banda_1.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# BANDA DE ROCK FOO FIGHTERS
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_2 = pd.DataFrame(lista_completa_2)

banda_2_oficial = banda_2.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_2_of = banda_2_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_2_of = banda_2_of.fillna("-")
banda_2_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_2_of.to_json("dados_banda_2.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_2_of.to_excel("dados_banda_2.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# BANDA DE ROCK AC/DC
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_3 = pd.DataFrame(lista_completa_3)

banda_3_oficial = banda_3.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_3_of = banda_3_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_3_of = banda_3_of.fillna("-")
banda_3_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_3_of.to_json("dados_banda_3.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_3_of.to_excel("dados_banda_3.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# BANDA DE ROCK THE ROLLING STONES
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_4 = pd.DataFrame(lista_completa_4)

banda_4_oficial = banda_4.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_4_of = banda_4_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_4_of = banda_4_of.fillna("-")
banda_4_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_4_of.to_json("dados_banda_4.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_4_of.to_excel("dados_banda_4.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# QUINTA BANDA DE RED HOT CHILI PEPPERS
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_5 = pd.DataFrame(lista_completa_5)

banda_5_oficial = banda_5.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_5_of = banda_5_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_5_of = banda_5_of.fillna("-")
banda_5_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_5_of.to_json("dados_banda_5.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_5_of.to_excel("dados_banda_5.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# SEXTA BANDA DE ROCK GREEN DAY
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_6 = pd.DataFrame(lista_completa_6)

banda_6_oficial = banda_6.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_6_of = banda_6_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_6_of = banda_6_of.fillna("-")
banda_6_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_6_of.to_json("dados_banda_6.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_6_of.to_excel("dados_banda_6.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# SETIMA BANDA DE ROCK GUNS N ROSES
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_7 = pd.DataFrame(lista_completa_7)

banda_7_oficial = banda_7.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_7_of = banda_7_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_7_of = banda_7_of.fillna("-")
banda_7_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_7_of.to_json("dados_banda_7.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_7_of.to_excel("dados_banda_7.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# OITAVA BANDA DE ROCK COLDPLAY
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_8 = pd.DataFrame(lista_completa_8)

banda_8_oficial = banda_8.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_8_of = banda_8_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_8_of = banda_8_of.fillna("-")
banda_8_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_8_of.to_json("dados_banda_8.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_8_of.to_excel("dados_banda_8.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# NONA BANDA DE ROCK COLDPLAY
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_9 = pd.DataFrame(lista_completa_9)

banda_9_oficial = banda_9.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_9_of = banda_9_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_9_of = banda_9_of.fillna("-")
banda_9_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_9_of.to_json("dados_banda_9.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_9_of.to_excel("dados_banda_9.xlsx", index=False)

#-------------------------------------------------------------------------------------------------------------------------

# DÉCIMA BANDA DE ROCK ARTIC MONKEYS
# SALVANDO OS DADOS DA BANDA EM UM DATAFRAME ATRAVÉS DO PANDAS

banda_10 = pd.DataFrame(lista_completa_10)

banda_10_oficial = banda_10.T

# ALTERANDO OS NOMES DAS COLUNAS
banda_10_of = banda_10_oficial.rename(columns={0:"Gênero", 1:"Nome",2:"Membros", 3:"Sites", 4:"Nome do Álbum",
                                             5:"Estilos do álbum",6:"Ano de lançamento do álbum", 7:" Gravadora do álbum",
                                             8:"Faixas do álbum", 9:"Duração de cada faixa do álbum"})

# SUBSTITUINDO OS VALORES NONES POR -
banda_10_of = banda_10_of.fillna("-")
banda_10_of

# EXPORTANTO OS DADOS DA BANDA EM FORMATO JSON
banda_10_of.to_json("dados_banda_10.json", orient="records")

# EXPORTANTO OS DADOS DA BANDA EM FORMATO EXCEL
banda_10_of.to_excel("dados_banda_10.xlsx", index=False)


#-------------------------------------------------------------------------------------------------------------------------