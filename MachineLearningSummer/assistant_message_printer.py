from openai import OpenAI
import time
import json

SENTENCE_ID = "asst_jwqKl7o85yHTcQYO1s66J2QF"

def show_json(obj):
    print(json.loads(obj.model_dump_json()))

def get_response(thread):
    messages = client.beta.threads.messages.list(
    thread_id = thread,)
    return pretty_print(messages)
    
def pretty_print(messages):
    print("# Messages")
    for m in reversed(messages.data):
        print(f"{m.role}: {m.content[0].text.value}")
    print()

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

client = OpenAI(api_key="sk-proj-zhneKzEWaF5adbdJPBPmT3BlbkFJk8yS2iJVC501GP79GVwx")
assistant = client.beta.assistants.retrieve(
    SENTENCE_ID,
)

get_response("thread_IJXuYr299aws9Wv1oDtRz7BP")


show_json(assistant)