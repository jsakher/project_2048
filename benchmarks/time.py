import Game2048
import time

start = time.time()
Game2048.Game_2048().random_2048()
end = time.time()
print("Exection time of the function: {0:.5f} s.".format(end - start))
# 0.00598 s.

start = time.time()
Game2048.Game_2048().clockwise_2048()
end = time.time()
print("Exection time of the function: {0:.5f} s.".format(end - start))
# 0.00501 s.

start = time.time()
Game2048.Game_2048().adjacent_2048()
end = time.time()
print("Exection time of the function: {0:.5f} s.".format(end - start))
# 0.00199 s.; 0.00100 s.; 0.00299 s.

start = time.time()
Game2048.Game_2048().opposite_2048()
end = time.time()
print("Exection time of the function: {0:.5f} s.".format(end - start))
# 0.00100 s.; 0.00197 s.; 0.00202 s.

start = time.time()
RM = Game2048.functions.Fonction_2048.right_movement([[0, 2, 2, 0],[2, 0, 0, 2],[0, 2, 0, 4],[8, 8, 0, 8]], 128)
end = time.time()
print(RM, "Exection time of the function: {0:.15f} s.".format(end - start))

start = time.time()
DM = Game2048.functions.Fonction_2048.down_movement([[0, 2, 2, 0],[2, 0, 0, 2],[0, 2, 0, 4],[8, 8, 0, 8]], 128)
end = time.time()
print(DM, "Exection time of the function: {0:.15f} s.".format(end - start))

start = time.time()
LM = Game2048.functions.Fonction_2048.left_movement([[0, 2, 2, 0],[2, 0, 0, 2],[0, 2, 0, 4],[8, 8, 0, 8]], 128)
end = time.time()
print(LM, "Exection time of the function: {0:.15f} s.".format(end - start))

start = time.time()
UM = Game2048.functions.Fonction_2048.up_movement([[0, 2, 2, 0],[2, 0, 0, 2],[0, 2, 0, 4],[8, 8, 0, 8]], 128)
end = time.time()
print(UM, "Exection time of the function: {0:.15f} s.".format(end - start))