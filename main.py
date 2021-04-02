sleep_time = 0
def LEDをつけて少し停止(LED_X: number, LED_Y: number):
    global sleep_time
    led.plot(LED_X, LED_Y)
    basic.pause(sleep_time)
    sleep_time += 0 - 1
def LEDを消して少し停止(LED_X: number, LED_Y: number):
    global sleep_time
    led.unplot(LED_X, LED_Y)
    basic.pause(sleep_time)
    sleep_time += 0 - 1

def on_forever():
    global sleep_time
    sleep_time = 100
    while sleep_time >= 0:
        LEDをつけて少し停止(2, 2)
        LEDをつけて少し停止(3, 3)
        LEDをつけて少し停止(2, 4)
        LEDをつけて少し停止(1, 4)
        LEDをつけて少し停止(0, 3)
        LEDをつけて少し停止(0, 2)
        LEDをつけて少し停止(0, 1)
        LEDをつけて少し停止(1, 0)
        LEDをつけて少し停止(2, 0)
        LEDをつけて少し停止(3, 0)
        LEDをつけて少し停止(4, 1)
        LEDをつけて少し停止(4, 2)
        LEDをつけて少し停止(4, 3)
        LEDを消して少し停止(2, 2)
        LEDを消して少し停止(3, 3)
        LEDを消して少し停止(2, 4)
        LEDを消して少し停止(1, 4)
        LEDを消して少し停止(0, 3)
        LEDを消して少し停止(0, 2)
        LEDを消して少し停止(0, 1)
        LEDを消して少し停止(1, 0)
        LEDを消して少し停止(2, 0)
        LEDを消して少し停止(3, 0)
        LEDを消して少し停止(4, 1)
        LEDを消して少し停止(4, 2)
        LEDを消して少し停止(4, 3)
basic.forever(on_forever)
