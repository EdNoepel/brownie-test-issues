import pytest
from brownie import accounts, TestBrownieWithHardhat


@pytest.fixture
def contract():
    return accounts[0].deploy(TestBrownieWithHardhat)
