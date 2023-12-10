
class Links:
    """ HOST = ""
    LOGIN_PAGE = f"{HOST}/auth/login"
    DASHBOARD_PAGE = f"{HOST}/dashboard/index"
    PERSONAL_PAGE = f"{HOST}/pim/viewPersonalDetails/empNumber/7" """

    def __init__(self) -> None:
        self._host = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    def __str__(self) -> str:
        return f' HOST: {self.host}, List: {self.lst}'
