from django.shortcuts import render, HttpResponse
from dotenv import load_dotenv
import os, random
load_dotenv()

cards = [
  "How can I optimize my#digital advertising campaigns?",
  "What are the best practices#for audience targeting?",
  "Can you quiz me on#campaign performance metrics?",
  "How do I write ad copy#that resonates with my audience?",
  "Help me create a#digital marketing strategy.",
  "Struggling to meet ROI#targets. Any advice?",
  "What strategies can I use#to reduce ad spend waste?",
  "How can I use data#to improve campaign performance?",
  "Managing multiple campaigns.#Tips for efficiency?",
  "How can I increase#engagement with localized ads?",
]

# def pages(request):
#   try:
#     load_template = request.path.split('/')
#     print("Load Template:", load_template)
#     return HttpResponse(status=405)
#   except:
#     return HttpResponse(status=500)

def index(request):
  return render(request, 'index.html')

def app(request):
  cards_bold, cards_normal = card_choser()

  context = {
     'cards_bold': cards_bold,
     'cards_normal': cards_normal,
     'zipped': zip(cards_bold, cards_normal)
  }

  return render(request, 'app.html', context=context)

def card_choser():
  chosen = random.sample(cards, 4)

  bold_texts = []
  normal_texts = []

  for card in chosen:
    parts = card.split("#")
    bold_texts.append(parts[0])
    normal_texts.append(parts[1])

  return bold_texts, normal_texts

def ai(request):
  from portkey_ai import Portkey

  client = Portkey(
    api_key=os.getenv("PORTKEY_API_KEY"),
    virtual_key=os.getenv("VIRTUAL_KEY"),
  )

  # completion = client.chat.completions.create(
  # prompt_id="pp-ai-therapi-f9b710",
  # variables={}
  # )

  stream_prompt_completion = client.prompts.completions.create(
    prompt_id="pp-ai-therapi-f9b710",
    variables={},
    stream=True
  )

  # Access and handle the response stream using the _iterator attribute
  response_text = ""
  
  for chunk in stream_prompt_completion._iterator:
      # Process each chunk of data here
      # Assuming the chunk is an instance of PromptCompletionChunk
      print(chunk)
      
      # Check if the chunk has a 'text' attribute
      if hasattr(chunk, 'text'):
          response_text += chunk.text
      else:
          # If 'text' attribute is not present, try accessing other potential attributes or methods
          # Adjust this based on the actual structure of PromptCompletionChunk
          if hasattr(chunk, 'data'):
              response_text += chunk.data
          elif hasattr(chunk, 'get_text'):
              response_text += chunk.get_text()
          else:
              response_text += str(chunk)  # Convert to string if no suitable attribute or method is found

  print('\n\nFINAL \n\n')

  print("Complete response:", response_text)
  
  return render(request, 'app.html')

def handler500(request):
  return render(request, 'handler500.html', status=500)

def handler404(request, exception):
  return render(request, 'handler404.html', status=404)