from mycroft import MycroftSkill, intent_file_handler


class Mines(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mines.intent')
    def handle_mines(self, message):
        self.speak_dialog('mines')


def create_skill():
    return Mines()

