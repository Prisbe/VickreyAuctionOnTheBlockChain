from brownie import Sealed_Bid_Auction, network, config
from scripts.helpful_scripts import get_account


def deploy_sealed_bid_auction_contract():
    account = get_account()
    print(f"Current account is: {account.address}")
    sealed_bid_auction = Sealed_Bid_Auction.deploy({"from": account})
    print(f"Deployed Contract to {sealed_bid_auction.address}")
    return sealed_bid_auction


def main():
    deploy_sealed_bid_auction_contract()
