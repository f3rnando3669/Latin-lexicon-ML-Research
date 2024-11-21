from Clients.ClientInterface import ClientInterface
from Clients.ContextFreeClient import ContextFreeClient
from Clients.ContextTightClient import ContextTightClient
from Prompts.Prompt import Prompt
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from Clients.Utilities.FileUtilities import readjson, readfile, write_to_file
# import sys
# sys.path.insert(1, 'Computer-Science-Research-Summer-master/MachineLearningSummer/clean_space/test')
# from test import 


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

#Testing ContextTight Client and json writing 
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

#parameters = readfile(r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\MachineLearningSummer\clean_space\sentence_parameter.txt")

#parameter_set = SimplePrompt(parameters)
sent_1 = SimplePrompt("Apply <Full_Sent> to the string \'It seems to me that it was far from right for the Professor of English in Yale, the Professor of English Literature in Columbia, and Wilkie Collins to deliver opinions on Cooper's literature without having read some of it.\'")
sent_2 = SimplePrompt("Apply <Full_Sent> to the string \'It would have been much more decorous to keep silent and let persons talk who have read Cooper.\'")
sent_3 = SimplePrompt("Apply <Full_Sent> to the string \'Cooper's art has some defects.\'")
sent_4 = SimplePrompt("Apply <Full_Sent> to the string \'In one place in Deerslayer, and in the restricted space of two-thirds of a page, Cooper has scored 114 offenses against literary art out of a possible 115.\'")
sent_5 = SimplePrompt("Apply <Full_Sent> to the string \'It breaks the record.\'")
sent_6 = SimplePrompt("Apply <Full_Sent> to the string \'There are nineteen rules governing literary art in the domain of romantic fiction--some say twenty-two.\'")
sent_7 = SimplePrompt("Apply <Full_Sent> to the string \'In Deerslayer Cooper violated eighteen of them.\'")
sent_8 = SimplePrompt("Apply <Full_Sent> to the string \'These eighteen require:\'")
sent_9 = SimplePrompt("Apply <Full_Sent> to the string \'That a tale shall accomplish something and arrive somewhere\'")
sent_10 = SimplePrompt("Apply <Full_Sent> to the string \'But the Deerslayer tale accomplishes nothing and arrives in the air.\'")
sent_11 = SimplePrompt("Apply <Full_Sent> to the string \'They require that the episodes of a tale shall be necessary parts of the tale and shall help to develop it.\'")
sent_12 = SimplePrompt("Apply <Full_Sent> to the string \'But as the Deerslayer tale is not a tale, and accomplishes nothing and arrives nowhere, the episodes have no rightful place in the work, since there was nothing for them to develop.\'")
sent_13 = SimplePrompt("Apply <Full_Sent> to the string \'They require that the personages in a tale shall be alive, except in the case of corpses, and that always the reader shall be able to tell the corpses from the others.\'")
sent_14 = SimplePrompt("Apply <Full_Sent> to the string \'But this detail has often been overlooked in the Deerslayer tale....\'")

prompts = PromptList()

#prompts.add_userprompts([parameter_set, sent_13])

client_interface = ClientInterface(ContextTightClient)
#tpath = r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\MachineLearningSummer\clean_space"
#client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")

# Andi's Experiment
# params = readfile(r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/rule_book_bank/RAW_Rulebooks_14.txt")
# param_prompt = SimplePrompt(params)
# prompt = SimplePrompt("Apply <IDAA> to \"You should eat more vegetables because they are green\"")
# prompts = PromptList()
# prompts.add_userprompts([param_prompt, prompt])
# client_interface = ClientInterface(ContextTightClient)
# tpath = r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/clean_space"
# client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")
    # prompt = SimplePrompt(f"Classify \"{article}\" as of type <G>, <FE>, <IR>, <RR>, <WCB>, <FU> or <DEP>. Take it step by step.")
    
    
    
def generate_response(text):  
    prompt = SimplePrompt(text)
    prompts.add_userprompts([prompt])
    client_interface = ClientInterface(ContextFreeClient)
    client = client_interface._client
    response = client.generate(prompts=prompts)
    return response
if __name__ == "__main__":
    print(generate_response(input()))
    