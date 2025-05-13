import time
import random
import csv
import threading
import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.common.by import By
import os
import undetected_chromedriver as uc
from tkinter import ttk

# Fungsi scraping
def scrape(auth_token, query, max_tweets):
    options = uc.ChromeOptions()
    options.add_argument("--headless")  # Hapus/dibuat komentar line ini jika ingin lihat browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://twitter.com")
        time.sleep(3)

        driver.add_cookie({
            "name": "auth_token",
            "value": auth_token
        })

        search_url = f"https://twitter.com/search?q={query}&src=typed_query&f=live"
        driver.get(search_url)
        time.sleep(5)

        tweets_data = []
        tweet_texts = set()
        last_height = driver.execute_script("return document.body.scrollHeight")

        while len(tweets_data) < max_tweets:
            elements = driver.find_elements(By.XPATH, '//article')
            for el in elements:
                try:
                    # Clean username and tweet content
                    username = el.find_element(By.XPATH, './/span[starts-with(text(), "@")]').text.strip()
                    raw_text = el.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
                    tweet_body = ' '.join(raw_text.split())
                    if tweet_body and tweet_body not in tweet_texts:
                        tweet_texts.add(tweet_body)
                        tweets_data.append((username, tweet_body))
                except:
                    continue

            status_label.config(text=f"Cuitan terkumpul: {len(tweets_data)}")
            progress['value'] = len(tweets_data)
            progress.update()
            root.update()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        driver.quit()

        # Generate unique filename to avoid overwriting previous outputs
        base_name = "data_twitter"
        ext = ".csv"
        filename = f"{base_name}{ext}"
        counter = 1
        while os.path.exists(filename):
            filename = f"{base_name}_{counter}{ext}"
            counter += 1
        with open(filename, "w", newline="", encoding="utf-8") as f:
            # Use quoting to wrap any commas/newlines cleanly
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(["Username", "Cuitan"])
            for username, tweet in tweets_data[:max_tweets]:
                writer.writerow([username, tweet])

        status_label.config(text=f"✅ Selesai! File disimpan sebagai '{filename}'")
        messagebox.showinfo("Selesai", f"Scraping selesai dan disimpan sebagai '{filename}'")
        # Re-enable inputs
        start_button.state(['!disabled'])
        token_entry.state(['!disabled'])
        query_entry.state(['!disabled'])
        limit_entry.state(['!disabled'])
        progress['value'] = progress['maximum']
        progress.update()

    except Exception as e:
        driver.quit()
        status_label.config(text="❌ Terjadi kesalahan.")
        messagebox.showerror("Error", str(e))
        # Re-enable inputs on error
        start_button.state(['!disabled'])
        token_entry.state(['!disabled'])
        query_entry.state(['!disabled'])
        limit_entry.state(['!disabled'])

# Jalankan di thread agar GUI tidak freeze
def start_scrape_thread():
    auth = token_entry.get().strip()
    q = query_entry.get().strip()
    try:
        m = int(limit_entry.get())
    except ValueError:
        messagebox.showwarning("Input Salah", "Jumlah tweet harus berupa angka!")
        return

    if not auth or not q:
        messagebox.showwarning("Input Kosong", "Silakan isi semua kolom.")
        return

    # Reset progress and disable inputs
    progress['maximum'] = m
    progress['value'] = 0
    status_label.config(text="Memulai scraping...")
    start_button.state(['disabled'])
    token_entry.state(['disabled'])
    query_entry.state(['disabled'])
    limit_entry.state(['disabled'])
    threading.Thread(target=scrape, args=(auth, q, m), daemon=True).start()

# =============== GUI TKINTER ===============
root = tk.Tk()
root.title("Twitter Scraper GUI")
root.geometry("550x350")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill='both', expand=True)

# Auth Token
ttk.Label(frame, text="Auth Token:").grid(row=0, column=0, sticky='e', padx=(0,10), pady=5)
token_entry = ttk.Entry(frame, width=50, show="*")
token_entry.grid(row=0, column=1, sticky='w', pady=5)

# Kata Kunci Pencarian
ttk.Label(frame, text="Kata Kunci Pencarian:").grid(row=1, column=0, sticky='e', padx=(0,10), pady=5)
query_entry = ttk.Entry(frame, width=50)
query_entry.grid(row=1, column=1, sticky='w', pady=5)

# Jumlah Cuitan
ttk.Label(frame, text="Jumlah Cuitan:").grid(row=2, column=0, sticky='e', padx=(0,10), pady=5)
limit_entry = ttk.Entry(frame, width=20)
limit_entry.insert(0, "1000")
limit_entry.grid(row=2, column=1, sticky='w', pady=5)

# Mulai Scraping Button
start_button = ttk.Button(frame, text="Mulai Scraping", command=start_scrape_thread)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

# Progress Bar
progress = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate')
progress.grid(row=4, column=0, columnspan=2, pady=5)

# Status Label
status_label = ttk.Label(frame, text="")
status_label.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
