from db import DbService
from models import User
from custom_exceptions import RepositoryError
from models.controllers import ProfileController
import models.repositories

class UserRepository:
    __db = None
    
    def __init__(self, db: DbService):
        self.__db = db
        

    def create_user(self, user: User):
        try:
            query = "INSERT INTO blog_user (user_name, password, profile_id) VALUES ('{username}', '{password}', {profile_id})"
            query = query.format(
                username = user.user_name, 
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def login_user(self, username, password):
        
        try:
            query = "SELECT * FROM blog_user WHERE user_name = '{username}' AND password = '{password}'"
            query = query.format(username= username, password= password)
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                user = User.from_dict(self.__db.cursor.fetchone())

                if user:
                    profile_repo = models.repositories.ProfileRepository(self.__db)
                    profile_controller = ProfileController(profile_repo)
                    profile = profile_controller.select_profile(user.profile_id)

                    if profile:
                        return (user, profile)
            elif self.__db.cursor.rowcount > 1:
                raise RepositoryError
                
            return (None, None)
        except Exception as ex:
            print(ex)


    def select_user_by_username(self, username):
        try:
            query = "SELECT * FROM blog_user WHERE user_name = '%s'" % username
            self.__db.execute(query)
            if self.__db.cursor.rowcount > 0:
                return User.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as ex:
            print(ex)
            raise RepositoryError


    def select_user(self, id):

        try:
            query = "SELECT * FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return User.from_dict(self.__db.cursor.fetchone())
            else:
                return None
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def update_user(self, user: User):

        try:
            query = "UPDATE blog_user SET user_name = '{username}', password = '{password}', profile_id = {profile_id} WHERE id = {id}"
            query = query.format(
                id = user.id,
                username = user.username,
                password = user.password,
                profile_id = user.profile_id
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def delete_user(self, id):

        try:
            query = "DELETE FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def select_user_id(self, username):
        try:
            query = "SELECT id FROM blog_user where user_name = '%s'" % username
            self.__db.execute(query)

            if self.__db.cursor.rowcount >= 1:
                return self.__db.cursor.fetchone()['id']
            else:
                return None
        except Exception as ex:
            print(ex)
            raise 


    def select_prof_id(self, username):
        try:
            query = "SELECT profile_id FROM blog_user where user_name = '%s'" % username

            self.__db.execute(query)

            if self.__db.cursor.rowcount >= 1:

                return self.__db.cursor.fetchone()['profile_id']
            else:
                return None
        except Exception as ex:
            print(ex)
            raise 