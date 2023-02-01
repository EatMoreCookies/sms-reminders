from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/sms")
async def sms(request: Request):
    form = await request.form()
    
    fromNumber: str = form['From']
    message: str = form['Body']

    response = MessagingResponse()
    response.message("Hello, you are {}, and you said {}".format(fromNumber, message))

    print(response)

    return Response(content=str(response), media_type="application/xml")
