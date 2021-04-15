from menu import BaseMenu
from utils import *
from models import Context, Post
from custom_exceptions import ExitStartMenuException
import os

class ProfileMenu(BaseMenu):
    __header = '-' * 10 + ' Profile ' + '-' * 10
    __options = ('[1] - Edit first name\n[2] - Edit second name\n[3] - Edit last name\n[4] - Edit age\n[5] - Delete page\n[6] - back')
    __next_menus = {}

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()
        self.__next_menus = {
            '1': self.edit_first_name,
            '2': self.edit_second_name,
            '3': self.edit_last_name, 
            '4': self.edit_age,
            '5': self.delete_page,
            '6': lambda *_: raise_exception(ExitFromMenuException)
        }


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            print(self.__context.profile)
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return


    def edit_first_name(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func('Enter new first name: ')

        new_first_name = self.input_secure_wrap(curr_name_input)

        self.__context.profile.first_name = new_first_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print('DB error!')
        else:
            input('First name changed successfully 🗸\nPress Enter...')


    def edit_second_name(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func('Enter new second name: ')

        new_second_name = self.input_secure_wrap(curr_name_input)
        
        self.__context.profile.second_name = new_second_name
        if not self.__profile_controller.update_profile(self.__context.profile):
            print('DB error!')
        else:
            input('second name changed successfully 🗸\nPress Enter...')


    def edit_last_name(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func('Enter new last name: ')

        new_last_name = self.input_secure_wrap(curr_name_input)
        
        self.__context.profile.last_name = new_last_name
        if not self.__profile_controller.update_profile(self.__context.profile):
            print('DB error!')
        else:
            input('last name changed successfully 🗸\nPress Enter...')


    def edit_age(self):

        while True:
            new_age = input('Enter new age: ')
            if new_age.isdigit():
                break
            else:
                print('try again')
        
        self.__context.profile.age = new_age
        if not self.__profile_controller.update_profile(self.__context.profile):
            print('DB error!')
        else:
            input('age changed successfully 🗸\nPress Enter...')


    def delete_page(self):

        while True:
            
            yn = input('are you sure you want to delete the page?\n y/n: ')  

            if yn == "y" or yn == "д":
                try:
                    user_id = self.__user_controller.select_user_id(self.__context.user.user_name)
                    profile_id = self.__user_controller.select_prof_id(self.__context.user.user_name)
                    sel_user_id = self.__user_controller.select_user_id(self.__context.user.user_name)
                    
                    delete_post = self.__post_controller.all_delete_post(user_id)
                    delete_user = self.__user_controller.delete_user(sel_user_id)
                    delete_prof = self.__profile_controller.delete_profile(profile_id)

                    os.system("python main.py")
                    
                    quit()

                except Exception as ex:
                    print(ex)
                    raise RepositoryError

            elif yn == "т" or yn == "n":
                break
            else:
                print("Invalid value entered!")

        input('removal completed 🗸\nPress Enter....')

        return