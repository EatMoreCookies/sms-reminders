from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from message_parser import MessageParser
from database_client import DatabaseClient

app = FastAPI()
message_parser = MessageParser()

@app.post("/sms")
async def sms(request: Request):
    form = await request.form()    
    message: str = form['Body']
    from_phone_number = form['From']

    response_message = message_parser.determine_response_body_from_message(from_phone_number, message)

    response = MessagingResponse()
    response.message(response_message)

    return Response(content=str(response), media_type="application/xml")
