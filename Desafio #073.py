times = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Atlético-PR','Cruzeiro','Botafogo',
         'Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')
print(f'[A] Os cinco primeiros colocados são {times[:5]}')
print(f'[B] Os quatro últimos colocados são {times[16:]}')
print(f'[C] Os times em ordem alfabética ficaria: {sorted(times)}')
print(f'[D] O time do Chapecoense está na {times.index("Chapecoense")+1}ª posição.')