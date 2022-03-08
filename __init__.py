import os
import signal
import subprocess

from mycroft import MycroftSkill, intent_handler


class Mines(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.mines_process = None

    @intent_handler("launch-mines.intent")
    def handle_launch_mines(self, message):
        size = message.data.get("size")
        if size in ["large", "big"]:
            size = "--big"
            cmd = ["gnome-mines", size]
        else:
            cmd = ["gnome-mines"]
        self.speak_dialog("launching-mines")
        self.mines_process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid
        )
        self.log.error(self.mines_process)

    @intent_handler("close-mines.intent")
    def handle_close_mines(self, message):
        self.log.error(self.mines_process)
        if self.mines_process is None:
            self.speak_dialog("error_cannot-find-mines-process")
        else:
            self.speak_dialog("closing-mines")
            os.killpg(os.getpgid(self.mines_process.pid), signal.SIGTERM)


def create_skill():
    return Mines()
