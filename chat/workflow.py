from llama_index.core.workflow import (step, StartEvent, StopEvent, Workflow, Event, Context, HumanResponseEvent, InputRequiredEvent)
from llama_index.core.agent import FunctionCallingAgentWorker 
from llama_index.core.tools import FunctionTool
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.utils.workflow import draw_all_possible_flows
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from colorama import Fore, Style
from typing import (Optional, List, Callable)
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from asyncio import sleep
from asyncio import sleep
import os, asyncio
from chat import prompts

load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or a list of specific allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Events that runs custom functions

class InitializeEvent(Event):
	pass

class ConciergeEvent(Event):
    request: Optional[str] = None
    just_completed: Optional[str] = None
    need_help: Optional[bool] = None

class OrchestratorEvent(Event):
	request: str

class GraphGenerateEvent(Event):
	request: str

class DataFrameLookupEvent(Event):
	request: str

# we emit progress events to the frontend so the user knows what's happening
class ProgressEvent(Event):
    msg: str


class MainWorkflow(Workflow):
	"""Main Workflow

	The main workflow that runs the whole application's steps, calling all the Events from StartEvent -> StopEvent.
	"""
  
	@step(pass_context=True)
	async def concierge(self, ctx: Context, ev: StartEvent) -> OrchestratorEvent:
		message = f"I am thinking how to solve this... '{ev.request}'\n\n"
		ctx.write_event_to_stream(ProgressEvent(msg=message))
		await sleep(3)  # Adjust the duration as needed
		message = f"There should be a way... '{ev.request}'\n\n"
		ctx.write_event_to_stream(ProgressEvent(msg=message))
		await sleep(3)  # Adjust the duration as needed
		message = f"Maybe I can implement this... to solve this...\n\n"
		ctx.write_event_to_stream(ProgressEvent(msg=message))
		await sleep(3)  # Adjust the duration as needed
		message = f"I am fetching the solutions...\n\n"
		ctx.write_event_to_stream(ProgressEvent(msg=message))
		await sleep(1)  # Adjust the duration as needed
		return OrchestratorEvent(request=ev.request)
	
	@step(pass_context=True)
	async def orchestrator(self, ctx: Context, ev: OrchestratorEvent) -> StopEvent:
		
		llm = OpenAI(model="gpt-3.5-turbo")
		gen = llm.stream_complete(ev.request)
		for response in gen:
			print(response.text, end="", flush=True)

		print(f"Orchestrator received a request: {ev.request}")
		ctx.write_event_to_stream(ProgressEvent(msg="Running the Orchestrator\n\n"))

		await sleep(3)  # Adjust the duration as needed

		return StopEvent(result = response.text)

async def main(request: str):
	wf = MainWorkflow(timeout=100, verbose=False)
	result = await wf.run()
	return {"query": request.query, "result": result}

	# Save as HTML
	workflow_dot  = draw_all_possible_flows(wf, filename="workflow.html")

if __name__ == "__main__":
	asyncio.run(main())

from llama_index.core.workflow.handler import WorkflowHandler

# create a websocket endpoint for our app
# @app.websocket("/app/chat")
# async def query_endpoint(websocket: WebSocket):
#     await websocket.accept()

#     # instantiate our workflow with no timeout
#     workflow = MainWorkflow(timeout=None, verbose=False)

#     try:
#         # the first thing we should receive is a query
#         query_data = await websocket.receive_json()
#         # we pass it to the workflow
#         handler: WorkflowHandler = workflow.run(query=query_data["question"])

#         # now we handle events coming back from the workflow
#         async for event in handler.stream_events():
#             # if we get an InputRequiredEvent, that means the workflow needs human input
#             # so we send an event to the frontend that will be handled specially
#             if isinstance(event, InputRequiredEvent):
#                 await websocket.send_json({
#                     "type": "input_required",
#                     "payload": event.payload
#                 })
				
#                 # we expect the next thing from the socket to be human input
#                 response = await websocket.receive_json()
#                 # which we send back to the workflow as a HumanResponseEvent
#                 handler.ctx.send_event(HumanResponseEvent(response=response["response"]))
#             elif isinstance(event, ProgressEvent):
#                 # the workflow also emits progress events which we send to the frontend
#                 await websocket.send_json({
#                     "type": "progress", 
#                     "payload": str(event.msg)
#                 })

#         # this only happens when the workflow is complete
#         final_result = await handler
#         await websocket.send_json({
#             "type": "final_result", 
#             "payload": str(final_result)
#         })

#     except Exception as e:
#         await websocket.send_json({"type": "error", "payload": str(e)})
#     finally:
#         await websocket.close()
