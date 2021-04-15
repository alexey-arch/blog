class User:
    __slots__ = ('id', 'create_data', 'user_name', 'password', 'profile_id')

    def __init__(
        self, 
        user_name,  
        password, 
        profile_id,
        id = None, 
        create_data = None
    ):
        self.id = id
        self.create_data = create_data
        self.user_name = user_name
        self.password = password
        self.profile_id = profile_id

    @classmethod
    def from_dict(cls, data):
        return User(**data)