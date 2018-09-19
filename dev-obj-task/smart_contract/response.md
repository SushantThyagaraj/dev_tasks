# Response
## General Explanation of `smart_contract.sol`
*[YOUR RESPONSE HERE]*
This is an example of betting on a coin flip using Ethereum smart contract, specifically with only two players. First, player1 makes his commitment to a value and makes a bet by initiating the contract. In this contract, the player's name is stored as well as his boolean value, which is in the commitment variable after being hashed. This value cannot be changed once the bet has been accepted. The bet amount is also stored in this contract. If the other player, player2, has yet to take player1's bet offer, player1 can cancel the bet. If the bet is cancelled, the money is returned to the player1. If player2 takes the bet, he accepts the bet amount and makes his prediction for the coin flip. If the bet goes through, the first player has 24 hours to reveal the flip of the coin. However, if player1 chooses not to reveal the flip within 24 hours, the bet is nullified, and player2 can receive the value of the bet. Finally, once player1 reveals the flip (within 24 hours), if player 2 predicted the correct choice, he gets the entire value of the bet; otherwise, all the money in the contract goes to player 1.

## How is the Smart Contract Secured?
1. By having an expiration time of 24 hours for the contract, the smart contract prevents player1 from refusing to reveal his secret and lose the game. Therefore, if the bet exceeds 24 hours, player1 will forfeit the money he put into the bet, which player2 can claim.
2. Once the player2 has accepted the bet, the contract can no longer be voided or manipulated, which prevents player1 from taking advantage of the game.
3. Since there are only two outcomes in the game, if the choices were hashed by themselves, it would be fairly easy to guess the value that was hashed. This would allow player2 to access player1's commitment beforehand and rig the game. To address this, a nonce is added during hashing in order to effectively eliminate this from happening.

## Etherscan Link to Deploy Smart Contract
https://ropsten.etherscan.io/tx/0x49d0be132acbd265a2bf37c25d349164a430558359fee827cabe4adafe6e5d4d
