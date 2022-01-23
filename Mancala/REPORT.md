->Grupo D04
    -Membros do grupo:
        -Duarte Miguel Dos Santos Rodrigues nº30009658
        -Jorge Manuel Fernandes Chaves nº30008541
        -Eduane Alexandre da Cunha Cardoso nº30008592
        -Henrique Dias Velez nº30008353

->Mancala
    -Comandos
        ->Registar jogador (RJ)
            -Contribuintes: Jorge, Duarte.
            -Funções utilizadas: registar_jogador, controller(), has_player(), commandRJ().
            -Parâmetros: player, commands.
            -Input: RJ nomeJogador
            -Restrições: Não se podem registar jogadores já inseridos.
            -Descrição: Regista os jogadores de modo a poderem participar no jogo. 

        ->Listar jogadores (LJ)
            -Contribuintes: Jorge.
            -Funções utilizadas:has_players(),controller(), get_players() commandLJ().
            -Parâmetros: player.
            -Input: LJ.
            -Restrições: O comando não funciona se não existirem jogadores registados.
            -Descrição: Lista os valores de dicionários que pertencem a cada jogador, que contêm o nome, número de jogos feitos, número de vitórias, empates e derrotas.

        ->Iniciar jogo (IJ)
            -Contribuintes: Jorge.
            -Funções utilizadas: commandIJ(), has_player(), controller(), jogo().
            -Parâmetros: commands, player, game.
            -Input: IJ nomeJogador_A nomeJogador_B
            -Restrições: O comando não funciona se um dos jogadores não estiver registado ou se um jogo já estiver em curso.
            -Descrição: Verifica se os jogadores foram registados e, em seguida inicia um jogo com os jogadores inseridos.

        ->Iniciar jogo automático(IJA)
            -Contribuintes: Jorge, Duarte.
            -Funções utilizadas: commandIJA, iniciar_jogada()
            -Parâmetros:player,players,game
            -Input: IJA nomeJogador Nivel
            -Restrições: O comando não funciona se o jogador não estiver registado
            -Descrição: O comando inicia um jogo de nivel normal ou avançado com o computador

        ->Detalhes de jogo (DJ)
            -Contribuintes: Duarte.
            -Funções utilizadas: controller(), jogo(), commandDJ().
            -Parâmetros: game, players.
            -Input: DJ
            -Restrições: O comando não funciona se não existir um jogo em curso.
            -Descrição: Se os jogadores estiverem registados num jogo, o comando retorna os nomes dos jogadores, seguido das casas e do poço de cada jogador.

        ->Efetuar jogada (J)
            -Contribuintes: Duarte.
            -Funções utilizadas: commandJ, iniciar_jogada(), has_players(), jogo(), controller().
            -Parâmetros: posicao, player, players, game.
            -Input: J nomeJogador posicao
            -Restrições: O comando não funciona se não existir um jogo em curso.
            -Descrição: Se existir um jogo em curso, o comando efetua uma jogada dependendo da casa escolhida pelo jogador e, depois de destribuir as peças, o programa dá a vez ao outro jogador.

        ->Desistir de jogo (D)
            -Contribuintes: Duarte.
            -Funções utilizadas: has_player(), commandD.
            -Parâmetros: commands, player, game.
            -Input: D nomeJogador_A nomeJogador_B
            -Restrições: O comando não funciona se não existir um jogo em curso, se um jogador não existir ou se um jogador não participar no jogo.
            -Descrição: Se existir um jogo em curso, este comando acaba o jogo com os respetivos jogadores.

        ->Gravar (G)
            -Contribuintes: Jorge.
            -Funções utilizadas: save(), commandG().
            -Parâmetros: player, filename.
            -Input: G nomeFicheiro
            -Descrição: Grava num ficheiro com o nome escolhido pelo utilizador.
            
        ->Ler (L)
            -Contribuintes: Jorge.
            -Funções utilizadas: load(), controller() commandL().
            -Parâmetros: filename.
            -Input: L nomeFicheiro
            -Descrição: Lê a informação armazenada no ficheiro criado no comando Gravar.
            
    -Report
        ->Contribuintes: Duarte, Jorge.

    -Notas
        ->Dificuldades: Tivemos mais dificuldades a criar o comando do jogo automático e na jogada.