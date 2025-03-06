# Terminal Fire Animation

A dynamic fire animation that runs in the terminal with interactive text display.

Based on <a href="https://fabiensanglard.net/doom_fire_psx/">Fabien Sanglard's 'How DOOM fire was done'</a>

## Features

- Real-time fire simulation in the terminal
- Text message revealed through the fire animation
- Frame rate control using delta time calculations

## Technical Details

- Written in Python
- Uses ANSI escape codes for colorful terminal output
- Terminal size detection for responsive display (not perfect)
- Implements a fire spreading algorithm

## How It Works

The animation simulates fire using a pixel array and spreading algorithm:
- Fire intensity is represented by color values (0-9)
- The bottom row acts as the fire source
- Fire propagates upward with random decay
- Text message is revealed when the fire reaches each letters position

## Usage

Run the script with:

```bash
python fire_test.py
```

## Preview

![Animation Demo](preview.gif)

