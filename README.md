# quantum-roulette
A quantum game based on quantum teleportation and the fidelity of quantum gates.


# Goal
The primary goal of this game is to demonstrate how the fidelity of quantum gates can impact quantum circuits, as well as familiarize the players with a few of the basic gates.


# How to Play
Players take turns teleporting a quantum state |ψ⟩, which starts in the |0⟩ state, back and forth between each other. Since quantum gates are not accurate 100% of the time, however, eventually the state will be lost. The first player that fails to send the quantum state loses. While the probability of losing should stay the same, as the previous successful transmissions do not affect the future probability of failure, in the game we pretend as if each successive transmission requires the entire circuit to be run from the beginning. This both reflects the difficulty of creating longer, more complex circuits with current technology and makes the game more interesting.

Additionally, players have the option of performing multiple single-qubit operations on |ψ⟩ during their turn. This increases the chance of losing; however, this also increases that player's score, for a maximum of 5 points every turn. If a player reaches 20 points and then successfully sends the signal, they win the game. This demonstrates how the transmitted signal can be used for calculations by both players, which can be sent back and forth.

Finally, at the start of their turn, players have the option to measure the current state |ψ⟩, collapsing it to |0⟩ or |1⟩. If it collapses to |1⟩, the player wins, and if it collapses to |0⟩, that player loses. Additionally, the other player will know how many gates the player used, as well as one random gate they applied. This encourages players to use multiple gates to increase information entropy and distinguishes between the different gates, making the choice of gates important.
