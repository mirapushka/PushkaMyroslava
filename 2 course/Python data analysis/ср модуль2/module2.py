"""Парсер локального каталогу книг з використанням BeautifulSoup, lxml та robotparser."""

import csv
from pathlib import Path
import urllib.robotparser
from bs4 import BeautifulSoup

MOCK_HTML = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Книжковий каталог Data Science</title>
</head>
<body>
    <header><h1>Каталог літератури з аналітики та Python</h1></header>
    <main>
        <div class="catalog-container">
            <article class="product-card" data-id="101">
                <h3 class="product-title">Python для аналізу даних</h3>
                <p class="product-author">Уес Маккінні</p>
                <div class="product-info">
                    <span class="price-value">850.00</span> <span class="currency">грн</span>
                    <span class="stock-status in-stock">В наявності</span>
                </div>
                <a class="product-link" href="/catalog/item/101">Детальніше</a>
            </article>
            <article class="product-card" data-id="102">
                <h3 class="product-title">Прикладне машинне навчання з Scikit-Learn</h3>
                <p class="product-author">Орельєн Жерон</p>
                <div class="product-info">
                    <span class="price-value">1200.00</span> <span class="currency">грн</span>
                    <span class="stock-status in-stock">В наявності</span>
                </div>
                <a class="product-link" href="/catalog/item/102">Детальніше</a>
            </article>
            <article class="product-card" data-id="103">
                <h3 class="product-title">Глибоке навчання без математики</h3>
                <p class="product-author">Франсуа Шолле</p>
                <div class="product-info">
                    <span class="price-value">950.50</span> <span class="currency">грн</span>
                    <span class="stock-status out-of-stock">Очікується</span>
                </div>
                <a class="product-link" href="/catalog/item/103">Детальніше</a>
            </article>
            <article class="product-card" data-id="104">
                <h3 class="product-title">Чистий код у Python</h3>
                <p class="product-author">Маріано Анайя</p>
                <div class="product-info">
                    <span class="price-value">720.00</span> <span class="currency">грн</span>
                    <span class="stock-status in-stock">В наявності</span>
                </div>
                <a class="product-link" href="/catalog/item/104">Детальніше</a>
            </article>
        </div>
        <nav class="pagination">
            <a class="page-link" href="/catalog/page/2">Наступна сторінка &raquo;</a>
        </nav>
    </main>
</body>
</html>
"""


def ensure_html_file(html_path: Path) -> None:
    """Створює HTML-файл каталогу, якщо він ще не існує."""
    if not html_path.exists():
        html_path.write_text(MOCK_HTML.strip(), encoding="utf-8")


def check_robots_permission(robots_url: str, target_url: str, agent: str = "*") -> bool:
    """Перевіряє доступ до цільової адреси через robots.txt з безпечним fallback."""
    try:
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(robots_url)
        parser.read()
        return parser.can_fetch(agent, target_url)
    except Exception:
        return True


def parse_catalog(html_path: Path) -> tuple[list[dict[str, object]], list[str]]:
    """Зчитує HTML, витягує картки товарів та посилання пагінації без повторів."""
    html_content = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_content, "lxml")

    products: list[dict[str, object]] = []
    for card in soup.select(".product-card"):
        title_el = card.select_one(".product-title")
        author_el = card.select_one(".product-author")
        price_el = card.select_one(".price-value")
        stock_el = card.select_one(".stock-status")
        link_el = card.select_one("a.product-link")

        price_text = price_el.get_text(strip=True) if price_el else "0"
        products.append({
            "product_id": card.get("data-id", "").strip(),
            "title": title_el.get_text(strip=True) if title_el else "",
            "author": author_el.get_text(strip=True) if author_el else "",
            "price_uah": float(price_text),
            "stock_status": stock_el.get_text(strip=True) if stock_el else "",
            "relative_url": link_el.get("href", "").strip() if link_el else "",
        })

    visited_urls: set[str] = set()
    pagination_links: list[str] = []
    for link in soup.select(".pagination a.page-link"):
        href = link.get("href", "").strip()
        if href and href not in visited_urls:
            visited_urls.add(href)
            pagination_links.append(href)

    return products, pagination_links


def save_to_csv(products: list[dict[str, object]], csv_path: Path) -> None:
    """Зберігає список словників у CSV-файл у кодуванні UTF-8."""
    fieldnames = [
        "product_id",
        "title",
        "author",
        "price_uah",
        "stock_status",
        "relative_url",
    ]
    with open(csv_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


def main() -> None:
    """Запускає перевірку robots.txt, парсинг каталогу та збереження звіту."""
    html_path = Path("module2_mock_catalog.html")
    csv_path = Path("catalog_scraped.csv")
    report_path = Path("report_scraped.txt")

    ensure_html_file(html_path)

    allowed = check_robots_permission("local://robots.txt", html_path.resolve().as_uri())
    if not allowed:
        print("Доступ заборонено правилами robots.txt")
        return

    products, pagination_links = parse_catalog(html_path)
    save_to_csv(products, csv_path)

    report_lines = [
        f"Зібрано позицій: {len(products)}",
        f"Виявлені лінки пагінації: {pagination_links if pagination_links else 'немає'}",
    ]
    report_text = "\n".join(report_lines)
    report_path.write_text(report_text + "\n", encoding="utf-8")
    print(report_text)


if __name__ == "__main__":
    main()