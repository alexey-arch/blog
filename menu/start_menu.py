from menu import BaseMenu
from utils import get_option_input, raise_exception
from custom_exceptions import UserInputOptionException, ExitFromMenuException
from menu.sign_up import RegistrationMenu
from menu.log_menu import LoginMenu
import sys
from db.db_service import DbService

class StartMenu(BaseMenu):
    db = DbService()
    __header = '-' * 10 + ' Blog ' + '-' * 10
    __options = '[1] - Sign in\n[2] - Sign up\n[3] - Exit'
    __next_menus = {
        '1': LoginMenu,
        '2': RegistrationMenu,
        '3': lambda *_: quit('Disconnecting from DB...\ngood bay!')
    }

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option
        
        while True:
            print(self.__header)
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)
            
            next_menu = self.__next_menus[selected_option](
                self.__user_controller,
                self.__profile_controller, 
                self.__post_controller
            )
            next_menu.show()