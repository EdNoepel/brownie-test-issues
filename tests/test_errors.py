import brownie
import pytest
from brownie.exceptions import VirtualMachineError
from web3 import Web3


def test_require(contract):
    with brownie.reverts("test/require"):
        contract.testRequire()


def test_custom_error(contract):
    tx = None
    try:
        tx = contract.testCustomError()
    except VirtualMachineError as ex:
        assert "CustomError" in str(ex)


def test_custom_error_workaround(contract):
    # thanks to https://github.com/eth-brownie/brownie/issues/1108#issuecomment-937741398
    expected_revert_string = "typed error: " + Web3.keccak(text="CustomError()")[:4].hex()
    with brownie.reverts(expected_revert_string):
        contract.testCustomError()


def test_custom_error_in_library(contract):
    tx = None
    try:
        tx = contract.testCustomErrorInLibrary()
    except VirtualMachineError as ex:
        assert "CustomLibraryError" in str(ex)


def test_custom_error_workaround_in_library(contract):
    # thanks to https://github.com/eth-brownie/brownie/issues/1108#issuecomment-937741398
    expected_revert_string = "typed error: " + Web3.keccak(text="CustomLibraryError()")[:4].hex()
    with brownie.reverts(expected_revert_string):
        contract.testCustomErrorInLibrary()
