from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from pynput.mouse import Button,Controller

class MouseAutomationSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MouseAutomationSkill, self).__init__(name="MouseAutomationSkill")

        

    @intent_handler(IntentBuilder("MouseLocation").require("Location"))
    def handle_mouse_location_intent(self, message):
        mouse = Controller()
        (x,y) = mouse.position
        self.speak_dialog("mouse.location",data={"left_position": x,"top_position": y})

    @intent_handler(IntentBuilder("MouseMoveUp").require("Move").require("MoveUp"))
    def handle_mouse_up_intent(self, message):
        mouse = Controller()
        mouse.move(0,-50)
        self.speak_dialog("mouse.move",data={"direction": "Up","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseMoveDown").require("Move").require("MoveDown"))
    def handle_mouse_down_intent(self, message):
        mouse = Controller()
        mouse.move(0,+50)
        self.speak_dialog("mouse.move",data={"direction": "Down","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseMoveLeft").require("Move").require("MoveLeft"))
    def handle_mouse_left_intent(self, message):
        mouse = Controller()
        mouse.move(-50,0)
        self.speak_dialog("mouse.move",data={"direction": "Left","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseMoveRight").require("Move").require("MoveRight"))
    def handle_mouse_right_intent(self, message):
        mouse = Controller()
        mouse.move(+50,0)
        self.speak_dialog("mouse.move",data={"direction": "Right","move_pixels": 50})

def create_skill():
    return MouseAutomationSkill()
