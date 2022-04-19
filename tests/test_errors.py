import brownie
from brownie.exceptions import VirtualMachineError


def test_require(contract):
    with brownie.reverts("test/require"):
        contract.testRequire()


def test_custom_error(contract):
    tx = None
    try:
        tx = contract.testCustomError()
    except VirtualMachineError as ex:
        assert "CustomError" in str(ex)


def test_custom_error_in_library(contract):
    tx = None
    try:
        tx = contract.testCustomErrorInLibrary()
    except VirtualMachineError as ex:
        assert "CustomLibraryError" in str(ex)
