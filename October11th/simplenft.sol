// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SimpleNFT is ERC721, Ownable {
    uint256 public tokenCounter;

    constructor() ERC721("SimpleNFT", "SNFT") {
        tokenCounter = 0;
    }

    function mintNFT(address recipient) public onlyOwner {
        _safeMint(recipient, tokenCounter);
        tokenCounter++;
    }
}
