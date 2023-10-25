# This is a proof-of-concept for a serverless discord slash command endpoint

import json
import os
from random import randint
from nacl.signing import VerifyKey

PUBLIC_KEY = os.getenv('PUBLIC_KEY')

PING_PONG = {"type": 1}

RESPONSE_TYPES =  { 
                    "PONG": 1, 
                    "ACK_NO_SOURCE": 2, 
                    "MESSAGE_NO_SOURCE": 3, 
                    "MESSAGE_WITH_SOURCE": 4, 
                    "ACK_WITH_SOURCE": 5
                  }

zenisms = [
    "Slow is smooth, smooth is fast. -US Navy SEALs saying",
    "Play is the highest form of research. -Albert Einstein",
    "It's not what you look at that matters, it's what you see. -Henry David Thoreau",
    "You hit what you aim at and if you aim at nothing you will hit it every time. -Zig Ziglar",
    "Bad weather always looks worse through a window. -Tom Lehrer",
    "To breakthrough your performance, you've got to breakthrough your psychology. -Jensen Siaw"
]

def verify_signature(event, body):
    auth_sig = event['headers'].get('x-signature-ed25519')
    auth_ts  = event['headers'].get('x-signature-timestamp')
    
    
    message = auth_ts.encode() + body.encode()
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(auth_sig)) # raises an error if unequal

def ping_pong(body):
    if body.get("type") == 1:
        return True
    return False
    
def lambda_handler(event, context) -> Dict:
    raw_body = event.get('body')
    json_body = json.loads(raw_body)

    # verify the signature
    verify_signature(event, raw_body)

    # check if message is a ping
    if ping_pong(json_body):
        return PING_PONG
    
    elif json_body['data'].get('name', '') == 'zen':
        print("Making zen")

        the_zen = zenisms[randint(0,len(zenisms)-1)]
        print(the_zen)
        return {
            "type": RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": the_zen,
            }
        }
    
    else:
        # If there happens to be another bot command pointing at this endpoint, we'll handle it here
        # right now we only have one slash command registered though, which is handled above
        return {
            "type": RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": "BEEP BOOP", # dummy return content
            }
        }
