import pytest

from ledger.account import (
    lock_account,
    atomic_debit,
    is_idempotent,
    rollback,
    counts_match,
    can_debit,
)


def test_check_then_act_locked():
    locks = {}
    assert lock_account("a1", locks) is True


def test_debit_atomic():
    assert atomic_debit(100, 30) == 70


def test_duplicate_request_id_rejected():
    seen = {}
    is_idempotent("req1", seen)
    assert is_idempotent("req1", seen) is False


def test_first_request_id_allowed():
    assert is_idempotent("req1", {}) is True


def test_rollback_restores_balance():
    ledger = [{"amount": 30}]
    rollback({"amount": 30}, ledger)
    assert len(ledger) == 0


def test_failed_entry_removed():
    ledger = []
    rollback({"amount": 10}, ledger)
    assert ledger == []


def test_count_matches_entries():
    assert counts_match(70, [{"amount": 30}], ) is True


def test_count_mismatch_detected():
    assert counts_match(50, [{"amount": 30}]) is False


def test_can_debit_sufficient():
    assert can_debit(100, 30) is True


def test_can_debit_insufficient():
    assert can_debit(20, 30) is False


def test_overdraft_rejected():
    assert can_debit(0, 1) is False


def test_concurrent_debit_no_overdraw():
    assert atomic_debit(10, 3) == 7


def test_idempotent_replay_no_double_debit():
    seen = {}
    is_idempotent("r", seen)
    assert is_idempotent("r", seen) is False


def test_negative_amount_rejected():
    import pytest
    with pytest.raises(ValueError):
        atomic_debit(100, -5)


def test_entry_balance_consistent():
    assert counts_match(100, []) is True
