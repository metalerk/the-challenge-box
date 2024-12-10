# Snakes and ladders

from typing import Any, List, Tuple

import random

from dataclasses import dataclass
from enum import Enum
from pprint import pprint as pprint


class ArtifactType(Enum):
    LADDER = 'ladder'
    SNAKE = 'snake'

@dataclass
class Artifact:
    start: int
    end: int
    type: str | None

    def __init__(self, start: int, end: int, type: str|None) -> None:
        self.start = start
        self.end = end
        self.type = type


@dataclass
class Round:
    initial_position: int
    final_position: int
    dice: int
    artifact: ArtifactType | None


class GameBoard:
    artifacts: List[Artifact]
    current_position: int
    last_square: int

    def __init__(self, squares=25):
        self.squares = {x: None for x in range(squares)}
        self.last_square = squares
        self.current_position = 1
        self.game = []

    def set_artifacts(self, artifacts: List[Artifact]):
        for artifact in artifacts:
            self.squares[artifact.start] = artifact
    
    def set_round(self, initial, final, dice, artifact=None):
        r = Round(
                initial_position=initial,
                final_position=final,
                dice=dice,
                artifact=artifact
            )
        self.game.append(r)
        return r
    
    def simulate(self):
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
                self.set_round(
                    initial=final_position,
                    final=self.squares[final_position].end,
                    dice=0,
                    artifact=self.squares[final_position].type.value
                )
                final_position = self.squares[final_position].end

            self.current_position = final_position
        
        return self.game
    
    def play(self):
        simulated_game = self.simulate()
        round_counter = 0

        for r in simulated_game:
            if r.initial_position <= 25:
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
    def roll_dice(self):
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
