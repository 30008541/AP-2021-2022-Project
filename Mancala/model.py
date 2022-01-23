def create_player(name: str) -> dict:
    return {
        'name'   : name,
        'numJogos': 0,
        'numVitorias': 0,
        'numEmpates': 0,
        'numDerrotas': 0,
    }

def jogo():
    jogo = {'Tabuleiro A': [4, 4, 4, 4, 4, 4, 0], 
            'Tabuleiro B': [4, 4, 4, 4, 4, 4, 0],
            'Vez Jogador A' : False,
            'Automático': False,
            'Nível': None,
            'Em curso': False
             }
    return jogo
