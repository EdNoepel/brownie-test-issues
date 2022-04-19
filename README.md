# brownie-with-hardhat-example

This project was created to reproduce and illustrate `eth-brownie` issues.
It was created to provide evidence for `eth-brownie` bug reports. 

## Prerequisites
`pipx` and `npm`

## Setup
```
pipx install eth-brownie
npm install --save-dev hardhat
```

## Running
To test with `ganache`:
```
brownie test
```

To test with `hardhat` (more issues):
```
brownie test --network hardhat
```
