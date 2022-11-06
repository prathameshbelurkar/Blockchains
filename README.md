<h1 align="center">Blockchains 🔗</h1>

<br>

<p align="center">
<img src="https://images.unsplash.com/photo-1639322537504-6427a16b0a28?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1032&q=80" width=500 />
</p>

<br>

A blockchain is a distributed database or ledger that is shared among the nodes of a computer network. As a database, a blockchain stores information electronically in digital format. Blockchains are best known for their crucial role in cryptocurrency systems, such as Bitcoin, for maintaining a secure and decentralized record of transactions. The innovation with a blockchain is that it guarantees the fidelity and security of a record of data and generates trust without the need for a trusted third party.

One key difference between a typical database and a blockchain is how the data is structured. A blockchain collects information together in groups, known as blocks, that hold sets of information. Blocks have certain storage capacities and, when filled, are closed and linked to the previously filled block, forming a chain of data known as the blockchain. All new information that follows that freshly added block is compiled into a newly formed block that will then also be added to the chain once filled.

A database usually structures its data into tables, whereas a blockchain, as its name implies, structures its data into chunks (blocks) that are strung together. This data structure inherently makes an irreversible timeline of data when implemented in a decentralized nature. When a block is filled, it is set in stone and becomes a part of this timeline. Each block in the chain is given an exact timestamp when it is added to the chain.

<br>

<p align="center">
<img src="https://uploads-ssl.webflow.com/5d2dd7e1b4a76d8b803ac1aa/5e81c66dd4cabdcc1674a08d_0nt8_YaCOJ_ED51A163rrtjq4mA4Qp1MsIXdDUR4iUAVBYYM5thrRmXCJsZHNa95-yQ3poZep9S8hkUffFkdqbIt9EXmk0bUbLfV0TJWOTH2dwUp6sSsCtnPx8esAE_DROgkKAAT.png" alt="img of blockchain" width=600 />
</p>

<br>

**Points to summarize**

1. Blockchain is a type of shared database that differs from a typical database in the way that it stores information; blockchains store data in blocks that are then linked together via cryptography.

2. As new data comes in, it is entered into a fresh block. Once the block is filled with data, it is chained onto the previous block, which makes the data chained together in chronological order.

3. Different types of information can be stored on a blockchain, but the most common use so far has been as a ledger for transactions.

4. In Bitcoin’s case, blockchain is used in a decentralized way so that no single person or group has control—rather, all users collectively retain control.

5. Decentralized blockchains are immutable, which means that the data entered is irreversible. For Bitcoin, this means that transactions are permanently recorded and viewable to anyone.

<br>

**Working:**
_*The goal of blockchain is to allow digital information to be recorded and distributed, but not edited. In this way, a blockchain is the foundation for immutable ledgers, or records of transactions that cannot be altered, deleted, or destroyed. This is why blockchains are also known as a distributed ledger technology (DLT).*_

<br>

<hr>

### Distributed Ledgers

Distributed ledger technology (DLT) could fundamentally change the financial sector, making it more efficient, resilient and reliable.

- This could address persistent challenges in the financial sector and change roles of financial sector stakeholders. DLT has the potential to transform various other sectors as well, like manufacturing, government financial management systems and clean energy.

- Since this technology is still nascent, the World Bank Group doesn’t have general recommendations about its use for international development. We are in dialogue with standard-setting bodies, governments, central banks and other stakeholders to monitor, research and pilot applications based on blockchain and DLT.

- However, waiting for “perfect” DLT solutions could mean missing an opportunity to help shape it. To understand how DLT can address challenges in the financial sector requires both research and real-life applications and pilots.

- It also requires resolving consumer protection issues, financial integrity concerns, speed of transactions, environmental footprint, legal, regulatory and technological issues that arise with the advent of new technology.

- DLT applications will likely be incremental, and will likely first replace processes and activities that are still manual and inefficient. (Such as reference data maintenance in payment and settlement systems, trade finance, syndicated loans, and tracking provenance of agricultural products and commodities, their subsequent sale or use as financing collateral.)

- Eventually, DLT could increase efficiency and lower remittance costs, and potentially improve access to finance for unbanked populations, who are currently outside the traditional financial system.

<br>

<hr>

### Distributed P2P Network

<br>

<p align="center">
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--s9zSkG-3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s3nc9o2goloh6ml7xth1.png" width=500>
</p>

<br>

Peer-to-peer (P2P) computing or networking is a distributed application architecture that partitions tasks or workloads between peers. Peers are equally privileged, equipotent participants in the network. They are said to form a peer-to-peer network of nodes.

Peers make a portion of their resources, such as processing power, disk storage or network bandwidth, directly available to other network participants, without the need for central coordination by servers or stable hosts. Peers are both suppliers and consumers of resources, in contrast to the traditional client–server model in which the consumption and supply of resources are divided.

<br>

<hr>

### Mining in Blockchains

<br>

<p align="center">
<img src="https://bitcoinist.com/wp-content/uploads/2018/08/Cryptocurrency-Mining.jpg" width=400 />
</p>

<br>

Bitcoin mining is the process by which new bitcoins are entered into circulation. It is also the way the network confirms new transactions and is a critical component of the blockchain ledger's maintenance and development. "Mining" is performed using sophisticated hardware that solves an extremely complex computational math problem. The first computer to find the solution to the problem receives the next block of bitcoins and the process begins again.

- By mining, you can earn cryptocurrency without having to put down money for it.

