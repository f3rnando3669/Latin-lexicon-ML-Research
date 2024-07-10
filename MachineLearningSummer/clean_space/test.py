from Clients.ClientInterface import ClientInterface
from Clients.ContextFreeClient import ContextFreeClient
from Clients.ContextTightClient import ContextTightClient
from Prompts.Prompt import Prompt
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from Clients.Utilities.FileUtilities import readjson, readfile, write_to_file

# Testing ContextTight Client
text = readfile(r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/text.txt")
prompt = SimplePrompt(text)
prompt2 = SimplePrompt("Apply (Apply <A> to <C>) to \"You must avoid medical doctors when ill because otherwise you will become lazy.\"")
# prompt3 = SimplePrompt("Apply <C> to <h>")
prompts = PromptList()
prompts.add_userprompts([prompt, prompt2])
client_interface = ClientInterface(ContextTightClient)
# jsonp = r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/responsehistory.json"
tpath = r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/"
client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")

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

# r = readjson("jsontext.json")
# write_to_file("response", r[-1])