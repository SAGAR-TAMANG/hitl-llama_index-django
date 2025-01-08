from channels.generic.websocket import AsyncWebsocketConsumer
from django.template.loader import render_to_string
from dotenv import load_dotenv

from llama_index.core.workflow.handler import WorkflowHandler
from .workflow import MainWorkflow, HumanResponseEvent, ProgressEvent, InputRequiredEvent
from colorama import Fore, Style

import json, uuid, os
import asyncio

class ChatConsumerDemo(AsyncWebsocketConsumer):
  async def connect(self):
    self.user = self.scope['user']
    self.messages = []
    await self.accept()

  async def disconnect(self, code):
    pass
  
  async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message_text = text_data_json["message"]

    if not message_text.strip():
      return
    
    # print("Message:", message_text)
    
    # Show users message
    user_message_html = render_to_string(
      "chat/user_msg.html",
      {
        "message_text": message_text,
      },
    )

    # Adding message to history

    self.messages.append(
      {
        "role": "user",
        "content": message_text
      }
    )

    await self.send(text_data=user_message_html)

    # render an empty text 

    message_id = uuid.uuid4().hex
    contents_div_id = f"message-response-{message_id}"
    system_message_html = render_to_string(
      "chat/ai_msg.html",
      {
        "contents_div_id": contents_div_id,
      },
    )

    await self.send(text_data=system_message_html)

    w = MainWorkflow(timeout=None, verbose=True)

    chunks = []
    handler = w.run(request=message_text)

    async for event in handler.stream_events():
      try:
        print("ASYNC EVENT STREAM:", event.msg)
        chunks.append(event)
        chunk = f'<div hx-swap-oob="beforeend:#{contents_div_id}">{_format_token(event.msg)}</div>'
        await self.send(text_data=chunk)
      except:
        pass

    system_message = await handler
    
    final_message_html = render_to_string(
      'chat/ai_msg_final.html',
      {
        'contents_div_id': contents_div_id,
        'message': system_message,
      },
    )

    # Save message

    self.messages.append(
      {
        "role": "system",
        "content": system_message,
      }
    )

    print("TOTAL:", self.messages)

    await self.send(text_data=final_message_html)

def _format_token(token: str) -> str:
  # apply very basic formatting while we're rendering tokens in real-time
  token = token.replace("\n", "<br>")
  return token