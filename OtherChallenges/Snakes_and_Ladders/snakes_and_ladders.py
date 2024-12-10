#!/bin/python3
"""
Snakes and Ladders Problem Solution
---------------------------------------

Snakes and Ladders is a classic board game where players navigate a series
of numbered squares, starting at square 1 and aiming to reach the final square.
Along the way, players may encounter ladders, which boost them forward, or snakes,
which send them backward. Players progress by rolling a dice and moving the
resulting number of squares.

1. The board consists of consecutively numbered squares from 1 to n.
2. The player starts at square 1 and aims to reach the last square, n.
3. On each turn, the player rolls a dice (with values from 1 to 6) and moves forward by the dice's value.
4. If the player lands on the start of a ladder, they immediately move to the ladder's endpoint.
5. If the player lands on the start of a snake, they immediately move to the snake's endpoint.
6. The game continues until the player reaches or exceeds square n.

The task is to simulate the game and output the details of each round,
including the player's initial position, dice roll, any artifacts
encountered (snakes or ladders), and final position.

Author: Luis Esteban Rodriguez
Email: rodriguezjluis0@gmail.com
Github: https://github.com/metalerk
"""

from typing import List, Optional

import copy
import random
import unittest

from dataclasses import dataclass
from enum import Enum
import unittest.mock


class ArtifactType(Enum):
    """Represents Artifact types."""

    LADDER = "ladder"
    SNAKE = "snake"


@dataclass
class Artifact:
    """Represents an artifact. (Snake or Ladder)"""

    start: int
    end: int
    type: Optional[str]

    def __init__(self, start: int, end: int, type: Optional[str]) -> None:
        """Initialize an artifact representing a snake or ladder."""
        self.start = start
        self.end = end
        self.type = type


@dataclass
class Round:
    """Represents a game round."""

    initial_position: int
    final_position: int
    dice: int
    artifact: Optional[ArtifactType]

    def __init__(
        self,
        initial_position: int,
        final_position: int,
        dice: int,
        artifact: Optional[ArtifactType] = None,
    ):
        """Represent a single round in the game."""
        self.initial_position = initial_position
        self.final_position = final_position
        self.dice = dice
        self.artifact = artifact


class GameBoard:
    """Represents a Game board."""

    artifacts: List[Artifact]
    current_position: int
    last_square: int

    def __init__(self, squares: int = 25):
        """Initialize the game board."""
        if squares < 5 or squares > 100:
            raise Exception(
                f"Invalid parameter squares[{squares}]: Value must be within 5 to 100 range."
            )
        self.squares = {x: None for x in range(squares)}
        self.last_square = squares
        self.current_position = 1
        self.game: List[Round] = []

    def set_artifacts(self, artifacts: List[Artifact]) -> None:
        """Place artifacts (snakes or ladders) on the board."""
        for artifact in artifacts:
            self.squares[artifact.start] = artifact

    def set_round(
        self, initial: int, final: int, dice: int, artifact: Optional[str] = None
    ) -> Round:
        """Record a single round in the game."""
        r = Round(
            initial_position=initial, final_position=final, dice=dice, artifact=artifact
        )
        self.game.append(r)
        return r

    def simulate(self) -> List[Round]:
        """Simulate the entire game and record rounds."""
        while True:
            dice = self.roll_dice()
            final_position = self.current_position + dice
            self.set_round(
                initial=self.current_position,
                final=final_position,
                dice=dice,
                artifact=None,
            )

            if final_position >= self.last_square:
                break

            if self.squares[final_position] is not None:
                artifact = self.squares[final_position]
                self.set_round(
                    initial=final_position,
                    final=artifact.end,
                    dice=0,
                    artifact=artifact.type.value,
                )
                final_position = artifact.end

            self.current_position = final_position

        return self.game

    def play(self, verbose=True) -> None:
        """Play the game and display the results."""
        simulated_game = self.simulate()
        round_counter = 0

        for r in simulated_game:
            if r.initial_position <= self.last_square:
                if r.artifact is None:
                    round_counter += 1
                    if verbose:
                        print(f"Round {round_counter}:")
                else:
                    if verbose:
                        print(f"Artifact: {r.artifact}")
                if verbose:
                    print("*" * 20)
                    print(f"Initial pos: {r.initial_position}")
                    print(f"Dice Roll: {r.dice}")
                    print(f"Final pos: {r.final_position}")
                    print("*" * 20)
                    print("\n")

        if verbose:
            print(f"Total rounds: {round_counter}")

        return simulated_game, round_counter

    @classmethod
    def roll_dice(cls) -> int:
        """Simulate a dice roll."""
        return random.randint(1, 6)


# test cases
class SnakesAndLaddersTestCase(unittest.TestCase):
    """Handles game test cases."""

    def setUp(self):
        """Initialize test case class variables."""
        self.artifacts = [
            Artifact(3, 6, ArtifactType.LADDER),
            Artifact(9, 5, ArtifactType.SNAKE),
        ]
        self.game = GameBoard(squares=10)
        self.game.set_artifacts(artifacts=self.artifacts)
        return super().setUp()

    @unittest.mock.patch(f"{GameBoard.__module__}.GameBoard.simulate")
    def test_artifacts_correct(self, mock_simulate):
        """Test artifacts behave as expected."""
        # set simulateed rounds
        simulated_rounds = [
            Round(initial_position=0, final_position=3, dice=3, artifact=None),
            Round(
                initial_position=3,
                final_position=6,
                dice=0,
                artifact=ArtifactType.LADDER.value,
            ),
            Round(initial_position=6, final_position=9, dice=3, artifact=None),
            Round(
                initial_position=9,
                final_position=5,
                dice=0,
                artifact=ArtifactType.SNAKE.value,
            ),
            Round(initial_position=5, final_position=11, dice=6, artifact=None),
        ]

        # makes sure it is a deep copy. copy.deepcopy creates a new list and recursively
        # copies the items from the original list.
        mock_simulate.return_value = copy.deepcopy(simulated_rounds)

        # omits verbove output
        rounds, total = self.game.play(verbose=False)

        # assert expected values match the mocked simulated rounds return value
        self.assertEqual(rounds, simulated_rounds)
        self.assertEqual(total, 3)

        simulated_rounds = [
            Round(initial_position=0, final_position=3, dice=3, artifact=None),
            Round(
                initial_position=3,
                final_position=6,
                dice=0,
                artifact=ArtifactType.LADDER.value,
            ),
            Round(initial_position=6, final_position=10, dice=4, artifact=None),
        ]

        mock_simulate.return_value = copy.deepcopy(simulated_rounds)
        rounds, total = self.game.play(verbose=False)

        # again, assert expected values match the mocked simulated rounds return value
        self.assertEqual(rounds, simulated_rounds)
        self.assertEqual(total, 2)

    def test_gameboard_squares_boundaries(self):
        """Test gameboard squares boundaries."""
        # within
        self.game = GameBoard(squares=5)
        self.game = GameBoard(squares=100)

        # without
        with self.assertRaises(Exception):
            self.game = GameBoard(squares=1)
        with self.assertRaises(Exception):
            self.game = GameBoard(squares=101)


def main():
    """main function."""
    unittest.main()


if __name__ == "__main__":
    main()
