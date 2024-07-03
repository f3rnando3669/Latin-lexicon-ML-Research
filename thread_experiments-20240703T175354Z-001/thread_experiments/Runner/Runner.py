from ClientUtils.StringValidation import emptyString

class Runner:

    def __init__(self, client, thread_id, assistant_id, system_instructions) -> None:
        self._client = client
        self._thread_id = thread_id
        self._assistant_id = assistant_id
        self._system_instructions = system_instructions
        self._threads = client.beta.threads.runs
        self._history = []
    
    def getId(self):
        return self._thread.id
    
    def addMessage(self, content, role="user"):
        if emptyString(content):
            Exception("Empty Message!")
        else:
            self._messages.append(
                self._client.beta.threads.messages.create(
                    thread_id = self.getId(),
                    role = role,
                    content = content
                )
            )
    
    def run(self):
        run = None

        if self._system_instructions:
            run = self._run.create_and_poll(
                thread_id=self._thread_id,
                assistant_id=self._assistant_id,
                instructions=self._system_instructions
            )
        else:
            run = self._run.create_and_poll(
                thread_id=self._thread_id,
                assistant_id=self._assistant_id,
            )

        self._history.append(run)
        return run
    
    def acesslastrun(self):
        run = self._history[-1]
        if run.status == 'completed':
            print(run.status)
            return self._client.beta.threads.messages.list(
                thread_id=self._thread_id
            )
        else:
            print(run.status)
    
    def clearmessages(self):
        self._messages.clear()