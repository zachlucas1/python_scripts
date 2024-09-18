from tkinter import Tk, Frame, Canvas, BOTH
import math


def main(): #this creates the window that we can draw in
    width = 800
    height = 500

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

house_triangle_points = []
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    # tree_left = scene_left + 500
    # tree_top = scene_top + 100
    # tree_height = 150
    # draw_pine_tree(canvas, tree_left, tree_top, tree_height)
    
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_cloud(canvas, 50, 75, scale=1)
    draw_cloud(canvas, 100, 125, scale=1)
    draw_cloud(canvas, 150, 100, scale=1)
    draw_house_body(canvas, 400, 200, 600, 400)
    draw_house_window_left(canvas, 425, 225, 475, 275)
    draw_house_window_right(canvas, 525, 225, 575, 275)
    draw_house_roof(canvas, house_triangle_points)
    draw_house_door(canvas, 485, 325, 515, 400)
    draw_ground(canvas, scene_left, 400, scene_right, scene_bottom)
    draw_sun(canvas, 650, 75, scale=1)
    
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_house_roof(canvas, house_triangle_points):
    house_triangle_points = [375, 200, 625, 200, 500, 100]
    canvas.create_polygon(house_triangle_points)

def draw_house_door(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill='red')

def draw_house_window_right(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill='#FFFFFF', outline='#FFFFFF')

def draw_house_window_left(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill='#FFFFFF', outline='#FFFFFF')

def draw_house_body(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill='burlywood2')

def draw_cloud(canvas, cloud_left, cloud_top, scale=1):
    cloud_width = 200 * scale
    cloud_height = 100 * scale
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='#FFFFFF', width=False)

def draw_ground(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill='#449909')

def draw_sky(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill='lightskyBlue')

#this draws a grid so its easier to make shapes
def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    
    #shifts text over a bit
    text_horizontal_margin = 20 
    text_vertical_margin = 10

    #draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

    #draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

def draw_sun(canvas, sun_left, sun_top, scale=1):
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_length = 100 * scale
    ray_width = 3 * scale
    ray_count = 10

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill='#FFFF00', width=False)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width = ray_width, fill='#FFFF00')


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters:
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()

# def draw_house_roof(canvas, left_x, left_y, right_x, right_y, top_x, top_y):
#     canvas.create_polygon(canvas, left_x, left_y, right_x, right_y, top_x, top_y, fill='red')