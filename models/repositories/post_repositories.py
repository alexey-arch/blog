from db import DbService
from models import Post
from custom_exceptions import RepositoryError
from models.controllers import PostController 
import models.repositories

class PostRepository:
    __db = None
    def __init__(self, db: DbService):
        self.__db = db

    def create_post(self, post:Post):
        try:
            query = "INSERT INTO post (user_id, title, description) VALUES ('{user_id}', '{title}','{description}');"
            query = query.format(
                user_id = post.user_id,
                title = post.title,
                description = post.description
            )

            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError

    def select_post(self, post:Post):
        try:
            query = "SELECT * FROM post WHERE user_id = %d;" % post
            self.__db.execute(query)
            if self.__db.cursor.rowcount >= 1:
                for i in self.__db.cursor.fetchall():
                    print('='*30)
                    print(f'{i["creation_date"]}\t id-[{i["id"]}]')
                    print('_'*30)
                    print(f'{i["title"]}')
                    print(f'{i["description"]}')
                    print('='*30)
            else:
                print('no entries')
                None
        except Exception as ex:
            print(ex)
            raise RepositoryError

    def update_post(self, post: Post):
        try:
            query = "UPDATE post SET user_id = {user_id}, title = '{title}', description = '{description}' WHERE id = %d;" %int(post.id)
            query = query.format(
                user_id = post.user_id,
                title = post.title,
                description = post.description,
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def tape_select_post(self):
        try:
            query = "select blog_user.user_name, post.creation_date,  post.title, post.description  from post inner join blog_user on post.user_id = blog_user.id order by post.creation_date ASC"
            self.__db.execute(query)

            if self.__db.cursor.rowcount >= 1:
                for i in self.__db.cursor.fetchall():
                    print('='*30)
                    print(f'{i["user_name"]}')
                    print(f'{i["creation_date"]}')
                    print('_'*30)
                    print(f'{i["title"]}')
                    print(f'{i["description"]}')
                    print('='*30)
            else:
                None
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def delete_post(self, id):
        try:
            query = "DELETE FROM post WHERE id = %d;" %id
            self.__db.execute(query)

        except Exception as ex:
            print(ex)
            raise RepositoryError

    
    def all_delete_post(self, user_id):
        try:

            query = "DELETE FROM post Where user_id =%d;" %user_id

            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError