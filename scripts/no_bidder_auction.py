from brownie import Sealed_Bid_Auction, accounts
from scripts.helpful_scripts import *
from scripts.deploy import deploy_sealed_bid_auction_contract
from web3 import Web3
import time


def run_no_bidder_auction():
    print("I will now show an example of an auction with no bidders\n")

    deploy_sealed_bid_auction_contract()

    getOwner()

    getNFT()

    print("Lets check to see if the auction is open!\n")

    check_if_auction_open()

    print("Ok well let's get the owner to sell!")

    sell_nft(accounts[0], 10, 0.001)

    print("Lets check if the auction is open again!\n")

    check_if_auction_open()

    end_time = get_end_time()

    while time.time() < end_time:
        continue

    find_winner(accounts[0])

    print("Ok Let's revert the DOGGO NFT Back to the Owner\n")

    revert_to_owner(accounts[0])


def main():
    run_no_bidder_auction()
