import os
import re
import time
import img2pdf
from io import BytesIO
from PIL import Image
from playwright.sync_api import sync_playwright

# ==========================================
# CONFIGURATION
# ==========================================
OUTPUT_DIR = "captured_pages"
OUTPUT_PDF = "final_complete_flipbook.pdf"
WAIT_TIME_PER_PAGE = 3.5  # Seconds to wait for high-res fonts/vectors to render

# ==========================================
# SCRIPT LOGIC
# ==========================================
def capture_with_keyboard():
    print("\n" + "="*60)
    print(" FLIPBOOK AUTOMATION DOWNLOADER")
    print("="*60)
    
    # Safely prompt the user for the exact URL and page count
    start_url = input("\n[?] Paste the FULL URL of your flipbook:\n> ").strip()
    if not start_url.startswith("http"):
        print("[-] Invalid URL. It must start with http:// or https://")
        return

    try:
        total_pages = int(input("[?] How many pages in total does the book have?:\n> ").strip())
    except ValueError:
        print("[-] Please enter a valid numerical digit.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("\n[*] Launching browser window...")
    with sync_playwright() as p:
        # Launching with headless=False so you can watch and interact if needed
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        print(f"[*] Navigating to starting URL: {start_url}")
        try:
            page.goto(start_url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"[-] Failed to load URL: {e}")
            return
        
        print("\n" + "="*60)
        print(" [!] MANUAL INTERACTION STEP:")
        print(" 1. Go to the browser window that just opened.")
        print(" 2. Close any cookie pop-ups or login prompts.")
        print(" 3. Make sure you are at Page 1 of the book.")
        print("="*60 + "\n")
        
        # Give you 15 seconds to quickly clear any popups or center the page
        for i in range(15, 0, -1):
            print(f"Starting automation in {i} seconds...", end="\r")
            time.sleep(1)
        print("\n[*] Automation started. Do not click inside the browser window now.\n")

        for page_num in range(1, total_pages + 1):
            filename = f"page_{page_num:04d}.png"
            filepath = os.path.join(OUTPUT_DIR, filename)

            # Wait for the network to deliver the heavy images and text vectors
            time.sleep(WAIT_TIME_PER_PAGE)

            # Capture the viewport
            if not os.path.exists(filepath):
                page.screenshot(path=filepath)
                print(f"[+] Captured Page {page_num}/{total_pages}")
            else:
                print(f"[*] Page {page_num} file already exists. Skipping capture.")

            # Turn the page using the keyboard right arrow key (except on the very last page)
            if page_num < total_pages:
                page.keyboard.press("ArrowRight")
                time.sleep(0.5)

        browser.close()

    build_pdf()

def build_pdf():
    print(f"\n[*] Compiling images into PDF: {OUTPUT_PDF}...")
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.png')]
    files.sort(key=lambda f: int(re.search(r'\d+', f).group()))

    if not files:
        print("[-] No images found to compile.")
        return

    image_data_list = []
    for file in files:
        filepath = os.path.join(OUTPUT_DIR, file)
        try:
            with Image.open(filepath) as img:
                if img.mode != "RGB":
                    img = img.convert("RGB")
                
                img_byte_arr = BytesIO()
                img.save(img_byte_arr, format='JPEG', quality=95)
                image_data_list.append(img_byte_arr.getvalue())
        except Exception as e:
            print(f"[-] Error processing {file}: {e}")

    if image_data_list:
        try:
            pdf_bytes = img2pdf.convert(image_data_list)
            with open(OUTPUT_PDF, "wb") as f:
                f.write(pdf_bytes)
            print(f"[+] Success! Fully rendered PDF saved to {OUTPUT_PDF}")
        except Exception as e:
            print(f"[-] Error writing PDF file: {e}")

if __name__ == "__main__":
    capture_with_keyboard()