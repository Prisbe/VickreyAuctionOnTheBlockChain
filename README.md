Cryptocurrencies, NFTs, and Blockchain technologies seem like the hottest topic online right now. For my final project, I want to dive into how the Ethereum blockchain works and how NFTs are bought and sold on the Ethereum blockchain. I know at the current moment that most NFTs are sold via rising price auctions or at a fixed price. I want to implement a way of selling an NFT via a sealed bid second price auction (Vickrey Auction). I was inspired to do this because of the paper by Honglei Li and Weilian Xue called “A Blockchain-Based Sealed-Bid e-Auction Scheme with Smart Contract and Zero-Knowledge Proof.” NFTs are sold via smart contract interactions. A smart contract is an agreement, contract, or set of instructions that is deployed on a decentralized blockchain. These smart contracts are immutable, self-executing, and open for everyone on the blockchain to see. When it comes to selling an NFT, the smart contract is in charge of the sale and of the transfer of ownership. This way, the buyer doesn’t have to trust that the seller will change ownership to the buyer, the transfer of ownership is guaranteed by the smart contract. This is why smart contracts are called trustless because we eliminate having to trust a centralized entity. 
	My goal of the project is as follows: create an NFT, create a smart contract that controls the buying and selling of that NFT, and then simulate a Vickrey auction. The selling of the NFT will only be done via Vickrey auction. The programming languages that I am going to use are Solidity and Python. Solidity is an object-oriented programming language used for creating smart contracts on the Ethereum blockchain. I will use python for compiling the solidity code, deploying the smart contract to the blockchain, and to interact with contracts on the blockchain. The python framework used to do all the above is called brownie and is built off of tools from web3.py. I will be using two different Ethereum test networks, the first being a local network called Ganache. Ganache spins up a fake Ethereum blockchain filled with users with ETH. Ganache is used for developing and allows me to quickly run tests, execute commands, and inspect state while controlling how the chain operates. I will also be using the Rinkeby testnet, which is a fork of the main Ethereum network. I am using Rinkeby just to show how contract creation, deployment, and interaction would look like on the real Ethereum network. 

Project Stages: 
-	Create Solidity Smart Contract for Sealed Bid Auction 
o	Could be tested on Remix IDE (Removes Python Part) 
-	Create NFT and link to Smart Contract 
-	Deploy Smart Contract with Python 
o	Demonstrate Transactions on Ganache 
o	Demonstrate Transactions on Rinkeby 
-	Simulate Sealed Bid Auction on Ganache 
With this project I will learn more about how the blockchain works, NFT’s, Smart Contracts, and Smart Contract Development. 
