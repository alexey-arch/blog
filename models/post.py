class Post:
    __slots__ = ('id', 'creation_date', 'update_at', 'user_id', 'title', 'description')

    def __init__(
        self,
        user_id,
        title,
        id = None,
        creation_date = None,
        update_at = None,
        description = None
    ):
        self.id = id
        self.creation_date = creation_date
        self.update_at = update_at
        self.user_id = user_id
        self.title = title
        self.description = description


    @classmethod
    def from_dict(cls, data):
        return Post(**data)