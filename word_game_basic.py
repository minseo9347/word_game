# pip install --upgrade --user pyglet
import pyglet
from pygame import mixer
mixer.init() # 미디어 파일 사용을 위한 초기화
import random
import time

with open("data/word.txt", "r",  encoding="utf-8") as word:
    w = word.read()
    words = w.strip().split('\n')
    print(words)



print("시작합니다.")
a = 0 # 맞췄을 때
k = 0 # 틀린 개수를 세기 위함.
start = time.time()
for i in range(5):
    random_word = random.choice(words)
    print(random_word)
    input("단어를 적어주세요")
    if random_word == input():
        mixer.music.load("assets/good.wav") # 소리 파일 위치 path
        mixer.music.play() # 소리가 들린다.
        print(f"{a+1}개 맞췄습니다.")
        a = a + 1
    else:
        mixer.music.load("assets/bad.wav") # 소리 파일 위치 path
        mixer.music.play() # 소리가 들린다.
        print(f"{k+1}개 틀렸습니다.")
        k = k + 1
end = time.time()
    
t = end - start
during_time = round(t, 2)
if a >= 3:
    print(f"타자 치는데 {during_time}초가 걸렸고 합격입니다.")
else:
    print(f"타자 치는데 {during_time}초가 걸렸고 불합격입니다.")




import csv
with open("data/word_game_score.csv", "a", newline="", encoding="utf-8") as game_score:
    w = csv.writer(game_score)
    w.writerow([during_time, a])
