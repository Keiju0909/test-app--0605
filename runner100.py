import random

# ダミーの日本人風の名前リスト（姓と名の組み合わせ）
last_names = [
    "佐藤", "鈴木", "高橋", "田中", "伊藤", "渡辺", "山本", "中村", "小林", "加藤",
    "吉田", "山田", "佐々木", "山口", "松本", "井上", "木村", "林", "斎藤", "清水",
    "山崎", "阿部", "森", "池田", "橋本"
]
first_names = [
    "大輔", "翔太", "健太", "悠斗", "蓮", "陽斗", "颯太", "大和", "陸", "海斗",
    "優斗", "拓海", "悠真", "陽向", "蒼", "翼", "隼人", "直樹", "翔", "駿",
    "優", "誠", "和也", "亮", "直人"
]

# 選手50人分の名前とタイムを生成
players = []
used_names = set()
while len(players) < 50:
    name = random.choice(last_names) + " " + random.choice(first_names)
    if name in used_names:
        continue
    used_names.add(name)
    time = round(random.uniform(9.56, 12.99), 2)
    players.append({"name": name, "time": time})

# タイムが良い順（昇順）に並び替え
players_sorted = sorted(players, key=lambda x: x["time"])

# 結果表示
print("順位\t名前\t\tタイム(秒)")
for idx, player in enumerate(players_sorted, 1):
    print(f"{idx}\t{player['name']}\t{player['time']}")
