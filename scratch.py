from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://practice.expandtesting.com/webpark")

    # Step 1: Calculate
    page.locator("#parkingLot").select_option("Valet")
    page.locator("#entryDate").fill("2026-09-07")
    page.locator("#entryTime").fill("10:00")
    page.locator("#exitDate").fill("2026-09-08")
    page.locator("#exitTime").fill("10:00")
    page.locator("#calculateCost").click()
    page.wait_for_timeout(1000)
    
    # Step 2: Book Now
    page.locator("a:has-text('Book Now!')").click()
    page.wait_for_timeout(1500)
    
    # Step 3: Fill Booking details
    page.locator("#firstName").fill("John")
    page.locator("#lastName").fill("Doe")
    page.locator("#email").fill("john.doe@example.com")
    page.locator("#phone").fill("1234567890")
    page.locator("#vehicleSize").select_option("small")
    page.locator("#lpNumber").fill("ABC1234")
    page.locator("#continue").click()
    page.wait_for_timeout(1500)
    
    # Step 4: Fill Payment details
    page.locator("#cardNumber").fill("5200828282828223")
    page.locator("#expirationDate").fill("1027")
    page.locator("#securityCode").fill("123")
    page.locator("#completeReservation").click()
    page.wait_for_timeout(2000)

    print("Final Confirmation URL:", page.url)
    print("Final Text:", page.locator("h1, h2, h3, .alert, p").all_inner_texts())

    browser.close()
