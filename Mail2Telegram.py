import asyncio
from aiosmtpd.controller import Controller
import requests
import os

class ExampleHandler:
   
    async def handle_DATA(self, server, session, envelope):
        decodedMail=envelope.content.decode('utf8', errors='replace')
        telegramRequest = 'https://api.telegram.org/bot' + os.environ.get("BOT_TOKEN")  + '/sendMessage?chat_id=' + os.environ.get("CHAT_ID") + '&text=' +str(decodedMail) 
        response = requests.post(telegramRequest)
        
        print("\nDecoded Mail:\n" + str(decodedMail))
        print("\nTelegram API response: " + str(response) + "\n")
    
        return '250 Message accepted for delivery'



async def amain(loop):
    #hostname is passed to your loop’s AbstractEventLoop.create_server() method as the host parameter, 
    #except None (default) is translated to ‘::1’. 
    #To bind dual-stack locally, use ‘localhost’. To bind dual-stack on all interfaces, use ''     
    controller = Controller(ExampleHandler(),hostname='', port=os.environ.get("SMTP_PORT"))
    controller.start()

loop = asyncio.get_event_loop()
loop.create_task(amain(loop=loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
