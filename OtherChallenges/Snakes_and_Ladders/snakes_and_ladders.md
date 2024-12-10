# Snakes and Ladders

Snakes and Ladders is a classic board game where players navigate a series of numbered squares, starting at square 1 and aiming to reach the final square. Along the way, players may encounter ladders, which boost them forward, or snakes, which send them backward. Players progress by rolling a dice and moving the resulting number of squares.

## Problem Statement

You are tasked with simulating a game of Snakes and Ladders on a game board. The game is played as follows:

1. The board consists of consecutively numbered squares from `1` to `n`.
2. The player starts at square `1` and aims to reach the last square, `n`.
3. On each turn, the player rolls a dice (with values from `1` to `6`) and moves forward by the dice's value.
4. If the player lands on the start of a ladder, they immediately move to the ladder's endpoint.
5. If the player lands on the start of a snake, they immediately move to the snake's endpoint.
6. The game continues until the player reaches or exceeds square `n`.

Your task is to simulate the game and output the details of each round, including the player's initial position, dice roll, any artifacts encountered (snakes or ladders), and final position.

### Example

Input:
```python
artifacts = [
    Artifact(3, 11, ArtifactType.LADDER),
    Artifact(6, 17, ArtifactType.LADDER),
    Artifact(14, 4, ArtifactType.SNAKE),
    Artifact(22, 20, ArtifactType.SNAKE),
]
game = GameBoard(squares=25)
game.set_artifacts(artifacts=artifacts)
game.play()
```

Output:
```bash
Round 1:
********************
Initial pos: 1
Dice Roll: 6
Final pos: 7
********************

Round 2:
********************
Initial pos: 7
Dice Roll: 5
Final pos: 12
********************

Artifact: snake
********************
Initial pos: 14
Dice Roll: 0
Final pos: 4
********************

...

Total rounds: X
```

## Explanation

The game is played on a board with 25 squares, and the following artifacts are placed:

- A ladder from square 3 to 11
- A ladder from square 6 to 17
- A snake from square 14 to 4
- A snake from square 22 to 20

The player rolls the dice, progresses across the board, and interacts with artifacts (snakes or ladders) as described.

## Constraints

- **5** `≤` **n** `≤` **100**: The board has at least `5` squares and at most `100` squares.

- Artifacts are represented as pairs of integers (`start`, `end`) where:
    - **1** `≤` **start** `<` **end**: For ladders.
    - **1** `≤` **end** `<` **start**: For snakes.
- The dice rolls are integers between `1` and `6`.

## Function Signature

Implement the following methods in the game simulation:

```python
def roll_dice(self) -> int:
    # Simulate a dice roll

def set_artifacts(self, artifacts: List[Artifact]) -> None:
    # Place the artifacts on the board

def simulate(self) -> List[Round]:
    # Simulate the game and return a list of rounds

def play(self) -> None:
    # Run the game simulation and print each round's details
```

## Solution

Proposed solution can be found [here](/OtherChallenges/Snakes_and_Ladders/snakes_and_ladders.py)
