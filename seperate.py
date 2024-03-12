from PIL import Image


def slice_spritesheet(input_path, output_path, sprite_width, sprite_height):

    spritesheet = Image.open(input_path)
    sheet_width, sheet_height = spritesheet.size

    num_cols = sheet_width // sprite_width
    num_rows = sheet_height // sprite_height

    for row in range(num_rows):
        for col in range(num_cols):
            left = col * sprite_width
            upper = row * sprite_height
            right = left + sprite_width
            lower = upper + sprite_height
            icon = spritesheet.crop((left, upper, right, lower))
            icon.save(f"{output_path}/icon_{row * num_cols + col}.png")


if __name__ == "__main__":
    input_path = "spritesheet.png"
    output_path = "icons"
    sprite_width = 48
    sprite_height = 48
    slice_spritesheet(input_path, output_path, sprite_width, sprite_height)
