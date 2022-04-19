pragma solidity ^0.8.0;

contract TestLibraryContract {
    error CustomLibraryError();

    function testCustomErrorInLibrary() public {
        revert CustomLibraryError();
    }
}
