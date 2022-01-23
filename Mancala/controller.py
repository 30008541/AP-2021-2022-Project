import pickle
from model import *
def controller():
    return {
        'jogadores': []
        }

# Registar Jogador
def registar_jogador(_player, nomeJogador):
   player = {
            'name'   : nomeJogador,
            'numJogos': 0,
            'numVitorias': 0,
            'numEmpates': 0,
            'numDerrotas': 0,
            }
   _player['jogadores'].append(player)

# Iniciar Jogo Automático
def iniciar_jogo_automatico(level,players,posicao,game):
        if "Normal" == level:
            game['Em curso'] = True
            player_A = players['jogadores'][0]
            player_B = players['jogadores'][1]
            posicao = int(posicao)
            poco_2 = game['Tabuleiro B'][6]
            poco_1 = game['Tabuleiro A'][6]
            if game['Vez Jogador A'] == True:
                for player in players['jogadores']:
                    if posicao > 6:
                        break
                    else:
                        sementes = game['Tabuleiro A'][posicao-1]
                        game['Tabuleiro A'][posicao-1] = 0

                        checking_p_c = True

                        i = posicao
                        if sementes>=8:
                            sementes = int(sementes) +1
                        for _ in range(posicao, posicao+sementes):
                            if i%7 == 0:

                                checking_p_c = not checking_p_c
                                i = 0

                        
                            if checking_p_c:

                                game['Tabuleiro A'][i] += 1             
                            else:
                                if (-i == -6):
                                    game['Tabuleiro B'][6] = poco_2
                                else: 
                                    game['Tabuleiro B'][i] += 1

                            if 7 >= sementes:
                                if sementes%7 == 0:
                                    game['Vez Jogador A'] = True
                                else:
                                    game['Vez Jogador A'] = False
                            else:
                                if (sementes-1)%7 == 0:
                                    game['Vez Jogador A'] = False
                                else:
                                    game['Vez Jogador A'] = True

                            i += 1
                            if sum(game['Tabuleiro A'][:6]) == 0:
                                if player_A in players['jogadores'] and player_B in players['jogadores']:
                                    if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                                        player_B['numJogos'] = player_B['numJogos'] +1
                                        player_B['numEmpates'] = player_B['numEmpates'] +1
                                        player_A['numJogos'] = player_A['numJogos'] +1
                                        player_A['numEmpates'] = player_A['numEmpates'] +1

                                    else:
                                        if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                                            player_A['numJogos'] = player_A['numJogos'] +1
                                            player_A['numVitorias'] = player_A['numVitorias'] +1
                                            player_B['numJogos'] = player_B['numJogos'] +1
                                            player_B['numDerrotas'] = player_B['numDerrotas'] +1

                                        else:  
                                            player_B['numJogos'] = player_B['numJogos'] +1
                                            player_B['numVitorias'] = player_B['numVitorias'] +1
                                            player_A['numJogos'] = player_A['numJogos'] +1
                                            player_A['numDerrotas'] = player_A['numDerrotas'] +1

                            if sum(game['Tabuleiro B'][:6]) == 0:
                                if player_A in players['jogadores'] and player_B in players['jogadores']:
                                    if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                                        player_B['numJogos'] = player_B['numJogos'] +1
                                        player_B['numEmpates'] = player_B['numEmpates'] +1
                                        player_A['numJogos'] = player_A['numJogos'] +1
                                        player_A['numEmpates'] = player_A['numEmpates'] +1
                                        
                                    else:
                                        if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                                            player_A['numJogos'] = player_A['numJogos'] +1
                                            player_A['numVitorias'] = player_A['numVitorias'] +1
                                            player_B['numJogos'] = player_B['numJogos'] +1
                                            player_B['numDerrotas'] = player_B['numDerrotas'] +1

                                        else:  
                                            player_B['numJogos'] = player_B['numJogos'] +1
                                            player_B['numVitorias'] = player_B['numVitorias'] +1
                                            player_A['numJogos'] = player_A['numJogos'] +1
                                            player_A['numDerrotas'] = player_A['numDerrotas'] +1
                return game


