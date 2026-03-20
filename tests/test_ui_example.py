def test_google(playwright_page):
    playwright_page.goto("https://www.google.com")
    assert "Google" in playwright_page.title()
