from PIL import Image
import os
import time

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

total = 0
start_time = time.time()

print("=" * 60)
print("       BATCH IMAGE RENDERING / PROCESSING")
print("=" * 60)

for filename in os.listdir(INPUT_DIR):

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    total += 1

    input_path = os.path.join(INPUT_DIR, filename)

    try:
        # Open image
        image = Image.open(input_path)

        original_width, original_height = image.size
        original_size = os.path.getsize(input_path) / 1024

        # Resize
        image.thumbnail((1280, 1280))

        new_width, new_height = image.size

        # Convert to WebP
        output_name = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        image.save(output_path, "WEBP", quality=80)

        output_size = os.path.getsize(output_path) / 1024

        print()
        print(f"INPUT  : {filename}")
        print(f"SIZE   : {original_width} x {original_height}")
        print(f"FILE   : {original_size:.2f} KB")
        print(f"OUTPUT : {output_name}")
        print(f"SIZE   : {new_width} x {new_height}")
        print(f"FILE   : {output_size:.2f} KB")
        print("-" * 60)

    except Exception as e:
        print(f"Error processing {filename}: {e}")

end_time = time.time()

print()
print("=" * 60)
print(f"TOTAL IMAGES PROCESSED : {total}")
print(f"TOTAL TIME             : {end_time - start_time:.2f} seconds")
print("=" * 60)
print("BATCH RENDERING COMPLETED")