while True:
    try:
        primeira_nota = float(input("digite a primeira nota: "))
        segunda_nota = float(input("digite a segunda nota: "))

        media = (primeira_nota + segunda_nota) / 2

        print(f"A média final é {media:.2f}")
        
    except:
        print("digite um valor válido meu brother!")