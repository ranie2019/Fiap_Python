usuarios = {}
print(f'{usuarios}')

usuarios = {'chaves': ['chaves', '24/12/2021', 'recep_01'],
            'quico': ['quico', '26/09/2021', 'raiox_02']}
print(usuarios)

usuarios['florinda'] = ['dona florinda', '30/12/2021', 'casa_56']
print(usuarios)

print('*-* ' * 15)
print(usuarios.get('quico'))
