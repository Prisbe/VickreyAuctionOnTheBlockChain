// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6;

contract Sealed_Bid_Auction {
    address public owner;
    string public DOGGO_NFT =
        "https://drive.google.com/file/d/1ULKxa4PFUAg0Q7NsyfErE3p6_669Kf5u/view?usp=sharing";
    bool public auction_open = false;
    uint256 public auction_end_time = 0;

    address[] public bidderAddresses;
    mapping(address => uint256) public addressToAmountBidded;

    address public pendingWinner;
    uint256 public pendingPaymentAmnt = 0;

    constructor() public {
        owner = msg.sender;
    }

    function get_owner() public view returns (address) {
        return owner;
    }

    function get_nft() public view returns (string memory) {
        return DOGGO_NFT;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _; // The sell_nft() function will run after checking that the owner called the function
    }

    function sell_nft(uint256 _auction_time)
        public
        onlyOwner
        returns (uint256)
    {
        auction_open = true;
        auction_end_time = block.timestamp + _auction_time;
        return auction_end_time;
    }

    function check_if_auction_open() public view returns (bool, uint256) {
        return (auction_open, auction_end_time);
    }

    function check_if_bidded_before() internal view returns (bool) {
        for (uint256 i = 0; i < bidderAddresses.length; i++)
            if (msg.sender == bidderAddresses[i]) return true;

        return false;
    }

    modifier auction_open_check_bidder() {
        require(auction_open == true);
        require(check_if_bidded_before() == false); //They Have Not Already Submitted A Bid
        _;
    }

    function submit_bid(uint256 _ethAmount) public auction_open_check_bidder {
        bidderAddresses.push(msg.sender);
        addressToAmountBidded[msg.sender] = _ethAmount;
    }

    function find_winner_and_price() internal {
        uint256 highestBid = 0;
        address highestBidder;
        uint256 secondHighest = 0;

        for (uint256 i = 0; i < bidderAddresses.length; i++) {
            if (addressToAmountBidded[bidderAddresses[i]] > highestBid) {
                highestBid = addressToAmountBidded[bidderAddresses[i]];
                highestBidder = bidderAddresses[i];
            }
        }

        for (uint256 i = 0; i < bidderAddresses.length; i++) {
            if (highestBidder == bidderAddresses[i]) continue;
            else if (addressToAmountBidded[bidderAddresses[i]] > secondHighest)
                secondHighest = addressToAmountBidded[bidderAddresses[i]];
        }

        pendingWinner = highestBidder;
        pendingPaymentAmnt = secondHighest;
    }

    modifier auction_ended() {
        require(block.timestamp > auction_end_time);
        require(auction_open == true);
        _;
    }

    function get_auction_results() public auction_ended {
        auction_open = false;
        auction_end_time = 0;
        find_winner_and_price();
    }

    modifier only_winner() {
        require(msg.sender == pendingWinner);
        require(msg.value == pendingPaymentAmnt);
        _;
    }

    function transfer_ownership() public payable only_winner {
        payable(owner).transfer(address(this).balance);
        owner = msg.sender;

        //Need To Reset the Dictionary and Array of bidders
        for (uint256 i = 0; i < bidderAddresses.length; i++)
            addressToAmountBidded[bidderAddresses[i]] = 0; //Reset the Dictionary
        bidderAddresses = new address[](0); //Reset the array of Bidders

        pendingWinner = address(0);
        pendingPaymentAmnt = 0;
    }
}