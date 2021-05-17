def checar_string(variavel):
    if isinstance(variavel, str) and variavel != '':
        return variavel
    return 'Vazio'


def checar_inteiro(variavel):
    if isinstance(variavel, int) and variavel > 0:
        return variavel
    return 0


def checar_float(variavel):
    if (isinstance(variavel, float) or isinstance(variavel, int)) and variavel > 0:
        return float(variavel)
    return 0
