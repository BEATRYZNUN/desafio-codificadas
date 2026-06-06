import sys

def solve():
    # Lê toda a entrada da memória de uma vez só
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    # Número de casos de teste
    t = int(next(iterator))
    
    resultados = []
    
    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
        s = next(iterator)
        
        protecoes = 0
        # Inicializa com um valor bem negativo para o primeiro '1' sempre ser protegido
        ultima_posicao_protegida = -10**9 
        
        for i in range(n):
            if s[i] == '1':
                # Se a distância para o último protegido for maior ou igual a k
                if i - ultima_posicao_protegida >= k:
                    protecoes += 1
                    ultima_posicao_protegida = i # Atualiza o último guardião
                    
        resultados.append(str(protecoes))
    
    # Imprime todos os resultados separados por quebra de linha
    print('\n - Untitled-1:35'.join(resultados))

if __name__ == '__main__':
    solve()