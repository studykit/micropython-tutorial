import time
import ntptime
from machine import RTC

clock_initialized = False
clock = RTC()

def setup():
    global clock_initialized
    global clock

    if clock_initialized:
        return

    ntptime.host = 'time.google.com'
    ntptime.settime()  # ntptime으로 RTC를 UTC 시간으로 설정

    # 현재 UTC 시간을 초 단위로 가져와서, 9시간(9*3600초)을 더한 후 한국 시간으로 변환합니다.
    utc_seconds = time.mktime(time.localtime())
    kst_seconds = utc_seconds + (9 * 3600)
    t = time.localtime(kst_seconds)

    clock.datetime((t[0], t[1], t[2], 0, t[3], t[4], t[5], 0))
    clock_initialized = True

def now():
    _, _, _, _, h, m, s, _ = clock.datetime()
    return h, m