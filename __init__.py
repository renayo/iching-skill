from mycroft import MycroftSkill, intent_file_handler


class Iching(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('iching.intent')
    def handle_iching(self, message):
        self.speak_dialog('iching')


def create_skill():
    return Iching()

