pragma solidity ^0.8.0;

import {TestLibraryContract} from "./libraries/TestLibrary.sol";

contract TestBrownieWithHardhat {
    uint256 public counter;
    error CustomError();
    TestLibraryContract public l;

    constructor() {
        l = new TestLibraryContract();
    }

    function testRequire() public {
        require(false, "test/require");
    }

    function testCustomError() public {
        revert CustomError();
    }

    function testCustomErrorInLibrary() public {
        l.testCustomErrorInLibrary();
    }

    function doSomething() external returns (uint256) {
        return counter += 1;
    }
}
