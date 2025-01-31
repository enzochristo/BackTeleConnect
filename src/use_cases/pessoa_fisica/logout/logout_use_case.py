

class LogoutPessoaFisicaUseCase:
    def execute(self, response):
        # Remove o cookie do cliente, garantindo o logout
        response.delete_cookie("pessoa_fisica_auth_token")
        return {"message": "Logout successful. Please log in again."}
