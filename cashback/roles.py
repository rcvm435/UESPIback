from rolepermissions.roles import AbstractUserRole

class lojista(AbstractUserRole):
    available_permissions = {'cadastrar_produtos': True, 'ver_produtos': True, 'determina_cash': True, 'ver_cash': True }

class cliente(AbstractUserRole):
    available_permissions = {'comprar_produtos': True, 'ver_produto': True, 'ver_cash': True }