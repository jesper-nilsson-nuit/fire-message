import os
import random
import time
import msvcrt

os.system("cls||clear")

terminal_size = os.get_terminal_size()

# Define your desired update rate (e.g., 60 updates per second)
UPDATE_RATE = 27.0
UPDATE_INTERVAL = 1.0 / UPDATE_RATE  # Time between updates

# Initialize time tracking
previous_time = time.time()
accumulator = 0.0

pixel_color = {
    0: "\033[38;5;0m",
    1: "\033[38;5;52m",
    2: "\033[38;5;94m",
    3: "\033[38;5;131m",
    4: "\033[38;5;172m",
    5: "\033[38;5;173m",
    6: "\033[38;5;214m",
    7: "\033[38;5;222m",
    8: "\033[38;5;230m",
    9: "\033[38;5;255m",
    10: "\033[1;4;38;5;255m",
    11: "\033[24m",
}


fire_width = 0
fire_height = 0
fire_pixels = {}
for index, size in enumerate(terminal_size):
    if index == 0:
        fire_width = size
    elif index == 1:
        fire_height = size

# Fill the list with 0
for pixel in range(fire_height * fire_width):
    fire_pixels[pixel] = 0

# Fill the last row with 9
for x in range(fire_width):
    fire_pixels[(fire_height - 1) * fire_width + x] = 9


message = "Welcome to the greatest student system in the world!"

message_length = len(message)
front_of_message = round((fire_width - message_length) / 2) - 1
after_message = front_of_message + message_length


middle_row = round(fire_height / 2)
second_middle_row = middle_row + 1
top_row = []
message_section = []
for pixel in range(fire_width):
    top_row.append(1 * fire_width + pixel)
    if pixel not in range(front_of_message) and pixel not in range(after_message, fire_width):
        message_section.append({middle_row * fire_width + pixel: 9})

for index, key in enumerate(message_section):
    message_section[index]["char"] = message[index]
    message_section[index]["reached"] = False


def spread_fire(source):
    if source in top_row:
        return
    pixel = fire_pixels[source]
    for char_pixel in message_section:
        if source in char_pixel and 3 <= pixel < 9:
            fire_pixels[source] = 9
            pixel = fire_pixels[source]
            char_pixel["reached"] = True
    if pixel == 0:
        fire_pixels[source - fire_width] = 0
    elif source not in message_section and pixel not in message_section:
        # fire_dying_out_factor = random.randint(0,3)
        fire_dying_out_factor = random.choices([1, 2], weights=[65, 25])[0]
        destination_pixel = source - fire_dying_out_factor + 1
        fire_pixels[destination_pixel - fire_width] = max(pixel - (fire_dying_out_factor & 1), 0)


def do_fire():
    for x in range(fire_width):
        for y in range(1, fire_height):
            spread_fire(y * fire_width + x)


while True:
    if msvcrt.kbhit():
        key_press = msvcrt.getch()
        if key_press == "\r":
            break
    # Calculate delta time (time elapsed since last frame)
    current_time = time.time()
    delta_time = current_time - previous_time
    previous_time = current_time

    # Accumulate delta time
    accumulator += delta_time

    # Check if enough time has passed to update fire
    if accumulator >= UPDATE_INTERVAL:
        print("\033[H", end="")
        do_fire()
        color = 0
        skip = False
        for pixel in fire_pixels:
            color_index = fire_pixels[pixel]
            color = pixel_color[color_index]
            for char_pixel in message_section:
                if pixel in char_pixel and char_pixel["reached"]:
                    print(pixel_color[10] + char_pixel["char"] + pixel_color[11], end="")
                    skip = True
            if skip:
                skip = False
                continue
            elif color == pixel_color[0]:
                print(color + " ", end="")
            elif color == pixel_color[1] or color == pixel_color[2] or color == pixel_color[3]:
                print(color + ".", end="")
            elif color == pixel_color[4] or color == pixel_color[5]:
                print(color + "'", end="")
            elif color == pixel_color[6] or color == pixel_color[7]:
                print(color + "*", end="")
            elif color == pixel_color[8]:
                print(color + "=", end="")
            else:
                print(color + "@", end="")

        # Reset the accumulator, subtracting the interval
        accumulator -= UPDATE_INTERVAL
    time.sleep(0.0001)