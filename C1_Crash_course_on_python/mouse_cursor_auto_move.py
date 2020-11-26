import pyautogui

print(pyautogui.size())

for x in range(1,1920,100):
    for y in range (1,1080,100):
        pyautogui.moveTo(x,y, duration = 2)

# y = 1
# while y < 1080:
#     x = 1
#     pyautogui.moveTo(x, y, duration=2)
#     y += 100
#
# y = 1080
# x = 1
# while x < 1920:
#     pyautogui.moveTo(x, y, duration=2)
#     x += 100
#
# x = 1920
# while y > 1:
#     pyautogui.moveTo(x, y, duration=2)
#     x -= 100