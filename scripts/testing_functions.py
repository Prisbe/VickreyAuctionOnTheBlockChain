from brownie import Sealed_Bid_Auction
from scripts.helpful_scripts import get_account
import datetime


def getOwner():
    sealed_bid_auction = Sealed_Bid_Auction[
        -1
    ]  # Gets the most recently created contract or we can use 0
    account = get_account()
    owner = sealed_bid_auction.get_owner()
    print(f"The owner of the DOGGO_NFT is {owner}")


def getNFT():
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    nft_url = sealed_bid_auction.get_nft()
    print(f"URL of NFT: {nft_url}")


def check_if_auction_open():
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    open, time = sealed_bid_auction.check_if_auction_open()
    if open:
        print(
            f"The auction is open and will end at {datetime.datetime.fromtimestamp(time)}\n"
        )
    else:
        print("The auction is not open\n")


def sell_nft():
    account = get_account()
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    sealed_bid_auction.sell_nft(100, {"from": account})


def main():
    getOwner()
    getNFT()
    sell_nft()
    check_if_auction_open()
