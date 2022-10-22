// const contracts = [
//     `Escrow.sol`
// ]

// module.exports = deployer => contracts.map(contract => deployer.deploy(artifacts.require(contract)))

// var Escrow = artifacts.require("Escrow");
// module.exports = deployer => deployer.deploy(Escrow);


var Exp4 = artifacts.require("Exp4");
module.exports = deployer => deployer.deploy(Exp4, "0xE628A070AC48f83d7061f62Ce0f4304528e3141d", "0x874c7fbdB086F41BA3d2562B42f3b4Aec5307862", "100000000000000000");