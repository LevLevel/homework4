class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            return False
        self.clients[client_id] = {"name": name}
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            return False
        if client_id in self.accounts:
            return False

        self.accounts[client_id] = {
            "balance": start_balance,
            "years": years,
            "interest_rate": 0.10
        }
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.accounts:
            return False

        account = self.accounts[client_id]
        balance = account["balance"]
        years = account["years"]
        annual_rate = account["interest_rate"]

        monthly_rate = annual_rate / 12
        months = years * 12
        final_balance = balance * (1 + monthly_rate) ** months

        return round(final_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.accounts:
            return False

        final_amount = self.calc_interest_rate(client_id)
        del self.accounts[client_id]
        return final_amount
