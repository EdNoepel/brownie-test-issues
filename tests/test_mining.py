from brownie import accounts


def test_mine(chain, contract):
    chain.sleep(14)                         # this works with Ganache and Hardhat
    contract.doSomething({"from": accounts[0]})

    chain.mine(blocks=2)                    # this works with Ganache and Hardhat
    contract.doSomething({"from": accounts[0]})

    chain.mine(blocks=2, timedelta=28)      # this works with Ganache but not Hardhat
    contract.doSomething({"from": accounts[0]})
