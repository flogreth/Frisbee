import time, board, analogio

sound_pin = board.A0
peak_threshold = 10000
time_threshold = 0.2

sound_sensor = analogio.AnalogIn(sound_pin)

def measure_peak_distance():
    #print(sound_sensor.value)
    start_time = time.monotonic()
    while sound_sensor.value < peak_threshold:
        pass
    peak_start_time = time.monotonic()
    while sound_sensor.value >= peak_threshold:
        pass
    peak_end_time = time.monotonic()
    return peak_end_time - peak_start_time

while True:
    print(sound_sensor.value)
    #peak_distance = measure_peak_distance()
    #volume = 1 / max(peak_distance,1)
    #print("Lautstärke:", volume)
    time.sleep(0.05)