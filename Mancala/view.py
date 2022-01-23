from asyncio.windows_events import NULL
import controller as cr
from model import *

 
def main():
    filename = 'mancala.player'
    players = cr.controller()
    game = cr.jogo()
    while True:
        line = input()
        if not line:
            exit(0)
        commands = line.split(" ")
        # Registar jogadores
        if commands[0] == "RJ":
            commandRJ(commands, players)
        # Listar jogadores
        elif commands[0] == "LJ":
            commandLJ(players)
        # Inicar jogada
        elif commands[0] == "IJ":
            commandIJ(commands, players, game)
        # Iniciar jogo automático
        elif commands[0] == "IJA":
            commandIJA(commands, players, commands[2],game)
        # Detalhes de jogo
        elif commands[0] == "DJ":
            commandDJ(game,players)
        # Iniciar jogada
        elif commands[0] == "J":
            commmandJ(commands[2],commands[1], players,game)
        # Desistir do jogo
        elif commands[0] == "D":
            commandD(commands, players, game)
        # Gravar
        elif commands[0] == "G":
           commandG(players, filename)
        # Ler
        elif commands[0] == "L":
            players = commandL(filename,players)
        else:
            print("Instrução inválida.")   

# Registar jogador
def commandRJ(commands, player):
    name = commands[1]
    if cr.has_player(player, name):
        print("Jogador existente.")
    else:
        cr.registar_jogador(player, name)
        print("Jogador registado com sucesso.")

# Listar jogadores
def commandLJ(player):
    if not cr.has_players(player):
        print("Não existem jogadores registados.")
    else:
        for _player in cr.get_players(player):
            print(f"{_player['name']} {_player['numJogos']} {_player['numVitorias']} {_player['numEmpates']} {_player['numDerrotas']}")

# Iniciar jogo
def commandIJ(commands, player, game):
    nomejogador = commands[1]
    nomejogador = commands[2]
    if game['Em curso'] == True:
        print('Existe um jogo em curso.')
    else:
        if (not cr.has_player(player, nomejogador)) or (not cr.has_player(player, nomejogador)):
            print("Jogador inexistente.")
        else:
            game['Em curso'] = True
            game['Vez Jogador A'] = True
            print("Jogo iniciado com sucesso.")

# Iniciar jogo automático
def commandIJA(commands, player, level, game):
    nomejogador = commands[1]
    level = commands[2]
    posicao = NULL 
    if game['Em curso'] == True:
        print('Existe um jogo em curso.')
    elif (not cr.has_player(player, nomejogador)):
        print("Jogador inexistente.")
    else:
        if (not cr.has_player(player, nomejogador)):
            print("Jogador inexistente.")
        else:
            cr.iniciar_jogo_automatico(level, player, posicao, game)
            if level == "Normal":
                print("Jogo automático de nível Normal iniciado com sucesso.")
            elif level == "Avançado":
                print("Jogo automático de nível Avançado iniciado com sucesso.")


# Detalhes do jogo
def commandDJ(game,players):
    if game['Em curso'] == True:
        player_A = players['jogadores'][0]
        player_B = players['jogadores'][1]
        if player_A in players['jogadores']:
            print(player_A['name'], [game['Tabuleiro A'][0]], [game['Tabuleiro A'][1]], [game['Tabuleiro A'][2]],  [game['Tabuleiro A'][3]],  [game['Tabuleiro A'][4]],  [game['Tabuleiro A'][5]], ('(%s)') % (game['Tabuleiro A'][6]))
        if player_B in players['jogadores']:
            print(player_B['name'], [game['Tabuleiro B'][0]], [game['Tabuleiro B'][1]], [game['Tabuleiro B'][2]],  [game['Tabuleiro B'][3]],  [game['Tabuleiro B'][4]],  [game['Tabuleiro B'][5]], ('(%s)') % (game['Tabuleiro B'][6]))
    else:
        print('Não existe jogo em curso.')


