print("well come to this challenge")
user1 = input("user one what is your name ?\n ")
user2 = input("user two what is your name ? \n")

love_string = user1 + user2
lower_love = love_string.lower()

t = lower_love.count("t")
r = lower_love.count("r")
u = lower_love.count("u")
e = lower_love.count("e")

true = t + r + u + e

l = lower_love.count("l")
o = lower_love.count("o")
v = lower_love.count("v")
e = lower_love.count("e")

love = l + o + v + e

love_line = int(str(true) + str(love))

if (love_line<10) or (love_line>90):
    print(f"degry has a {love_line}$. your case just be a frinds dont good for real ")
elif(love_line >=40) and (love_line <=70):
    print(f"degry has a {love_line}$.that a true love your hurt together now")
else:
    print(f"degry has a {love_line}. not bad not good")