from Clients.ClientInterface import ClientInterface
from Clients.ContextFreeClient import ContextFreeClient
from Clients.ContextTightClient import ContextTightClient
from Prompts.Prompt import Prompt
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from Clients.Utilities.FileUtilities import readjson

# # Testing Context-Free Client
# prompt = Prompts.SimplePrompt.SimplePrompt()
# prompt.setprompt("How are you?")
# prompts = Prompts.PromptList.PromptList()
# prompts.add_systemprompt(prompt=prompt)

# client_interface = Clients.ClientInterface.ClientInterface()
# print(client_interface._client.generate(prompts=prompts))

# Testing ContextTight Client and json writing 
# prompt = SimplePrompt()
# prompt.setprompt("How are you?")
# prompts = PromptList()
# prompts.add_userprompt(prompt)
# client = ClientInterface(client=ContextTightClient)._client
# jsonloaded = readjson("jsontext.json")
# client.loadcontext_fromjson(jsonloaded)
# response = client.generate(prompts=prompts, json_savepath="jsontext.json")
# print(response)
# newjson = readjson("jsontext.json")
# print(newjson)