# Iniciar Jogada
def iniciar_jogada(posicao, player, players, game):
    player_A = players['jogadores'][0]
    player_B = players['jogadores'][1]
    posicao = int(posicao)
    poco_2 = game['Tabuleiro B'][6]
    poco_1 = game['Tabuleiro A'][6]
    if game['Vez Jogador A'] == True:
        for player in players['jogadores']:
            if posicao > 6:
                break
            else:
                sementes = game['Tabuleiro A'][posicao-1]

                game['Tabuleiro A'][posicao-1] = 0

                checking_p_c = True

                i = posicao
                if sementes>=8:
                    sementes = int(sementes) +1
                for _ in range(posicao, posicao+sementes):
                    if i%7 == 0:

                        checking_p_c = not checking_p_c
                        i = 0
                
                    if checking_p_c:
                        game['Tabuleiro A'][i] += 1             
                    else:
                        if (-i == -6):
                            game['Tabuleiro B'][6] = poco_2
                        else: 
                            game['Tabuleiro B'][i] += 1

                    if 7 >= sementes:
                        if posicao+sementes == (len(game['Tabuleiro A'])):
                            game['Vez Jogador A'] = True
                        else:
                            game['Vez Jogador A'] = False
                    else:
                        sementes = int(sementes -1)
                        if posicao+sementes == (len(game['Tabuleiro A'])):
                            game['Vez Jogador A'] = False
                        else:
                            game['Vez Jogador A'] = True

                    i += 1
                    if sum(game['Tabuleiro A'][:6]) == 0:
                        if player_A in players['jogadores'] and player_B in players['jogadores']:
                            if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                                player_B['numJogos'] = player_B['numJogos'] +1
                                player_B['numEmpates'] = player_B['numEmpates'] +1
                                player_A['numJogos'] = player_A['numJogos'] +1
                                player_A['numEmpates'] = player_A['numEmpates'] +1

                            else:
                                if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numVitorias'] = player_A['numVitorias'] +1
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numDerrotas'] = player_B['numDerrotas'] +1

                                else:  
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numVitorias'] = player_B['numVitorias'] +1
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numDerrotas'] = player_A['numDerrotas'] +1

                    if sum(game['Tabuleiro B'][:6]) == 0:
                        if player_A in players['jogadores'] and player_B in players['jogadores']:
                            if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                                player_B['numJogos'] = player_B['numJogos'] +1
                                player_B['numEmpates'] = player_B['numEmpates'] +1
                                player_A['numJogos'] = player_A['numJogos'] +1
                                player_A['numEmpates'] = player_A['numEmpates'] +1
                                
                            else:
                                if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numVitorias'] = player_A['numVitorias'] +1
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numDerrotas'] = player_B['numDerrotas'] +1

                                else:  
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numVitorias'] = player_B['numVitorias'] +1
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numDerrotas'] = player_A['numDerrotas'] +1
        return game

    else:
        for player in players['jogadores']:
            if posicao > 6:
                break
            else:
                sementes = game['Tabuleiro B'][posicao-1] 

                game['Tabuleiro B'][posicao-1] = 0

                checking_p_c = True

                i = posicao
                if sementes>=8:
                    sementes = int(sementes) +1
                for _ in range(posicao, posicao+sementes):
                    if i%7 == 0:

                        checking_p_c = not checking_p_c
                        i = 0

                
                    if checking_p_c:

                        game['Tabuleiro B'][i] += 1             
                    else:
                        if (-i == -6):
                            game['Tabuleiro A'][6] = poco_1
                        else: 
                            game['Tabuleiro A'][i] += 1

                    if 7 >= sementes:
                        if posicao+sementes == (len(game['Tabuleiro B'])):
                            game['Vez Jogador A'] = False
                        else:
                            game['Vez Jogador A'] = True
                    else:
                        sementes = int(sementes -1)
                        if posicao+sementes == (len(game['Tabuleiro B'])):
                            game['Vez Jogador A'] = True
                        else:
                            game['Vez Jogador A'] = False

                    i += 1
                    if sum(game['Tabuleiro A'][:6]) == 0:
                        if player_A in players['jogadores'] and player_B in players['jogadores']:
                            if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                                player_B['numJogos'] = player_B['numJogos'] +1
                                player_B['numEmpates'] = player_B['numEmpates'] +1
                                player_A['numJogos'] = player_A['numJogos'] +1
                                player_A['numEmpates'] = player_A['numEmpates'] +1

                            else:
                                if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numVitorias'] = player_A['numVitorias'] +1
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numDerrotas'] = player_B['numDerrotas'] +1

                                else:  
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numVitorias'] = player_B['numVitorias'] +1
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numDerrotas'] = player_A['numDerrotas'] +1

                    if sum(game['Tabuleiro B'][:6]) == 0:
                        if player_A in players['jogadores'] and player_B in players['jogadores']:
                            if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                                player_B['numJogos'] = player_B['numJogos'] +1
                                player_B['numEmpates'] = player_B['numEmpates'] +1
                                player_A['numJogos'] = player_A['numJogos'] +1
                                player_A['numEmpates'] = player_A['numEmpates'] +1
                                
                            else:
                                if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numVitorias'] = player_A['numVitorias'] +1
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numDerrotas'] = player_B['numDerrotas'] +1

                                else:  
                                    player_B['numJogos'] = player_B['numJogos'] +1
                                    player_B['numVitorias'] = player_B['numVitorias'] +1
                                    player_A['numJogos'] = player_A['numJogos'] +1
                                    player_A['numDerrotas'] = player_A['numDerrotas'] +1
        return game





# Verificar se existem jogadores    
def has_players(_player):
    for player in _player['jogadores']:
        if len(player) > 0:
            return True
    return False

# Obtem os jogadores
def get_players(_player):
    return _player['jogadores']

# Listar os jogadores
def has_player(_player, name):
    for player in _player['jogadores']:
        if player['name'] == name:
            return True
    return False

# Gravar o estado do programa no ficheiro criado
def save(player, filename):
    with open(filename, 'wb') as file:
        pickle.dump(player, file)

# Lê o ficheiro criado
def load(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    