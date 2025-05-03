import turtle
import random

# Constants
COLUMNS = 12
ROWS = 6

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

def draw_parking_grid(t, available_spots, origin_x, origin_y, cell_w, cell_h, h_gap, v_gap):
    for row in range(ROWS):
        for col in range(COLUMNS):
            is_left = col < 6
            block_x = origin_x if is_left else origin_x + (6 * cell_w) + h_gap

            section_row = row // 2
            y = origin_y - (row * cell_h) - (section_row * v_gap)
            x = block_x + (col % 6) * cell_w

            color = "white" if (row, col) in available_spots else "red"
            draw_spot(t, x, y, cell_w, cell_h, color)

def draw_legend(t, x_start, y_start):
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
    t.fillcolor("red")
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
    while True:
        try:
            hour = int(input("Enter check-in hour (0–23): "))
            if 0 <= hour <= 23:
                break
            else:
                print("Enter hour between 0 and 23.")
        except ValueError:
            print("Invalid input.")

    percent = get_availability_percentage(hour)
    spots = generate_available_spots(percent)

    screen = turtle.Screen()
    screen.title("Parking Layout Viewer")
    screen.setup(width=600, height=800)
    screen.tracer(0)
    screen.bgcolor("#f0f0f0")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Dimensions and spacing
    cell_w = 40
    cell_h = 25
    h_gap = 60
    v_gap = 15

    # Start drawing from top-left
    grid_total_height = ROWS * cell_h + (ROWS // 2) * v_gap
    grid_origin_y = grid_total_height // 2
    grid_origin_x = - (6 * cell_w + h_gap // 2)

    draw_parking_grid(t, spots, grid_origin_x, grid_origin_y, cell_w, cell_h, h_gap, v_gap)

    draw_legend(t, -80, -360)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
