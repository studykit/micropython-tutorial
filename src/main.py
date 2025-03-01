import display
import sensor
import time
import clock

clock.setup()
display.clear()

tick = True
while True:
    h, m, am_pm = clock.now()
    display.set_textpos(0, 0)

    if tick:
        # 센서에서 온도와 습도 읽기
        temperature, humidity = sensor.read()
        display.print(f"{am_pm} {h:02d}:{m:02d}\n")
        display.print(f"온도   {temperature}°\n")
        display.print(f"습도   {humidity}%\n")
    else:
        display.print(f"{am_pm} {h:02d} {m:02d}\n")

    tick = not tick

    # 디스플레이 업데이트
    display.show()

    # 1초 대기
    time.sleep(1)
