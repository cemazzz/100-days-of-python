boss_hp = 360
player_name = input("enter name: ")
player_dame = int(input("enter dame: "))
for i in range(1,6):
    boss_hp = boss_hp - player_dame
    print("round", i,"boss hp: " ,boss_hp)
if boss_hp <= 0:
    prinṭ̣̣("bosss is defeated by", player_name)
if boss_hp <= 0:
    print("rank SSS+",player_name , "is WINNER!")
elif boss_hp <= 36:
    print("rank A+",player_name , "is DRAW!")
else:
    print("rank F",player_name , "is a LOSER!")

