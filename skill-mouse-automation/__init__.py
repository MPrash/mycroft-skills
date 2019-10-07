from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from pynput.mouse import Button,Controller

class MouseAutomationSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MouseAutomationSkill, self).__init__(name="MouseAutomationSkill")

        

    @intent_handler(IntentBuilder("MouseLocation").require("Mouse_Location"))
    def handle_mouse_location_intent(self, message):
        mouse = Controller()
        (x,y) = mouse.position
        self.speak_dialog("mouse.location",data={"left_position": x,"top_position": y})

    @intent_handler(IntentBuilder("MouseMoveUp").require("Mouse_Move").require("Up"))
    def handle_mouse_move_up_intent(self, message):
        mouse = Controller()
        mouse.move(0,-50)
        self.speak_dialog("mouse.move",data={"direction": "Up","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseMoveDown").require("Mouse_Move").require("Down"))
    def handle_mouse_move_down_intent(self, message):
        mouse = Controller()
        mouse.move(0,+50)
        self.speak_dialog("mouse.move",data={"direction": "Down","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseMoveLeft").require("Mouse_Move").require("Left"))
    def handle_mouse_move_left_intent(self, message):
        mouse = Controller()
        mouse.move(-50,0)
        self.speak_dialog("mouse.move",data={"direction": "Left","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseMoveRight").require("Mouse_Move").require("Right"))
    def handle_mouse_move_right_intent(self, message):
        mouse = Controller()
        mouse.move(+50,0)
        self.speak_dialog("mouse.move",data={"direction": "Right","move_pixels": 50})

    @intent_handler(IntentBuilder("MouseScrollUp").require("Mouse_Scroll").require("Up"))
    def handle_mouse_scroll_up_intent(self, message):
        mouse = Controller()
        mouse.scroll(0,10)
        self.speak_dialog("mouse.scroll",data={"direction": "Up","scroll_steps": 10})

    @intent_handler(IntentBuilder("MouseScrollDown").require("Mouse_Scroll").require("Down"))
    def handle_mouse_scroll_down_intent(self, message):
        mouse = Controller()
        mouse.scroll(0,-10)
        self.speak_dialog("mouse.scroll",data={"direction": "Down","scroll_steps": 10})

    @intent_handler(IntentBuilder("MouseScrollLeft").require("Mouse_Scroll").require("Left"))
    def handle_mouse_scroll_left_intent(self, message):
        mouse = Controller()
        mouse.scroll(-10,0)
        self.speak_dialog("mouse.scroll",data={"direction": "Left","scroll_steps": 10})

    @intent_handler(IntentBuilder("MouseScrollRight").require("Mouse_Scroll").require("Right"))
    def handle_mouse_scroll_right_intent(self, message):
        mouse = Controller()
        mouse.scroll(10,0)
        self.speak_dialog("mouse.scroll",data={"direction": "Right","scroll_steps": 10}) 

def create_skill():
    return MouseAutomationSkill()
