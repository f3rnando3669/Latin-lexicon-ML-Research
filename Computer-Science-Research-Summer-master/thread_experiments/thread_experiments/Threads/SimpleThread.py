from ClientUtils.StringValidation import emptyString

class SimpleThread:

    def __init__(self, client) -> None:
        self._client = client
        self._thread = client.beta.threads.create()
        self._messages = []
    
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
    
    def clearmessages(self):
        self._messages.clear()