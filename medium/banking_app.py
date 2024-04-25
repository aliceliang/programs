""" started 1:18
1st tier: record and hold transactions (deposits and transfers). done @ 1:39
2nd tier: do data metrics, returning the top k accounts with outgoing money done @ 1:56, revised at 2:22
3rd tier: add scheduled transactions and canceling them done 2:01 
4th tier: merge two accounts while maintaining separate account histories done 2:33
"""
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = 1
    TRANSFER = 2

class Account(object):
    def __init__(self, id):
        self.id = id
        self.transactions = []
        self.balance = 0
        self.merged = False
        self.merged_account = None
    
    def record_transaction(self, transaction):
        # not sure we need to do anything when we cancel a transaction - not clear from prompt
        self.transactions.append(transaction.id)
        if self.merged:
            self.merge_account.transactions.append(transaction.id)

        if transaction.transaction_type == TransactionType.DEPOSIT:
            self.balance += transaction.amount
            if self.merged:
                self.merged_account.balance += transaction.amount
        elif transaction.transaction_type == TransactionType.TRANSFER:
            self.balance -= transaction.amount
            if self.merged:
                self.merged_account.balance -= transaction.amount
        else:
            raise KeyError, 'unsupported TransactionType'
        return True
    
    def merge_account(self, new_account):
        # update balance into new account
        new_account.balance += self.balance
        # update list of transactions into new account
        new_account.transactions.append(self.transactions)

        self.merged = True
        self.merged_account_id = new_account.id
        return

class Transaction(object):
    def __init__(self, id, transaction_type, amount, account_id, scheduled=False, scheduled_time=None):
        self.id = id
        self.transaction_type = transaction_type
        self.amount = amount
        self.account_id = Account(account_id)
        self.scheduled = scheduled
        self.scheduled_time = scheduled_time

    def is_transfer(self):
        return self.transaction_type == TransactionType.TRANSFER

    def is_deposit(self):
        return self.transaction_type == TransactionType.DEPOSIT

    def schedule(self, scheduled_time):
        self.scheduled = True
        self.scheduled_time = scheduled_time
        self.account 

    def cancel_schedule(self):
        self.scheduled = False
        self.scheduled_time = None

class AccountStore(object):
    def __init__(self):
        self.store = {} # account_id: Account
        self.id_counter = 0

    def create_account(self):
        id = self.id_counter
        account = Account(id)
        self.store[id] = account
        return account
    
    def merge_accounts(self, account_1, account_2):
        new_account = Account()
        account_1.merge_account(new_account)
        account_2.merge_account(new_account)
        return new_account

class TransactionStore(object):
    def __init__(self):
        self.store = {} # transaction_id: Transaction
        self.id_counter = 0
    
    def create_transaction(self, transaction_type, amount, account_id):
        id = self.id_counter
        transaction = Transaction(id, transaction_type, amount, account_id)
        self.store[id] = transaction
        self.id_counter += 1
        return transaction

    def get_transaction(self, transaction_id):
        return self.store[transaction_id]
    
    def get_transfers(self):
        def transfer_filter(pair):
            _, value = pair
            return value.is_transfer
        
        return filter(transfer_filter, self.store)

class Bank(object):
    def __init__(self):
        self.transaction_store = TransactionStore()
        self.account_store = AccountStore()

    def create_transaction(self, transaction_type, amount, account_id):
        transaction = self.transaction_store.create_transaction(transaction_type, amount, account_id)
        account = self.account_store[account_id]
        account.record_transaction(transaction)
        return transaction
    
    def hold_transaction(self, transaction_id):
        return self.transaction_store.get_transaction(transaction_id)
    
    def top_k_accounts(self, k):
        """
        Return the top k accounts with outgoing money
        outgoing money = transfer
        incoming money = deposit
        select from the transaction store where 
        """
        accounts = self.account_store.store
        # sort by accounts with greatest balance
        sorted_accounts_desc = sorted(accounts.items(), key=lambda kv: kv[1].balance, reverse=True)
        
        return sorted_accounts_desc[:k]
    
    def schedule_transaction(self, transaction_id, time):
        transaction = self.store.get(transaction_id)
        if transaction is not None:
            transaction.schedule(time)
            return True
        else:
            raise KeyError, f'Transaction {transaction_id} does not exist'
        
    def cancel_transaction(self, transaction_id):
        transaction = self.store.get(transaction_id)
        if transaction is not None:
            transaction.cancel()
            return True
        else:
            raise KeyError, f'Transaction {transaction_id} does not exist'
