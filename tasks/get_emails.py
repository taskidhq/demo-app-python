from taskid import Task, TextInput

class GetEmails(Task):
    def name():
        return "Tiago"

    def description():
        return "Joao"

    def inputs():
        return [TextInput("user_id", "User ID", "usr_123")]

    def run(inputs):
        return {"tiago": "botelho"}
