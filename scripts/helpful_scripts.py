from brownie import network, config, accounts, Sealed_Bid_Auction
from web3 import Web3
import datetime

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def getOwner():
    sealed_bid_auction = Sealed_Bid_Auction[
        -1
    ]  # Gets the most recently created contract or we can use 0
    account = get_account()
    owner = sealed_bid_auction.get_owner()
    print(f"The owner of the DOGGO_NFT is {owner}\n")


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


def get_end_time():
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    open, time = sealed_bid_auction.check_if_auction_open()
    return time


def sell_nft(ownerAddress, timeOfAuction):
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    sealed_bid_auction.sell_nft(timeOfAuction, {"from": ownerAddress})
    print(
        f"The owner at address: {ownerAddress} has initiated an auction of length {timeOfAuction} in seconds\n"
    )


def submit_bid(address, bidAmount):
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    sealed_bid_auction.submit_bid(bidAmount, {"from": address})
    print(
        f"Address {address} has submitted a bid of {Web3.fromWei(bidAmount, 'ether')} ETH\n"
    )


def find_winner(address):
    sealed_bid_auction = Sealed_Bid_Auction[-1]
    sealed_bid_auction.get_auction_results({"from": address})
    pendingwinner, pendingpayment = sealed_bid_auction.get_pendingWinner_and_price()
    print(f"Address {address} has initiated the results\n")
    print(
        f"The winner is account {pendingwinner} and they need to pay the {pendingpayment} ETH\n"
    )
