# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | Cadeado de notas | [Ver no Codeforces](https://codeforces.com/problemset/problem/2154/A)) | 800 |
 
---
 
## Problema 1 — [Cadeado de notas]
 
### O que o problema pede?
É um jogo onde o objetivo é proteger algumas notas musicais do meu oponente, que é o Teto, e ele só joga da esquerda para a direita.

 
### Como eu resolvi?
Eu aneio pela string junto com o Teto, da esquerda para a direita, e só gastei a proteção quando foinecessário. Eu começei o jogo sem nenhum escudo. Toda vez que eu encontrei uma nota '1', eu olho a distância dela para a última nota que eu protegi. Se a distância for menor que k, significa que o escudo anterior ainda está ativo e o Teto não pode atacar, então eu não gasto nada. Mas se a distância for maior ou igual a k, o escudo antigo já venceu e o Teto vai apagar a nota; aí eu sou obrigada a gastar uma proteção e colocar um escudo novo ali.
 
 
### Código
```python

import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    t = int(next(iterator))
    resultados = []
    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
        s = next(iterator)
        protecoes = 0
        ultima_posicao_protegida = -10**9 
        for i in range(n):
            if s[i] == '1':
                # Se a distância para o último protegido for maior ou igual a k
                if i - ultima_posicao_protegida >= k:
                    protecoes += 1
                    ultima_posicao_protegida = i # Atualiza o último guardião
        resultados.append(str(protecoes))
    print('\n  Untitled1:35 - Cadeado de notas- desafio codificadas.py:31'.join(resultados))
if __name__ == '__main__':
    solve()
```
 
---
## IA utilizada
 
**Qual IA você usou?**
Gemini
 
**Como a IA te ajudou?**
Você me ajudou explicando o problema e, se eu não entendia, eu mandava um novo comando para você explicar de outra forma, mais simples, até que eu entendesse a proposta do problema.
 
---
 
## Reflexão
 
### Dificuldades encontradas
A minha maior dificuldade foi entender o problema e a matemática envolvida.
 
 
### O que aprendi
Aprendi um pouco mais sobre a linguagem Python e um pouquinho mais sobre problemas matemático, pois nunca fui bem nessa área na escola.
 
 
### Como foi a experiência?
No geral, eu gostei. O que pretendo fazer agora é estudar mais sobre linguagens de programação.
