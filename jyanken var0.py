"""
じゃんけんプログラム（関数化版）
中級者向けに学習用コメントを多めに残しています。
"""

import random
import time
import sys


# 表示用の名前と勝敗判定で使う文字列のマッピング
HAND_MAP = {0: "グー✊", 1: "チョキ✌", 2: "パー✋"}


def to_halfwidth(s: str) -> str:
    """全角数字などが入ることがあるので半角に変換する小さなユーティリティ。

    ord() と translate を使って個別に置換しています。
    もっと一般的には unicodedata.normalize を使う方法もありますが、
    ここでは学習目的で明示的な置換を示します。
    """
    trans = str.maketrans({"０": "0", "１": "1", "２": "2", "３": "3", "４": "4", "５": "5", "６": "6", "７": "7", "８": "8", "９": "9", "Ｙ": "Y", "ｙ": "y", "Ｎ": "N", "ｎ": "n"})
    return s.translate(trans)


def ask_yes_no(prompt: str) -> bool:
    """開始確認の入力を標準化して受け取る関数。

    戻り値: True=開始, False=終了
    受け付ける入力例: y/Y/はい/Yes/yes/全角ｙ など
    """
    while True:
        ans = to_halfwidth(input(prompt).strip())
        # 小文字化して判定
        lower = ans.lower()
        if lower in ("y", "yes", "はい"):
            return True
        if lower in ("n", "no", "いいえ"):
            return False
        print("無効な入力です。y または n を入力してください（例: y, n, はい, いいえ）。")


def get_player_hand(player_name: str) -> int:
    """プレイヤーからの手を取得する関数。

    ユーザに0/1/2で入力してもらい、全角数字や代表的な文字列入力も受け付けます。
    返り値は 0,1,2 の整数。
    """
    while True:
        raw = to_halfwidth(input(f"{player_name}さん: 0=グー, 1=チョキ, 2=パー のいずれかを入力してください: ").strip())
        # 数字入力であればそのまま使う
        if raw in ("0", "1", "2"):
            val = int(raw)
            print(f"{player_name}の入力: {HAND_MAP[val]}")
            time.sleep(0.7)
            return val

        # 単語入力（日本語）を受け付ける場合の例
        lowered = raw.lower()
        if lowered in ("ぐー", "グー"):  # 全角かな/カナをそのまま比較
            print(f"{player_name}の入力: グー✊")
            return 0
        if lowered in ("ちょき", "チョキ"):
            print(f"{player_name}の入力: チョキ✌")
            return 1
        if lowered in ("ぱー", "パー"):
            print(f"{player_name}の入力: パー✋")
            return 2

        print("無効な入力です。0、1、2、または グー/チョキ/パー を入力してください。")


def get_computer_hand() -> int:
    """コンピュータの手をランダムに決定して返す。"""
    return random.randint(0, 2)


def decide_winner(player: int, computer: int) -> str:
    """勝敗判定を行い、'draw'|'player'|'computer' のいずれかを返す。"""
    if player == computer:
        return "draw"
    # 明示的な勝ちペアで判定する方が可読性が高く、誤りが出にくい
    # (winner, loser) の組として定義しています。
    # グー=0, チョキ=1, パー=2 のルールでは
    # グー(0) は チョキ(1) に勝ち、チョキ(1) は パー(2) に勝ち、パー(2) は グー(0) に勝ちます。
    winning_pairs = {(0, 1), (1, 2), (2, 0)}
    if (player, computer) in winning_pairs:
        return "player"
    return "computer"


def main() -> None:
    """プログラムのエントリポイント。会話の流れを制御する。"""
    name = input("こんにちは。名前を教えてください: ").strip()
    if not name:
        name = "プレイヤー"
    print(f"こんにちは、{name}さん!")

    if not ask_yes_no("じゃんけんを始めますか？(y/n): "):
        print("またね！")
        sys.exit(0)

    print("じゃんけんを始めます！")

    # ゲーム本体: 1回勝負（元の実装に合わせて勝敗が決まったら終了）
    while True:
        p = get_player_hand(name)
        c = get_computer_hand()
        print(f"COMの入力: {HAND_MAP[c]}")

        result = decide_winner(p, c)
        if result == "draw":
            print("あいこ！！！")
            # 元の挙動だと「あいこ」の場合は続ける（ループ継続）
            continue
        if result == "computer":
            print("COMの勝ち!!!")
            break
        print(f"{name}さんの勝ち!!!")
        break


if __name__ == "__main__":
    main()
