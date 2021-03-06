from mycroft import MycroftSkill, intent_file_handler


class Pass(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pass.intent')
    def handle_pass(self, message):
        self.speak_dialog('pass')


def create_skill():
    return Pass()

