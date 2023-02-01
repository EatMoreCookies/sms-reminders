from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from message_parser import MessageParser

app = FastAPI()

current_user_id: str = '07d5d47a-a041-11ed-84b6-c8348e4bbf3d'

@app.post("/sms")
async def sms(request: Request):
    form = await request.form()    
    message: str = form['Body']

    print("recived message {}".format(message))

    message_parser = MessageParser()
    response_message = message_parser.determine_response_body_from_message(current_user_id, message)

    print("response_message {}".format(response_message))

    response = MessagingResponse()
    response.message(response_message)

    return Response(content=str(response), media_type="application/xml")
