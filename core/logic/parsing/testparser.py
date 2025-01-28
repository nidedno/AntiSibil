import asyncio
import nodriver as uc
import inspect

NAME = '''//*[@id="__next"]/div/div/main/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/text()'''
TICKET = '''//*[@id="__next"]/div/div/main/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/p'''
MCAP = '''//div[text()="MKT Cap"]/following-sibling::div'''
LIUQ = '''//div[text()="Liq"]/following-sibling::div'''
HOLDERS = '''//div[text()="Holders"]/following-sibling::div'''
VOLUME = '''//div[text()="24h Vol"]/following-sibling::div'''

async def get_elements(page, **elements):
    # Получаем локальные переменные из вызывающего контекста
    page_results = {}
    for name, xpath in elements.items():
        result = await page.evaluate(get_element_by_xpath(xpath))
        page_results[name] = result
    return page_results

def get_element_by_xpath(path):
    return "document.evaluate('{0}', document, null, XPathResult.STRING_TYPE, null).stringValue".format(path)

async def gmgn_sol(token):
    browser = await uc.start(
        headless=True, # switch to headles.
        browser_args=["--disable-blink-features=AutomationControlled", "--user-agen=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"]
    )

    result = {}

    # page = await browser.get("https://www.google.com/")
    page = await browser.get('https://gmgn.ai/sol/token/{0}'.format(token))
    # await page
    # wait for banner
    await page.wait_for(".chakra-portal div div")
    
    # name = await page.evaluate(get_element_by_xpath(NAME))
    # result['name'] = name

    # ticket = await page.evaluate(get_element_by_xpath(TICKET))
    # result['ticket'] = ticket

    # # #print(get_element_by_xpath(MCAP), 'mcap')
    # mcap = await page.evaluate(get_element_by_xpath(MCAP))
    # result['mcap']  = mcap

    # liuq = await page.evaluate(get_element_by_xpath(LIUQ))
    # result['liq'] = liuq
    
    # holders = await page.evaluate(get_element_by_xpath(HOLDERS))
    # result['holders'] = holders

    result = await get_elements(page, name=NAME, ticket=TICKET, mcap=MCAP, liq=LIUQ, holder=HOLDERS, vol=VOLUME)
    # await page.sleep(10)
    # await page.sleep(10)
    # elems = await page.select_all('*[src]')
    # for elem in elems:
    #     await elem.flash()

    #page2 = await browser.get('https://twitter.com', new_tab=True)
    #page3 = await browser.get('https://github.com/ultrafunkamsterdam/nodriver', new_window=True)

    # for p in (page, page2, page3):
    #    await p.bring_to_front()
    #    await p.scroll_down(200)
    #    await p   # wait for events to be processed
    #    await p.reload()
    #    if p != page3:
    #        await p.close()
    #print(result)
    return result

if __name__ == '__main__':
    # since asyncio.run never worked (for me)
    uc.loop().run_until_complete(main())
    #asyncio.run(main())