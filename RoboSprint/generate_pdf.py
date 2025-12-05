import asyncio
from playwright.async_api import async_playwright
import os

async def generate_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, 'index.html')
    pdf_path = os.path.join(base_dir, 'RoboSprint_Technical_Report.pdf')
    
    file_url = 'file:///' + html_path.replace('\\', '/')
    
    print(f"Converting HTML to PDF...")
    print(f"Source: {html_path}")
    print(f"Output: {pdf_path}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto(file_url, wait_until='networkidle')
        await page.wait_for_timeout(3000)
        
        await page.pdf(
            path=pdf_path,
            format='A4',
            print_background=True,
            display_header_footer=False,
            prefer_css_page_size=True,
            margin={
                'top': '15mm',
                'right': '15mm',
                'bottom': '15mm',
                'left': '15mm'
            }
        )
        
        await browser.close()
    
    file_size = os.path.getsize(pdf_path) / (1024*1024)
    print(f"\n✅ PDF generated successfully!")
    print(f"📄 File saved to: {pdf_path}")
    print(f"📏 File size: {file_size:.1f} MB")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
