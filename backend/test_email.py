from microservices import sendEmail

try:
    sendEmail(100)
    print('Sucesso no envio!')
except Exception as e:
    print(e)