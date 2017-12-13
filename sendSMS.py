from twilio.rest import Client

# Datos requeridos de la cuenta

SID = "ACb5a0233d29cedb9ed60e9d51d227e541"
auth_token = "e1701e1a644d10920e5d27acb54868b7"

cliente = Client(SID, auth_token)

mensaje = cliente.messages.create(
    texto = "Este es un mensaje de prueba",
    to = "+50684430686",
    from_ =  "+13603299431")

print SID