# Efetuar jogada
def commmandJ(position, player, players,game):
    resultado_jogo = cr.iniciar_jogada(position, player, players, game)
    player_A = players['jogadores'][0]
    player_B = players['jogadores'][1]
    position = int(position)
    if position > 6:
        print('Não pode selecionar o poço. Escolha outra casa.')
    else:
        if not cr.has_players(players):
            print("Jogador inexistente.")  
        else:
            if game['Em curso'] == False:
                    print("Não existe jogo em curso.")
            else:
                if game['Vez Jogador A'] == True:
                    if player_A in players['jogadores']:
                        print(f"O jogador {player_A['name']} pode jogar.")
                else: 
                    if player_B in players['jogadores']:
                        print(f"O jogador {player_B['name']} pode jogar.")

            if sum(game['Tabuleiro A'][:6]) == 0:
                if player_A in players['jogadores'] and player_B in players['jogadores']:
                    if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                        print('Jogo Terminado.')
                        print(player_A['name'], game['Tabuleiro A'][6])
                        print(player_B['name'], game['Tabuleiro B'][6])

                    else:
                        if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                            print('Jogo Terminado.')
                            print(player_A['name'], game['Tabuleiro A'][6])
                            print(player_B['name'], game['Tabuleiro B'][6])

                        else:  
                            print('Jogo Terminado.')
                            print(player_A['name'], game['Tabuleiro A'][6])
                            print(player_B['name'], game['Tabuleiro B'][6])

                    game['Tabuleiro A'] = [4, 4, 4, 4, 4, 4, 0]
                    game['Tabuleiro B'] = [4, 4, 4, 4, 4, 4, 0]

            if sum(game['Tabuleiro B'][:6]) == 0:
                if player_A in players['jogadores'] and player_B in players['jogadores']:
                    if game['Tabuleiro A'][6] == game['Tabuleiro B'][6]:
                        print('Jogo Terminado.')
                        print(player_A['name'], game['Tabuleiro A'][6])
                        print(player_B['name'], game['Tabuleiro B'][6])
                         
                    else:
                        if game['Tabuleiro A'][6] > game['Tabuleiro B'][6]:
                            print('Jogo Terminado.')
                            print(player_A['name'], game['Tabuleiro A'][6])
                            print(player_B['name'], game['Tabuleiro B'][6])

                        else:  
                            print('Jogo Terminado.')
                            print(player_A['name'], game['Tabuleiro A'][6])
                            print(player_B['name'], game['Tabuleiro B'][6])

                    game['Tabuleiro A'] = [4, 4, 4, 4, 4, 4, 0]
                    game['Tabuleiro B'] = [4, 4, 4, 4, 4, 4, 0]

# Desistir
def commandD(commands, player, game):
    nomejogador = commands[1]
    nomejogador = commands[2]
    if (not cr.has_player(player, nomejogador)) or (not cr.has_player(player, nomejogador)):
        print("Jogador inexistente.")
    elif game['Em curso'] == False:
        print("Não existe jogo em curso.")
    else:
        game['Em curso'] = False
        print("Jogo terminado com sucesso.")
        
# Gravar
def commandG(player, filename):
    cr.save(player, filename)
    print("Jogo gravado com sucesso.")
    
# Ler
def commandL(filename,players):
    player_A = players['jogadores'][0]
    player_B = players['jogadores'][1]
    try:
        if player_A in players['jogadores'] and  player_B in players['jogadores']:
            player = cr.load(filename)
            print("Jogo lido com sucesso.")
            print(player_A['name'], player_A['numJogos'],player_A['numVitorias'],player_A['numEmpates'],player_A['numDerrotas'])
            print(player_B['name'], player_B['numJogos'],player_B['numVitorias'],player_B['numEmpates'],player_B['numDerrotas'])
            return player
    except Exception as e:
        print(" Ficheiro inexistente.")


if __name__ == '__main__':
    main()
