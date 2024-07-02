from openai import OpenAI

def pretty_print(messages):
    print("# Messages")
    for m in reversed(messages.data):
        print(f"{m.role}: {m.content[0].text.value}")
    print()

client = OpenAI(api_key="sk-proj-zhneKzEWaF5adbdJPBPmT3BlbkFJk8yS2iJVC501GP79GVwx")

messages = client.beta.threads.messages.list(
    thread_id = "thread_IJXuYr299aws9Wv1oDtRz7BP"
)

pretty_print(messages)