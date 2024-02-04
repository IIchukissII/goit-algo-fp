import matplotlib.pyplot as plt
import math
import argparse


def parse_argv():
    parser = argparse.ArgumentParser(description="Визначає рівень рекурсії")
    parser.add_argument(
        "-d", "--depth", type=int, required=True, help="Глибина рекурсії"
    )
    return parser.parse_args()


def draw_pythagorean_tree(x, y, length, angle, depth):
    if depth == 0:
        return
    else:
        x2 = x + length * math.cos(math.radians(angle))
        y2 = y + length * math.sin(math.radians(angle))

        plt.plot([x, x2], [y, y2], "g-")

        draw_pythagorean_tree(x2, y2, length * 0.8, angle - 45, depth - 1)
        draw_pythagorean_tree(x2, y2, length * 0.8, angle + 45, depth - 1)


def main():
    args = parse_argv()
    x = 0
    y = 0
    length = 200
    angle = 90
    depth = args.depth

    fig, ax = plt.subplots()
    ax.set_aspect("equal", "box")
    ax.axis("off")
    draw_pythagorean_tree(x, y, length, angle, depth)
    plt.show()


if __name__ == "__main__":
    main()
