from openpyxl import Workbook
import pandas as pd
import requests

wb = Workbook()
ws = wb.active


cookie = "_gcl_au=1.1.521922636.1706679984; _fbp=fb.1.1706679988441.575132951; BVBRANDID=48829252-2d8f-4a5a-a583-e4783d338dcf; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; __stripe_mid=dd8bfc00-c656-4337-999c-dff73174b742cb83d4; loyaltyID=null; _gid=GA1.2.691434059.1708408208; dotcomSearchId=55d69e5e-b994-4c64-9ab8-a87ae6da13b5; __cf_bm=.lD7VF42e64ir1HRjMyTjtF4B_WXagcT.ItF77bm6QU-1708495044-1.0-AWQMeUddhw77QBWwQlXByZ/dm5hh/uaWV3dthJROT0Qgo14obIW07cAmsFKZJaXnqsNNWikBlcSVakQnGWocPGc=; _gat_UA-47434162-1=1; BVBRANDSID=30c34d82-9464-4b09-9ef2-431422630cab; __stripe_sid=c41fbb19-29a5-4234-bd76-6063bf2f80e6f4c445; session-sprouts=.eJwdjk1vgjAAQP9Lz8ZABzq4oSykDMrEKtgL4aOMQq2GggrL_vvIDu_yLu_9gKzumWqAXedCsRXI7qy_5pLJAdhDPy5GMaX4TWbDrWMS2IBNflN4JY-4j04z0jH3rfUi9RKep4W5hOJRCOtO92iD2nNHScwx_IABcQxKwgG7VNC9Zlxg3AQEzaEbN7g96NR1IJ6QQvI809Sv8-TAoxZpeHZeETktoSe_JPGQJ-Z_K4WiQ-19rJKXCvbL1NUaWaI_qjTkkYynKjkpdBVNtXyEpHzi9vIWkc4Mpbb2vm91J4wUVo1n7Mz3Ypic7TEP07iwgk-n6MZ8N4mvoyUUWIFRsT7jFbChsdV0yzQ3v3_DJmlP.GLciaw.f-khekhFNesjsS6Nwg1J0zLvAFg; _ga=GA1.2.853090590.1706679987; _uetsid=e69c7400cfb311ee9882f5d79f096d43; _uetvid=14be1f60bffc11eea5691fbf32dcaa28; _ga_LPZ816BHL5=GS1.1.1708495060.21.1.1708495084.36.0.0; _dd_s=rum=0&expire=1708495985712"
HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
    'Cookie': cookie    
}
    
url = "https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=false&search_provider=ic&search_term=apple&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"
responses = requests.get(url,headers=HEADERS)
print(responses.status_code)
data = responses.json()
items = data.get('items')

df_items = pd.DataFrame(items)
# print(df_items)
df_clean = df_items[['name','base_price']]
# df_clean.to_excel("scrap_ploting.xlsx",index=False)


for index, row in df_clean.iterrows():
    ws.append([row['name'], row['base_price']])
    
wb.save('scrap_ploting_workbook.xlsx')