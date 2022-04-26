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
    time.sleep(2)
    deploy_sealed_bid_auction_contract()
    time.sleep(2)
    getOwner()
    time.sleep(2)
    getNFT()
    time.sleep(2)
    print("Lets check to see if the auction is open!\n")
    time.sleep(2)
    check_if_auction_open()
    time.sleep(2)
    print("Ok well let's get the owner to sell!")
    time.sleep(2)
    sell_nft(accounts[0], 20)
    time.sleep(2)
    print("Lets check if the auction is open again!\n")
    time.sleep(2)
    check_if_auction_open()
    end_time = get_end_time()
    time.sleep(2)
    print("Ok lets submit some bids from bidders!\n")
    time.sleep(2)
    submit_bid(accounts[1], Web3.toWei(0.03, "ether"))
    time.sleep(2)
    submit_bid(accounts[2], Web3.toWei(0.08, "ether"))
    time.sleep(2)
    submit_bid(accounts[3], Web3.toWei(0.12, "ether"))
    time.sleep(2)
    submit_bid(accounts[4], Web3.toWei(0.48, "ether"))
    time.sleep(2)
    submit_bid(accounts[5], Web3.toWei(0.98, "ether"))
    time.sleep(2)
    submit_bid(accounts[6], Web3.toWei(1.15, "ether"))
    time.sleep(2)
    print("Ok Let's wait for the auction to end!\n")
    while time.time() < end_time:
        continue
    print("Let's Figure Out Who the Winner is!")


def main():
    run()
