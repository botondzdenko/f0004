név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
születési_év = 2020 - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')
érettségi_év = születési_év + 18
print(név, ', kend ', 