- Bitcoin miners receive bitcoin as a reward for completing "blocks" of verified transactions, which are added to the blockchain.

- Mining rewards are paid to the miner who discovers a solution to a complex hashing puzzle first, and the probability that a participant will be the one to discover the solution is related to the portion of the network's total mining power.

- You need either a graphics processing unit (GPU) or an application-specific integrated circuit (ASIC) in order to set up a mining rig.

<br>

<hr>

### Byzantine Fault Tolerance (BFT)

<br>

<p align="center">
<img src="https://www.unitychain.io/blog/wp-content/uploads/2019/07/pre-prepare-phase.jpg" width=500 />
</p>

<br>

Byzantine Fault Tolerance(BFT) is the feature of a distributed network to reach consensus(agreement on the same value) even when some of the nodes in the network fail to respond or respond with incorrect information. The objective of a BFT mechanism is to safeguard against the system failures by employing collective decision making(both – correct and faulty nodes) which aims to reduce to influence of the faulty nodes. BFT is derived from Byzantine Generals’ Problem.

Byzantine fault tolerance can be achieved if the correctly working nodes in the network reach an agreement on their values. There can be a default vote value given to missing messages i.e., we can assume that the message from a particular node is ‘faulty’ if the message is not received within a certain time limit. Furthermore, we can also assign a default response if the majority of nodes respond with a correct value.

Leslie Lamport proved that if we have 3m+1 correctly working processors, a consensus(agreement on same state) can be reached if atmost m processors are faulty which means that strictly more than two-thirds of the total number of processors should be honest.

<br>

**Types of Byzantine Failures:**

There are two categories of failures that are considered. One is fail-stop(in which the node fails and stops operating) and other is arbitrary-node failure. Some of the arbitrary node failures are given below :

- Failure to return a result
- Respond with an incorrect result
- Respond with a deliberately misleading result
- Respond with a different result to different parts of the system

<br>

<hr>

### Consensus Protocols

<br>

<p align="center">
<img src="https://www.churchleadership.com/wp-content/uploads/2021/06/art-forging-meaningful-consensus.png" width=500 />
</p>

<br>

The Blockchain consensus protocol consists of some specific objectives such as coming to an agreement, collaboration, co-operation, equal rights to every node, and mandatory participation of each node in the consensus process. Thus, a consensus algorithm aims at finding a common agreement that is a win for the entire network. Now, we will discuss various consensus algorithms and how they work.

 <br>

**1. Proof of Work**

Proof of Work is one of the first consensus protocols used in blockchain applications. It is based on computing the hash values and validating the transactions until a specified number of trailing zeros are found in the hash value. The number that generates the hash with the specified number of trailing zeros is known as a nonce. A nonce is defined as a random number that generates the specified number of trailing zeros in the hash function.

- Proof of Work is designed for permissionless public ledgers and uses the computational resources from the systems in the node to reach consensus.

- The blocks are represented in a linear structure. Each block represents a group of transactions.

- The mining aspect of bitcoins has to do with solving the cryptographic puzzle of finding a random integer, that leads to hashes with a specified number of leading zeros.

- Every transaction is validated and signed using the public and private keys assigned to each user.

<br>

**2. Proof of Stake**

Ethereum was one of the largest cryptocurrencies to decide to move onto proof of stake consensus. Let’s understand this example a bit better. Let’s say we are miners and are validating the transactions made. In bitcoin, a person validates the transactions by computing the hash value with a certain number of leading zeros gets the allocated amount of bitcoins.

In proof of stake consensus, a validator is picked and assigned a block. The miner has to allocate a particular part of his cryptocurrency to start validating. If the miner succeeds in invalidating the transaction, then the award is the stake they had pledged initially, along with certain transaction fees. This is a way to penalize bad behavior and incentivize good behavior.

- The validators are picked according to their economic stake in the network.

- The objective is to avoid centralization of mining centers and provide a chance to validate to all the miners.

- It is environmentally friendly as there is no computational puzzle to be solved.

- Special hardware for mining is not required.

<br>

**3. Proof of Space**

Proof of Space, also known as PoSpace, is a network consensus protocol similar to the Proof of Work consensus protocol. Instead of the computational resources, PoSpace uses disk storage to validate transactions.

PoSpace consumes disk space and incentivizes miners with the most considerable disk space allocated to a block. Implemented using the hard-to-pebble graphs, this data structure is used to solve the pebbling game. The pebbling game consists of pebbling vertices in a graph only if all the parent vertices have been pebbled.

Pebbling refers to storing the parents’ hash values, and removing the pebble refers to freeing the memory. Refer to this article for more details on the pebbling game.

All the feasible solutions to the problem are generated randomly, called plots. These plots are stored on the disks and solved using an algorithm called Shabal’s algorithm. Once the solutions are computed, the miners compare their solutions, and the solution with the best time and space complexity is rewarded with the next block.

<br>

**4. Proof of Elapsed TIme**

Proof of Elapsed time is a network consensus protocol developed by the Intel Corporation. The algorithm is predominantly used in permissioned blockchain ledgers. The hardware used in PoET is specially designed for this protocol. For example, Intel Software Guarded Extension (SGX) is used in networks using PoET.

This consensus protocol is used to allocate blocks to miners on the network. In permissioned blockchain systems, the miners’ identity is determined before allowing access into the network. Therefore, anonymity is not a feature in this protocol.

Each node in the network is assigned a random waiting time. The first node to complete the randomly chosen period validates the new block. The specialized hardware puts the processor to sleep during the wait time—this repeats over all the blocks in the network.
