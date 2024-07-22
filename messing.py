from PIL import Image
import struct

def read_cur(filename):
    with open(filename, 'rb') as f:
        header = f.read(6)
        num_images = struct.unpack('<H', f.read(2))[0]
        entries = []
        for _ in range(num_images):
            entry = f.read(16)
            if len(entry) == 16:
                values = struct.unpack('<BBBxHHII', entry)
                entries.append(values)
                print(f"Unpacked values: {values}")
            else:
                print(f"Skipping invalid entry: {entry}")
        image_data = []
        for width, height, num_colors, reserved, hot_x, hot_y, size, offset in entries:
            f.seek(offset)
            data = f.read(size)
            image_data.append((width, height, hot_x, hot_y, data))
        return image_data

def write_cur(filename, image_data):
    with open(filename, 'wb') as f:
        f.write(b'\x00\x00\x02\x00')
        f.write(struct.pack('<H', len(image_data)))
        offset = 6 + 16 * len(image_data)
        for width, height, hot_x, hot_y, data in image_data:
            size = len(data)
            f.write(struct.pack('<BBBxHHII', width, height, 0, hot_x, hot_y, size, offset))
            offset += size
        for _, _, _, _, data in image_data:
            f.write(data)

# Open the original .cur file
image_data = read_cur('assets/Hand 1.cur')

resized_image_data = []
for width, height, hot_x, hot_y, data in image_data:
    img = Image.frombytes('RGBA', (width, height), data)
    img_resized = img.resize((64, 64), Image.LANCZOS)

    # Convert the resized image back to bytes with correct format
    resized_data = img_resized.convert("RGBA").tobytes()
    resized_image_data.append((64, 64, hot_x, hot_y, resized_data))

# Save the resized image data as a new .cur file
write_cur('assets/Hand 1_resized.cur', resized_image_data)

print("Image resized and saved as CUR successfully!")
