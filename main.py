from playwright.sync_api \
    import sync_playwright
    
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://search.azlyrics.com")
    
    
    song = input("Nombre de la canción: ")
    page.locator("input:near(.eac-bootstrap)").first.fill(song)
    
    page.locator("button:has-text(\"Search\")").first.click()
    
    rows = page.locator('tbody').first.locator('td')
    
    for i in range(rows.count()-1):
        text = rows.nth(i).inner_text()
        print(text)
        
    val = int(input('Selecciona una canción: '))
    val -=1
    rows.nth(val).click()
    song = page.locator('xpath=/html/body/div[2]/div[2]/div[2]/div[5]')
    
    for line in song.all_inner_texts():
        print(line)
    browser.close()