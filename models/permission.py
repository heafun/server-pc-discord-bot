class Permission:

    def __init__(self):
        self.roles = []
        self.users = []

    def add_role(self, role_id: str):
        self.roles.append(role_id)

    def add_user(self, user_id):
        self.users.append(user_id)
