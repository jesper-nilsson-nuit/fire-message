# Terminal Fire Animation

A dynamic fire animation that runs in the terminal with interactive text display.

## Features

- Real-time fire simulation in the terminal
- Text messages revealed through the fire animation
- Frame rate control using delta time calculations
- Interactive - waits for user input to continue

## Technical Details

- Written in Python
- Uses ANSI escape codes for colorful terminal output
- Terminal size detection for responsive display
- Implements a fire spreading algorithm

## How It Works

The animation simulates fire using a pixel array and spreading algorithm:
- Fire intensity is represented by color values (0-9)
- The bottom row acts as the fire source
- Fire propagates upward with random decay
- Text messages are revealed when the fire reaches their position

## Usage

Run the script with:

```bash
python fire_test.py
```

Press ENTER to exit the animation when prompted.

## Preview

<img src="firePreview.png" alt="Preview of the Fire Animation" width="600"/>
