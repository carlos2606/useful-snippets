from twilio.rest import Client

# Datos requeridos de la cuenta

SID = ""
auth_token = ""

cliente = Client(SID, auth_token)

mensaje = cliente.messages.create(
    texto = "Este es un mensaje de prueba",
    to = "+50684430686",
    from_ =  "+13603299431")

print SID