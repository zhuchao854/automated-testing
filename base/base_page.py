from base.box_driver import BoxDriver
class BasePage():
    def __init__(self,base_driver:BoxDriver):
        self.base_driver = base_driver