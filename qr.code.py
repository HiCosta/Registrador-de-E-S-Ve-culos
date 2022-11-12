import crcmod
import qrcode


#informações necessárias para gerar codigo de pagamento(payload)
class Payload():
    def __init__(self, nome, chavepix, valor, cidade):      
        self.nome = nome
        self.chavepix = chavepix
        self.valor = valor
        self.cidade = cidade
        
        #obtendo tamanho dos textos
        self.nome_tam = len(self.nome)                  
        self.chavepix_tam = len(self.chavepix)
        self.valor_tam = len(self.valor)
        self.cidade_tam = len(self.cidade)
        
        self.merchantAccount_tam = f'0014BR.GOV.BCB.PIX01{self.chavepix_tam}{self.chavepix}'
        
        #codigos de acordo com BRCode criado pelo BaCen
        self.payloadFormat = '000201'               
        
        self.merchantAccount = f'26{len(self.merchantAccount_tam)}{self.merchantAccount_tam}'
        
        #para aplicar 0 à esquerda por ser obrbitório para certos tamanhos
        if self.valor_tam <= 9:
            self.transactionAmmount_tam = f'0{self.valor_tam}{self.valor}'     
        else:
            self.transactionAmmount_tam = f'{self.valor_tam}{self.valor}'
        
        if self.nome_tam <= 9 :
            self.nome_tam = f'0{self.nome_tam}'
            
        if self.cidade_tam <= 9 :
            self.cidade_tam = f'0{self.cidade_tam}'
        
        #codigos de acordo com BRCode criado pelo BaCen
        self.payloadFormat = '000201'
        self.merchantAccount = f'26{len(self.merchantAccount_tam)}{self.merchantAccount_tam}'
        self.merchantCategCod = '52040000'
        self.transactionCurrency = '5303986'
        self.transactionAmmount = f'54{self.transactionAmmount_tam}'
        self.countryCode = '5802BR'
        self.merchantName = f'59{self.nome_tam}{self.nome}'
        self.merchantCity = f'60{self.cidade_tam}{self.cidade}'
        self.crc16 = '6304'
        
    def gerarPayload(self):
        self.payload = f'''{self.payloadFormat}{self.merchantAccount}{self.merchantCategCod}{self.transactionCurrency}
        {self.transactionAmmount}{self.countryCode}{self.merchantName}{self.merchantCity}{self.crc16}'''
        
        self.gerarCrc16(self.payload)


    def gerarCrc16(self, payload):
        crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000) #cod segundo documentação
        
        self.crc16Code = hex(crc16(str(payload).encode('utf-8')))
        
        self.crc16Code_formatado = str(self.crc16Code).replace('0x', '').upper()
        
        self.payload_completa = f'{payload}{self.crc16Code_formatado}'
        
        self.gerarQrCode(self.payload_completa)
        
    def gerarQrCode(self, payload): #criando iamgem qrcode a partir do pix copia e cola criado acima
        self.qrcode  = qrcode.make(payload)
        self.qrcode.save('pixqrcodegen.png')

        return print(payload)
    
if __name__ == '__main__':
    Payload('Albano Dias', '+5531995923283', '5.00', 'Betim').gerarPayload()
