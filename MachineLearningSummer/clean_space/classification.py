from Clients.ClientInterface import ClientInterface
from Clients.ContextTightClient import ContextTightClient
from Prompts.SimplePrompt import SimplePrompt
from Prompts.PromptList import PromptList
from Clients.Utilities.FileUtilities import readfile, write_to_file_in_dir
from extract import iscorrect, iscorrect_text

def batch_classify(rbk_path: str, article_to_label_map:dict, batch_dir:str, summary_name='batch_summary')->str:
    params = readfile(rbk_path)
    response_paths = classify(article_to_label_map=article_to_label_map, preprompt=params, batch_dir=batch_dir)
    summary = prepare_summary(response_paths=response_paths, batch_dir=batch_dir, summary_name=summary_name, rulebook=rbk_path)
    return summary

def batch_classify_with_portfolio(rbk_path: str, portfolio_path:str, article_to_label_map:dict, batch_dir:str, summary_name='batch_summary')->str:
    params = readfile(rbk_path)
    portfolio = readfile(portfolio_path)    
    response_paths = classify(article_to_label_map=article_to_label_map, preprompt=params+portfolio, batch_dir=batch_dir)
    summary = prepare_summary(response_paths=response_paths, batch_dir=batch_dir, summary_name=summary_name, rulebook=rbk_path+' and '+portfolio_path)
    return summary

def generate_response(preprompt: str, article: str) -> str:
    # prompt = SimplePrompt(f"Classify \"{article}\" as of type <G>, <FE>, <IR>, <RR>, <WCB>, <FU> or <DEP>. Take it step by step.")
    prompt = SimplePrompt(preprompt+'\n'+f"\nApply <IDAA> to \"{article}\"")
    prompts = PromptList()
    prompts.add_userprompts([prompt])
    client_interface = ClientInterface(ContextTightClient)
    client = client_interface._client
    response = client.generate(prompts=prompts)
    return response

def classify(article_to_label_map: dict, preprompt: str, batch_dir: str) -> list[str]:
    response_paths = []
    print_freq  = len(article_to_label_map) // 10
    counter = 0
    index = 1

    for article in article_to_label_map:
        if article == 'article':
            continue
        response = generate_response(preprompt=preprompt, article=article)
        txt_name = article_to_label_map[article][1:-1]
        path = write_to_file_in_dir(batch_dir, txt_name, response)
        response_paths.append(path)
        counter += 1
        if counter % print_freq == 0:
            print("="*10, f'group_{index}_complete', '='*10 )
            index += 1
    if counter % print_freq != 0:
        print("="*10, f'group_{index}_complete', '='*10 )
    
    return response_paths

def prepare_summary(response_paths, batch_dir, summary_name, rulebook)->str:
    category_details = {}
    incorrect_list = []
    count = 0
    for path in response_paths:
        category = path.split('/')[-1].split('_')[0]
        if category in category_details:
            category_details[category]['Total'] += 1
        else:
            category_details[category] = {'Total':1, 'Correct':0}
        correct = iscorrect(path)
        if correct:
            count += 1
            if category in category_details:
                category_details[category]['Correct'] += 1
            else:
                category_details[category] = {'Correct':1}
        else:
            incorrect_list.append(path)

    total = len(response_paths)
    summary = f'\nGeneral:\nCorrectly Indentified: {count}\nTotal: {total}\nPercentage: {round(count/total*100, 2)}\n\nBreakdown:'
    for category in category_details:
        correct = category_details[category]['Correct']
        total = category_details[category]['Total']
        summary += f'\n{category}:\nCorrect: {correct}\nTotal: {total}\nPercentage: {correct/total*100}\n'
        summary += "=" * 30
    summary += "\n\nPaths for Incorrect Files:\n"+"\n".join(incorrect_list)
    write_to_file_in_dir(batch_dir, summary_name, summary, text_analyzed=rulebook)
    return summary

def build_portfolio(rbk_path: str, article_to_label_map: dict, portfolio_dir: str, portfolio_name: str) -> str:
    params = readfile(rbk_path)
    path = f'{portfolio_dir}/{portfolio_name}.txt'
    fd = open(path, 'a')
    for article in article_to_label_map:
        if article == 'article':
            continue
        response = generate_response(preprompt=params, article=article)
        tag = article_to_label_map[article]
        correct = iscorrect_text(correct_tag=tag, text=response)
        if correct:
            fd.write(response)
            fd.write(f'\nType of Defective Argument for \'{article}\': {tag}\n\n')
    fd.close()
    return path