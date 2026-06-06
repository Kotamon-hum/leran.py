#ここはmain。よく使う短いコマンドを保存しておく場所でありハブ。ちゃんとした一貫したコードは別に付属させていく

#print構文(文字を出力できる)
print("Hello World!")

name = input("あなたの名前は？")
print(name+"さん、こんにちは。")

#input構文(ユーザーの入力を受け取る。又は競技プログラミングでは入力を**文字列**で受け取る)
name = input("あなたの名前は？")

num = int(input("数字を入力してください"))

int = int(input().split)

int = list(map(int, input().split()))

#for構文(指定した回数下に付属する行為を繰り返す)
for i in range(9):
 print ("piyo")
  
num = int(input("感謝の数字をいれてください"))
for i in range(num):
 print("ty")

#if構文(ifで条件分岐する)
while True:
 num = int(input())
 if num == 0:
  print("これはゼロです")
  break
 elif num == 1:
  print("これはイチです")
  break
 elif num == 2:
  print("これはニです")
  break
 else:
  print("もう一度入力してください")
  continue
