def encontrar_maior_menor_numeros(sequencia):
    if not sequencia:
        return None, None  # Retorna None se a sequência estiver vazia

    maior_numero = max(sequencia)
    menor_numero = min(sequencia)
    return maior_numero, menor_numero

def main():
    try:
        sequencia_str = input("Digite uma sequência de números separados por espaço: ")
        lista_numeros = [float(numero) for numero in sequencia_str.split()]
        
        maior, menor = encontrar_maior_menor_numeros(lista_numeros)

        if maior is None or menor is None:
            print("Sequência vazia. Não é possível encontrar maior e menor número.")
        else:
            print(f"Maior número: {maior}")
            print(f"Menor número: {menor}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar uma sequência válida de números.")

if __name__ == "__main__":
    main()