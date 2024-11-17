from Clients.ClientInterface import ClientInterface
from Clients.ContextFreeClient import ContextFreeClient
from Clients.ContextTightClient import ContextTightClient
from Prompts.Prompt import Prompt
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from Clients.Utilities.FileUtilities import readjson, readfile

text = readfile(r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/main2test.txt")
init_prompt = SimplePrompt(text)
# init_prompt.setprompt(text)
followup1 = "Apply <A> to <y>"
followup1prompt = SimplePrompt(followup1)
followup2 = "Apply <C> to <h>"
followup2prompt =  SimplePrompt(followup2)
promptlist =  PromptList()
promptlist.add_userprompts([init_prompt, followup1prompt, followup2prompt])
# print(promptlist)
client_interface = ClientInterface(ContextTightClient)
response = client_interface._client.generate(promptlist, json_savepath="convo.json")