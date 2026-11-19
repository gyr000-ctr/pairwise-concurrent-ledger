"""account 核心模块（初始失败环境，待修复）。"""

def lock_account(account_id, locks):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def atomic_debit(balance, amount):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def is_idempotent(request_id, seen):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def rollback(entry, ledger):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def counts_match(balance, entries):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def can_debit(balance, amount):
    """待实现的安全修复入口。"""
    raise NotImplementedError
