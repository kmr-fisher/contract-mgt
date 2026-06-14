from PIL import Image
import os

src = r"C:\Claude\Code\Local_Session\pwa\logo_source.png"
out_dir = r"C:\Claude\Code\Local_Session\pwa\icons"
os.makedirs(out_dir, exist_ok=True)

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

img = Image.open(src).convert("RGBA")

for s in sizes:
    # Create white background canvas
    canvas = Image.new("RGBA", (s, s), (255, 255, 255, 255))
    # Resize logo keeping aspect ratio, with 12% padding
    pad = int(s * 0.12)
    inner = s - pad * 2
    logo = img.copy()
    logo.thumbnail((inner, inner), Image.LANCZOS)
    # Center on canvas
    x = (s - logo.width) // 2
    y = (s - logo.height) // 2
    canvas.paste(logo, (x, y), logo)
    # Save as PNG
    canvas.convert("RGB").save(os.path.join(out_dir, f"icon-{s}.png"), "PNG", optimize=True)
    print(f"Generated icon-{s}.png")

print("Done!")
