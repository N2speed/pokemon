import random

class Pokemon:
    def __init__(self, name, type, hp, attack):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_opponent(self, opponent):
        damage = random.randint(1, self.attack)
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def display_stats(self):
        print(f"{self.name} (Type: {self.type}) - HP: {self.hp}, Attack: {self.attack}")


def main():
    # Create two Pokémon
    pikachu = Pokemon("Pikachu", "Electric", 100, 20)
    charmander = Pokemon("Charmander", "Fire", 90, 18)

    # Display Pokémon stats
    pikachu.display_stats()
    charmander.display_stats()

    # Simulate a battle
    while pikachu.hp > 0 and charmander.hp > 0:
        # Pikachu attacks Charmander
        pikachu.attack_opponent(charmander)
        charmander.display_stats()

        # Check if Charmander fainted
        if charmander.hp <= 0:
            print(f"{charmander.name} fainted! {pikachu.name} wins!")
            break

        # Charmander attacks Pikachu
        charmander.attack_opponent(pikachu)
        pikachu.display_stats()

        # Check if Pikachu fainted
        if pikachu.hp <= 0:
            print(f"{pikachu.name} fainted! {charmander.name} wins!")
            break


if __name__ == "__main__":
    main()
