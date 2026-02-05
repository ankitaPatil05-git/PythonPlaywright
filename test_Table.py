import re
import time

from playwright.sync_api import Page, expect


def test_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            column = i
            print(f"Colum value is {i}")
            break

    Cheese_row = page.locator("tr").filter(has_text="Tomato")
    #expect(row.locator("td").nth(column).filter(has_text="34"))
    #expect(Cheese_row.locator("td").nth(column)).to_have_text("34")
    #expect(rice.locator("td").nth(priceColValue)).to_have_text("37")

    expect(Cheese_row.locator("td").nth(column)).to_have_text(re.compile(r"^\d+(\.\d+)?$"))


