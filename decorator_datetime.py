from datetime import datetime

def hora():
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S") + f".{agora.microsecond // 1000:03d}"
    print(hora_formatada)

def meu_decorador(função):
    def horário_antes_e_depois():
        hora()
        função()
        hora()
    return horário_antes_e_depois

@meu_decorador
def jantar():
    print('Comendo...')

jantar()