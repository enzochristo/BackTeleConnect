

class LogoutManagerUseCase:
    def execute(self, response):
        response.delete_cookie("manager_auth_token")
        return {"message": "Logout successful. Please log in again."}
