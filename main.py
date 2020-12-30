import requests
from time import sleep
from bs4 import BeautifulSoup
from utils import * 


url = 'https://programathor.com.br/jobs-python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')


list_options = []
for option in html.find_all('option'):
    save_list_options = add_list(list_options, option.text)

list_save_beneftis = []
list_save_requerimentes = []
for jobs in html.select('.cell-list-content'):
    jobs_title = jobs.find_all('h3')
    for name_jobs in jobs_title:
        name = name_jobs.contents[0]
    
    list_requeriments = []
    list_beneftis = []
    beneftis = jobs.find_all('span')
    for text_name_beneftis in beneftis:
        if text_name_beneftis.text in save_list_options:
            save_list_requerimentes = add_list(list_requeriments, text_name_beneftis.text)
        else:
            save_list_beneftis = add_list(list_beneftis, text_name_beneftis.text)
    
    print(name)
    print(save_list_beneftis)
    print(save_list_requerimentes)
    print('-' * 80)

    list_save_beneftis.append(save_list_beneftis)
    list_save_requerimentes.append(save_list_requerimentes)

print('Analizando Beneficios.....')
sleep(3)
print('-'* 70)
print('Júnior, Pleno e Sênior')
# pegando quantas vagas tem de  Juniors, Plenos e Senior
list_levels_jps = jps_level(list_save_beneftis)
details_levels(list_levels_jps)

sleep(2)
print('-'* 70)
print('Fora ou dentro')
# pegando quantas vagas que aceitão candidatos de fora ou não
list_out_inside = city_out_inside(list_save_beneftis)
details_out_inside(list_out_inside)

sleep(2)
print('-'* 70)
print('Remoto ou não remoto')
# pegando quantas vagas são remotas ou não
list_remote_or_noremote = remote(list_save_beneftis)
details_remote_noremote(list_remote_or_noremote)
