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

### Consensus Protocol
