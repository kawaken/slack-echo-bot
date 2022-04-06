import functions_framework
import json
import logging
from box import Box

logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

# process_before_response must be True when running on FaaS
app = App(process_before_response=True)
handler = SlackRequestHandler(app)


@app.event("message")
def message_channel(body, say, logger):
    b = Box(body)
    say(b.event.text)


@functions_framework.http
def echo_bot(request):
    return handler.handle(request)
