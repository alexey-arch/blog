from db import DbService
from models import User
from models.repositories import *
from models.controllers import *
from custom_exceptions import RepositoryError
from menu.start_menu import StartMenu


def main():
    db = DbService()

    user_repo = UserRepository(db)
    profile_repo = ProfileRepository(db)
    post_repo = PostRepository(db)

    user_controller = UserController(user_repo)
    profile_controller = ProfileController(profile_repo)
    post_controller = PostController(post_repo)
    
    app = StartMenu(user_controller, profile_controller, post_controller)
    app.show()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Disconnecting from DB...')
        db = DbService()
        db.close()
        print('Bye!')