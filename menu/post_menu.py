from menu.basemenu import BaseMenu
from utils import *
from models.context import Context
from models.repositories.post_repositories import PostRepository
from db.db_service import DbService

class PostMenu(BaseMenu):
    __header = '-' * 10 + ' Tape ' + '-' * 10
    __options = ('[1] - Back\n')
    __next_menus = {}

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()
        self.__next_menus = {
            '1': lambda *_: raise_exception(ExitFromMenuException)
        }

    def show(self):
        db = DbService()
        post_rep = PostRepository(db)
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            post_rep.tape_select_post()
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return

        