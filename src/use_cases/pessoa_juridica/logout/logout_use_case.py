class LogoutPessoaJuridicaUseCase:
    def execute(self, response):
        response.delete_cookie("pessoa_juridica_auth_token")
        return {"message": "Logout successful. Please log in again."}
