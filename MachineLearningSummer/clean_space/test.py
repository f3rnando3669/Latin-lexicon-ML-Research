from Clients.ClientInterface import ClientInterface
from Clients.ContextFreeClient import ContextFreeClient
from Clients.ContextTightClient import ContextTightClient
from Prompts.Prompt import Prompt
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from Clients.Utilities.FileUtilities import readjson, readfile, write_to_file

# Testing ContextTight Client
# text = readfile(r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/text.txt")
# prompt = SimplePrompt(text)
# prompt2 = SimplePrompt("Apply (Apply <A> to <C>) to \"You must avoid medical doctors when ill because otherwise you will become lazy.\"")
# # prompt3 = SimplePrompt("Apply <C> to <h>")
# prompts = PromptList()
# prompts.add_userprompts([prompt, prompt2])
# client_interface = ClientInterface(ContextTightClient)
# # jsonp = r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/responsehistory.json"
# tpath = r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/"
# client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")

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

# # Liam's Experiment

parameters = readfile(r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\MachineLearningSummer\clean_space\sentence_parameter.txt")

parameter_set = SimplePrompt(parameters)
sent_1 = SimplePrompt("Apply <Full_Sent> to the string \'There is a time in every man's education when he arrives at the conviction that envy is ignorance; that imitation is suicide; that he must take himself for better for worse as his portion; that though the wide universe is full of good, no kernel of nourishing corn can come to him but through his toil bestowed on that plot of ground which is given to him to till.\'")
sent_2 = SimplePrompt("Apply <Full_Sent> to the string \'That power which resides in him is new in nature, and none but he knows what that is which he can do, nor does he know until he has tried.\'")
sent_3 = SimplePrompt("Apply <Full_Sent> to the string \'Not for nothing one face, one character, one fact, makes much impression on him and another none.\'")
sent_4 = SimplePrompt("Apply <Full_Sent> to the string \'This sculpture in the memory is not without pre-established harmony.\'")
sent_5 = SimplePrompt("Apply <Full_Sent> to the string \'The eye was placed where one ray should fall, that it might testify of that particular ray.\'")
sent_6 = SimplePrompt("Apply <Full_Sent> to the string \'We but half express ourselves, and are ashamed of that divine idea which each of us represents.\'")
sent_7 = SimplePrompt("Apply <Full_Sent> to the string \'It may be safely trusted as proportionate and of good issues, so it be faithfully imparted, but God will not have his work made manifest by cowards.\'")
sent_8 = SimplePrompt("Apply <Full_Sent> to the string \'A man is relieved and gay when he has put his heart into his work and done his best; but what he has said or done otherwise shall give him no peace.\'")
sent_9 = SimplePrompt("Apply <Full_Sent> to the string \'It is a deliverance which does not deliver.\'")
sent_10 = SimplePrompt("Apply <Full_Sent> to the string \'In the attempt his genius deserts him; no muse befriends; no invention, no hope.\'")

prompts = PromptList()

prompts.add_userprompts([parameter_set, sent_4])

client_interface = ClientInterface(ContextTightClient)
tpath = r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\MachineLearningSummer\clean_space"
client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")

# Andi's Experiment
# params = readfile(r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/rule_book_bank/RAW_Rulebooks_14.txt")
# param_prompt = SimplePrompt(params)
# prompt = SimplePrompt("Apply <IDAA> to \"You should eat more vegetables because they are green\"")
# prompts = PromptList()
# prompts.add_userprompts([param_prompt, prompt])
# client_interface = ClientInterface(ContextTightClient)
# tpath = r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/clean_space"
# client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")