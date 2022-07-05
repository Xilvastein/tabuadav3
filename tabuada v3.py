valor = 0
while True:
    print('--' * 20)
    v = int(input('Gostaria de ver a tabuada de que valor?'))
    if v < 0:
        break
    for tabu in range(0, 11):
        mult = v*tabu
        print(f'{v} x {tabu} = {mult}')
print('TABUADA ENCERRADA!')



