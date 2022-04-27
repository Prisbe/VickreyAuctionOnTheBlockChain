from distutils.command import check
from brownie import Sealed_Bid_Auction, accounts
from scripts.helpful_scripts import *
from scripts.deploy import deploy_sealed_bid_auction_contract
from web3 import Web3
import time


def run():
    print(
        "Ok Let's Run This Vickrey Auction!\nThe First thing we will do is deploy the contract!\n"
    )

    deploy_sealed_bid_auction_contract()

    getOwner()

    getNFT()

    print("Lets check to see if the auction is open!\n")

    check_if_auction_open()

    print("Ok well let's get the owner to sell!")

    sell_nft(accounts[0], 10)

    print("Lets check if the auction is open again!\n")

    check_if_auction_open()
    end_time = get_end_time()

    print("Ok lets submit some bids from bidders!\n")

    submit_bid(accounts[1], Web3.toWei(0.03, "ether"))

    submit_bid(accounts[2], Web3.toWei(0.08, "ether"))

    submit_bid(accounts[3], Web3.toWei(0.12, "ether"))

    submit_bid(accounts[4], Web3.toWei(0.48, "ether"))

    submit_bid(accounts[5], Web3.toWei(0.98, "ether"))

    submit_bid(accounts[6], Web3.toWei(1.15, "ether"))

    print("Ok Let's wait for the auction to end!\n")
    while time.time() < end_time:
        continue
    print("Let's Figure Out Who the Winner is!\n")

    find_winner(accounts[6])

    print("Ok let's get the winner to pay!\n")
    initiate_transfer(accounts[6], 0.98)

    print("Lets check who the newest owner of the doggo NFT is!")

    getOwner()


def main():
    run()
