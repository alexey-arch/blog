from menu import BaseMenu
from utils import *
from models.context import Context
from models.repositories import PostRepository
from models.post import Post

class WallMenu(BaseMenu):
    __header = '-' * 10 + ' My wall ' + '-' * 10
    __options = ('[1] - Create post\n[2] - Delete post\n[3] - edit post\n[4] - Back\n')
    __next_menus = {}

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context
        self.__post = Post
        self.__next_menus = {
            '1': self.create_post, 
            '2': self.delete_post,
            '3': self.update_post,
            '4': lambda *_: raise_exception(ExitFromMenuException)
        }

    def show(self):
        post = PostRepository
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')

            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException

            return selected_option

        while True:
            print(self.__header)

            user_id = self.__user_controller.select_user_id(self.__context.user.user_name)
            self.__post_controller.select_post(user_id)

            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return


    def create_post(self):
        try:
            input_post_func = get_post_input()
            
            def curr_title_input():
                return input_post_func('Enter title text: ')

            def curr_describe_input():
                return input_post_func('Enter describe text: ')

            title = self.input_secure_wrap(curr_title_input)
            describe = self.input_secure_wrap(curr_describe_input)

            user_id = self.__user_controller.select_user_id(self.__context.user.user_name)
            
            new_post = Post(user_id = user_id, title= title, description = describe)

            if self.__post_controller.create_post(new_post):
                print('DB error!')

            else:
                input('post created successfully 🗸\n Press Enter ...')
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def delete_post(self):
        try:
            input_id_func = get_option_input()
            
            def curr_id_input():
                return input_id_func('Enter id: ')

            delete_id = self.input_secure_wrap(curr_id_input)
            
            delete = self.__post_controller.delete_post(int(delete_id))
        
        except Exception as ex:
            print(ex)
            raise RepositoryError

    def update_post(self):
        try:
            input_id_func = get_option_input()
            input_post_func = get_post_input()
            def curr_id_input():
                return input_id_func('Enter post id: ')

            def curr_title_input():
                return input_post_func('Enter new title: ')            
            
            def curr_describe_input():
                return input_post_func('Enter new describe: ') 

            post_id = self.input_secure_wrap(curr_id_input)
            ed_title = self.input_secure_wrap(curr_title_input)
            ed_describe = self.input_secure_wrap(curr_describe_input)

            user_id = self.__user_controller.select_user_id(self.__context.user.user_name)
            
            ed_post = Post(user_id = user_id, id = post_id, title= ed_title, description = ed_describe)

            if self.__post_controller.update_post(ed_post):
                print('DB error!')
            else:
                input('post created successfully!\n Press Enter ...')

        except Exception as ex:
            print(ex)
            raise RepositoryError