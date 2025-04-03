2. Resolver o sudoku considerado o mais dificil da atualidade, utilizando as heuristicas

"Some people might make three or four lucky guesses and so be able to solve it in 15 minutes or half an hour and will wonder why it is said to be so difficult," he said. "But it will normally take days to solve by logic."

1a)  Os dois primeiros números escolhidos foram baseados na heurística **Hidden Single**, 3 e 5, também por terem o maior número de aparições no board.

2a) A segunda parte foi inserir o número usando a técnica de **Guessing**, onde em um quadrante há poucas possibilidades de inserir um número, e e feita a inserção de maneira aleatória e continuasse a resolução, se der errado faz um backtracking e tenta a outra possibilidade. Nesse caso, foi inserido o número 3 P(3, 9) e P(7, 1), o número 5 em P(5, 8). Ou seja, foram feitos 3 chutes.

3a) Depois foi feito **Hidden Single** com o número 3, na posição P(9,5) e na posição P(2,2)

4a) Depois, **Hidden Single** novamente para o número 4 na posição P(1,2)

