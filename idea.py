import random

# 手の対応
hands = {1: "パー", 2: "グー", 3: "チョキ"}

# 勝敗判定
def judge(player, computer):
    # パー(1)はグー(2)に勝ち
    # グー(2)はチョキ(3)に勝ち
    # チョキ(3)はパー(1)に勝ち
    if player == computer:
        return "あいこ"
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"

# メイン処理
print("じゃんけんをしましょう！")
print("1: パー, 2: グー, 3: チョキ")
player = int(input("あなたの手を数字で入力してください: "))
computer = random.randint(1, 3)

print(f"あなた: {hands[player]}")
print(f"コンピュータ: {hands[computer]}")
print(judge(player, computer))
