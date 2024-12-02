class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.transaction = None
        self.transaction_changes = {}

    def get(self, key):
        if self.transaction:
            if key in self.transaction_changes:
                return self.transaction_changes[key]
        return self.db.get(key, None)

    def put(self, key, val):
        if not self.transaction:
            raise Exception("No transaction in progress")
        self.transaction_changes[key] = val

    def begin_transaction(self):
        if self.transaction:
            raise Exception("A transaction is already in progress")
        self.transaction = True
        self.transaction_changes = {}

    def commit(self):
        if not self.transaction:
            raise Exception("No transaction in progress")
        self.db.update(self.transaction_changes)
        self.transaction = None
        self.transaction_changes = {}

    def rollback(self):
        if not self.transaction:
            raise Exception("No transaction in progress")
        self.transaction = None
        self.transaction_changes = {}
