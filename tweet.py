from playwright.sync_api import sync_playwright
import time
import psutil
import os
import re

def extract_tweet_id(href):
    match = re.search(r'status/(\d+)', href)
    return match.group(1) if match else None

start_time = time.time()
perf_start = time.perf_counter()
process = psutil.Process(os.getpid())

print("[🚀] Starting auto-reply script...")

with sync_playwright() as p:
    browser_start = time.perf_counter()
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    browser_end = time.perf_counter()

    try:
        tweet_url = 'https://x.com/rionvhk/status/1909069543772991702'
        reply_text = "🚀 Auto-reply with fallback button worked! -Diazzzzz"

        nav_start = time.perf_counter()
        print(f"[+] Navigating to tweet: {tweet_url}")
        page.goto(tweet_url, timeout=60000)
        page.wait_for_timeout(5000)
        page.screenshot(path="before_typing.png")
        nav_end = time.perf_counter()

        print("[+] Typing reply...")
        type_start = time.perf_counter()
        tweet_box = page.locator('[data-testid="tweetTextarea_0"]').first
        tweet_box.wait_for(state="visible", timeout=30000)
        tweet_box.click()
        tweet_box.fill(reply_text)
        type_end = time.perf_counter()

        page.screenshot(path="before_click.png")

        posted = False
        click_start = time.perf_counter()

        try:
            print("[+] Trying to click tweetButtonInline...")
            button_inline = page.locator('button[data-testid="tweetButtonInline"]').first
            button_inline.wait_for(state="visible", timeout=10000)
            button_inline.click()
            posted = True
            print("[✅] tweetButtonInline clicked successfully!")
        except Exception:
            print("[⚠️] tweetButtonInline not found, trying fallback tweetButton...")
            button_fallback = page.locator('button[data-testid="tweetButton"]').first
            button_fallback.wait_for(state="visible", timeout=10000)
            button_fallback.click()
            posted = True
            print("[✅] Fallback tweetButton clicked successfully!")

        click_end = time.perf_counter()

        if posted:
            print("[+] Waiting for tweet to appear...")
            page.wait_for_timeout(5000)
            page.screenshot(path="tweet_success.png")

            print("[+] Extracting Tweet ID...")
            id_start = time.perf_counter()
            tweet_link = page.locator('a[href*="/status/"]').first
            href = tweet_link.get_attribute("href")
            tweet_id = extract_tweet_id(href)
            id_end = time.perf_counter()

            if tweet_id:
                print(f"[✅] Reply Tweet ID: {tweet_id}")
                with open("reply_tweet_id.txt", "w") as f:
                    f.write(tweet_id)
            else:
                print("[⚠️] Unable to extract Tweet ID.")

    except Exception as err:
        print(f"[❌] Failed to send reply: {err}")
        page.screenshot(path="tweet_error.png")
    finally:
        browser.close()
        print("[+] Browser closed.")

        # Execution timing & resource usage
        end_time = time.time()
        perf_end = time.perf_counter()
        elapsed = end_time - start_time
        perf_elapsed = perf_end - perf_start
        memory_usage_mb = process.memory_info().rss / (1024 * 1024)
        cpu_percent = process.cpu_percent(interval=0.2)

        print("\n[📊] Execution Summary:")
        print(f"⏱️ Total time: {elapsed:.2f}s (perf counter: {perf_elapsed:.2f}s)")
        print(f"   ├─ Browser launch      : {browser_end - browser_start:.2f}s")
        print(f"   ├─ Navigate & load     : {nav_end - nav_start:.2f}s")
        print(f"   ├─ Type reply          : {type_end - type_start:.2f}s")
        print(f"   ├─ Click post button   : {click_end - click_start:.2f}s")
        print(f"   └─ Extract Tweet ID    : {id_end - id_start:.2f}s")
        print(f"🧠 Memory used : {memory_usage_mb:.2f} MB")
        print(f"⚙️ CPU used    : {cpu_percent:.2f}%\n")
