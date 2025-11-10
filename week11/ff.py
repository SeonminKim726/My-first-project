import random

# -----------------------------
# 함수: 파일에서 몬스터 정보 읽기
# -----------------------------
def load_monsters(filename):
    monsters = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                name, hp, attack = line.strip().split(',')
                monsters.append({'name': name, 'hp': int(hp), 'attack': int(attack)})
    except FileNotFoundError:
        # 기본 몬스터 데이터
        monsters = [
            {'name': 'Slime', 'hp': 10, 'attack': 2},
            {'name': 'Goblin', 'hp': 15, 'attack': 4},
            {'name': 'Orc', 'hp': 20, 'attack': 5}
        ]
    return monsters

# -----------------------------
# 클래스: 플레이어
# -----------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 30
        self.attack_power = 5
        self.inventory = []  # collection example

    # 공격
    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    # 아이템 사용
    def heal(self):
        if 'Potion' in self.inventory:
            self.hp += 10
            self.inventory.remove('Potion')
            print(f"{self.name} used a Potion! +10 HP")
        else:
            print("No potions left!")

# -----------------------------
# 클래스: 몬스터
# -----------------------------
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack_power = attack

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.hp -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")

# -----------------------------
# 메인 RPG 게임
# -----------------------------
def main():
    print("=== Welcome to Mini RPG ===")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    monsters_data = load_monsters('monsters.txt')
    monsters = [Monster(m['name'], m['hp'], m['attack']) for m in monsters_data]

    for monster in monsters:
        print(f"\nA wild {monster.name} appeared! HP: {monster.hp}")
        while monster.hp > 0 and player.hp > 0:
            print(f"\nPlayer HP: {player.hp}")
            action = input("Choose action (attack/heal/run): ").lower()
            
            if action == 'attack':
                player.attack(monster)
            elif action == 'heal':
                player.heal()
            elif action == 'run':
                print(f"{player.name} ran away!")
                break
            else:
                print("Invalid action.")
                continue

            if monster.hp > 0:
                monster.attack(player)

        if player.hp <= 0:
            print("You were defeated! Game Over.")
            return

    print(f"\nCongratulations {player.name}! You defeated all monsters!")

# -----------------------------
# 실행
# -----------------------------
if __name__ == "__main__":
    main()
