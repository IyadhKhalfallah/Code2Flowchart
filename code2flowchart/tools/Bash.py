from langchain.utilities import BashProcess


class Bash:
    def __init__(self):
        self.bash = BashProcess()

    def cmd(self, command):
        return self.bash.run(command)
