from typing import Any, List, Tuple, Optional
import random
from dataclasses import dataclass
from enum import Enum


class ArtifactType(Enum):
    LADDER = 'ladder'
    SNAKE = 'snake'


@dataclass
class Artifact:
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
    initial_position: int
    final_position: int
    dice: int
    artifact: Optional[ArtifactType]

    def __init__(self, initial_position: int, final_position: int, dice: int, artifact: Optional[ArtifactType] = None):
        """Represent a single round in the game."""
        self.initial_position = initial_position
        self.final_position = final_position
        self.dice = dice
        self.artifact = artifact


class GameBoard:
    artifacts: List[Artifact]
    current_position: int
    last_square: int

    def __init__(self, squares: int = 25):
        """Initialize the game board."""
        self.squares = {x: None for x in range(squares)}
        self.last_square = squares
        self.current_position = 1
        self.game: List[Round] = []

    def set_artifacts(self, artifacts: List[Artifact]) -> None:
        """Place artifacts (snakes or ladders) on the board."""
        for artifact in artifacts:
            self.squares[artifact.start] = artifact

    def set_round(self, initial: int, final: int, dice: int, artifact: Optional[str] = None) -> Round:
        """Record a single round in the game."""
        r = Round(
            initial_position=initial,
            final_position=final,
            dice=dice,
            artifact=artifact
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
                artifact=None
            )

            if final_position >= self.last_square:
                break

            if self.squares[final_position] is not None:
                artifact = self.squares[final_position]
                self.set_round(
                    initial=final_position,
                    final=artifact.end,
                    dice=0,
                    artifact=artifact.type.value
                )
                final_position = artifact.end

            self.current_position = final_position

        return self.game

    def play(self) -> None:
        """Play the game and display the results."""
        simulated_game = self.simulate()
        round_counter = 0

        for r in simulated_game:
            if r.initial_position <= self.last_square:
                if r.artifact is None:
                    round_counter += 1
                    print(f'Round {round_counter}:')
                else:
                    print(f"Artifact: {r.artifact}")
                print("*" * 20)
                print(f"Initial pos: {r.initial_position}")
                print(f"Dice Roll: {r.dice}")
                print(f"Final pos: {r.final_position}")
                print("*" * 20)
                print("\n")

        print(f"Total rounds: {round_counter}")

    @classmethod
    def roll_dice(cls) -> int:
        """Simulate a dice roll."""
        return random.randint(1, 6)


if __name__ == "__main__":
    artifacts = [
        Artifact(3, 11, ArtifactType.LADDER),
        Artifact(6, 17, ArtifactType.LADDER),
        Artifact(14, 4, ArtifactType.SNAKE),
        Artifact(22, 20, ArtifactType.SNAKE),
    ]

    game = GameBoard()
    game.set_artifacts(artifacts=artifacts)
    game.play()
