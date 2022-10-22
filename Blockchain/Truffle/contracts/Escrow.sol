// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

contract Escrow{
    uint256 amount;
    address payee;     // person who is recieving the amount
    address payer;     // person who is paying the amount
    address thirdparty;

    constructor(){
        thirdparty = msg.sender;  
    }

    function setPayee (address _payee) public thirdPartyOnly {
        payee = _payee;
    }
    function setPayer (address _payer) public thirdPartyOnly {
        payer =_payer;
    }
    function setAmount (uint256 _amount) public thirdPartyOnly{
        amount = _amount;
    }
    function returnAllParameters() public view returns(uint256, address, address, address){
        return (amount, payee, payer, thirdparty);
    }

    modifier thirdPartyOnly {
        require(thirdparty == msg.sender, "Only Third Party is authorized to access this method!!!");
        _;
    }
    modifier minimumWithdrawalAmount {
        require(address(this).balance >= amount, "Cannot release funds before full amount is sent");
        _;
    }

    function deposit() public payable {
        require(payer == msg.sender, "Sender must be the payer");
        // require(msg.value + contractBalance() >= amount, "Amount exceeding!!!");
    }

    function contractBalance() public view returns(uint256){
        return address(this).balance;
    }

    function release() public thirdPartyOnly minimumWithdrawalAmount returns(uint256){
        (bool callSuccess, ) = payable(payee).call{value: address(this).balance}("");
        require(callSuccess, "Call failed");

        return contractBalance();
    }


}