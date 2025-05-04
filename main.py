import turtle
import random

COLUMNS = 12
ROWS = 6
COLUMN_LABELS = [chr(ord('A') + i) for i in range(COLUMNS)]
ROW_LABELS = [str(i + 1) for i in range(ROWS)]

def get_availability_percentage(hour):
    if 7 <= hour <= 11:
        return 0.2
    elif 12 <= hour <= 17:
        return 0.5
    else:
        return 0.8

def generate_available_spots(availability_percentage):
    total_spots = ROWS * COLUMNS
    available_count = int(total_spots * availability_percentage)
    all_spots = [(row, col) for row in range(ROWS) for col in range(COLUMNS)]
    return set(random.sample(all_spots, available_count))

def draw_spot(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_parking_grid(t, available_spots, origin_x, origin_y, cell_w, cell_h, h_gap, v_gap, unavailable_color):
    for row in range(ROWS):
        for col in range(COLUMNS):
            is_left = col < 6
            block_x = origin_x if is_left else origin_x + (6 * cell_w) + h_gap

            section_row = row // 2
            y = origin_y - (row * cell_h) - (section_row * v_gap)
            x = block_x + (col % 6) * cell_w

            color = "white" if (row, col) in available_spots else unavailable_color
            draw_spot(t, x, y, cell_w, cell_h, color)

    for row in range(ROWS):
        section_row = row // 2
        y = origin_y - (row * cell_h) - (section_row * v_gap) + cell_h / 4
        t.penup()
        t.goto(origin_x + 6 * cell_w + h_gap / 2 - 5, y)
        t.write(str(ROWS - row), align="center", font=("Arial", 10, "bold"))

    for col in range(COLUMNS):
        label_x = origin_x + (col % 6) * cell_w
        if col >= 6:
            label_x += 6 * cell_w + h_gap
        t.penup()
        t.goto(label_x + cell_w / 2, origin_y - ROWS * cell_h - 2 * v_gap)
        t.write(COLUMN_LABELS[col], align="center", font=("Arial", 10, "bold"))

def draw_legend(t, x_start, y_start, unavailable_color):
    t.penup()
    t.goto(x_start, y_start)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x_start + 25, y_start + 5)
    t.write("Available", font=("Arial", 10, "normal"))

    t.penup()
    t.goto(x_start + 120, y_start)
    t.pendown()
    t.fillcolor(unavailable_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x_start + 145, y_start + 5)
    t.write("Unavailable", font=("Arial", 10, "normal"))

def main():
    print("Welcome to the Availability Visualiser!")
    while True:
        try:
            hour = int(input("Enter check-in hour (0–23): "))
            if 0 <= hour <= 23:
                break
            else:
                print("Enter hour between 0 and 23.")
        except ValueError:
            print("Invalid input.")

    bg_color = input("Choose a Background color (lightgrey, skyblue, yellow)\n>> Background Color (default lightgrey): ").strip().lower()
    if bg_color not in ["lightgrey", "skyblue", "yellow"]:
        bg_color = "lightgrey"

    unavailable_color = input("Choose an unavailable spot color (red, green, blue)\n>> Unavailable Color (default red): ").strip().lower()
    if unavailable_color not in ["red", "green", "blue"]:
        unavailable_color = "red"

    percent = get_availability_percentage(hour)
    print(f"Average parking availability: {int(percent * 100)}%")

    spots = generate_available_spots(percent)

    screen = turtle.Screen()
    screen.title("Parking Layout Viewer")
    screen.setup(width=800, height=800)
    screen.bgcolor(bg_color)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    cell_w = 50
    cell_h = 50
    h_gap = 100
    v_gap = 20

    grid_origin_x = - (6 * cell_w + h_gap // 2)
    grid_origin_y = 250

    draw_parking_grid(t, spots, grid_origin_x, grid_origin_y, cell_w, cell_h, h_gap, v_gap, unavailable_color)
    draw_legend(t, -350, -150, unavailable_color)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
