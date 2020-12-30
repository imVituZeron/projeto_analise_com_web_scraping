def add_list(save_list, value):
    save_list.append(value)
    return save_list


def jps_level(save_list):
    j_jobs = 0
    p_jobs = 0
    s_jobs = 0

    for benes in save_list:
        for items in benes:
            if items == 'Júnior':
                j_jobs += 1
            elif items == 'Pleno':
                p_jobs += 1
            elif items == 'Sênior':
                s_jobs += 1
        
    list_levels_jps = [j_jobs, p_jobs, s_jobs]
    return list_levels_jps


def city_out_inside(save_list):
    city_out_jobs = 0
    city_inside_jobs = 0

    for benes in save_list:
        for items in benes:
            if items == 'Aceita candidatos de fora':
                city_out_jobs += 1
            elif items == 'Não aceita candidatos de fora':
                city_inside_jobs += 1
        
    list_out_inside = [city_out_jobs, city_inside_jobs]
    return list_out_inside


def remote(save_list):
    remote = 0
    no_remote = 0

    for benes in save_list:
        if benes[1] == 'Remoto':
            remote += 1
        elif benes[1] != 'Remoto':
            no_remote += 1

    list_remote_or_noremote = [remote, no_remote]
    return list_remote_or_noremote
    

def details_levels(save_list):

    if save_list[0] <= 1:
        print(f'Tem {save_list[0]} vaga que nessecita de Júniors')
    else: 
        print(f'Tem {save_list[0]} vagaS que nessecitaM de Júniors')
    
    if save_list[1] <= 1:
        print(f'Tem {save_list[1]} vaga que nessecita de Plenos')
    else: 
        print(f'Tem {save_list[1]} vagas que nessecitam de Plenos')

    if save_list[2] <= 1:
        print(f'Tem {save_list[2]} vaga que nessecita de Sêniors')
    else: 
        print(f'Tem {save_list[2]} vagas que nessecitam de Sêniors')
    

def details_out_inside(save_list):

    if save_list[0] <= 1:
        print(f'Tem {save_list[0]} vaga que aceita candidatos de fora')
    else: 
        print(f'Tem {save_list[0]} vagas que aceitam candidatos de fora')
    
    if save_list[1] <= 1:
        print(f'Tem {save_list[1]} vaga que não aceita candidatos de fora')
    else: 
        print(f'Tem {save_list[1]} vagas que não aceitam candidatos de fora')


def details_remote_noremote(save_list):

    if save_list[0] <= 1:
        print(f'Tem {save_list[0]} vaga que é remota')
    else: 
        print(f'Tem {save_list[0]} vagas que são remotas')
    
    if save_list[1] <= 1:
        print(f'Tem {save_list[1]} vaga que não é remota')
    else: 
        print(f'Tem {save_list[1]} vagas que não são remotas')
