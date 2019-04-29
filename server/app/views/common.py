from __future__ import division
from flask import Response
from app import app
from flask_cors import CORS
from app.models.database import *
from app.models.set_price import *
from flask_autodoc import Autodoc
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import time
import re
from fake_useragent import UserAgent
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options
import json
import random
from app.common.proxy_rotator import ProxyRotator
CORS(app)
auto = Autodoc(app)

global dollar_price
url = 'http://www.forex.pk/open_market_rates.asp'

opts = Options()
opts.add_argument('--no-sandbox')
opts.add_argument('--headless')
browser = Chrome(options=opts )
#browser = Firefox(firefox_options=opts )
browser.get(url)

price = browser.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[24]/td[3]')
dollar_price = float(price.text)
print dollar_price
browser.close()

@app.route('/')
@auto.doc()
def index_route():
    """
    Index route
    TODO: Need to handle it properly
    :return:
    """
    return '/'

@app.route('/return-link/<sku>', methods=['GET'])
@auto.doc()
def return_product_link(sku):
    print(sku)
    link = get_product_link(sku)[0][0]
    print(link)
    if(link is not None and "amazon" in link):
        opts = Options()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--headless')
        browser = Chrome(options=opts)
        browser.get(link)

        try:
            quantity = None
            select=Select(browser.find_element_by_id("quantity"))
            for opt in select.options:
                quantity=opt.text
                print(quantity)
        except Exception as e:
            print(e)

        price =None
        try:
            availability = browser.find_element_by_xpath('//*[@id="availability"]/span').text
            print(availability)
            price = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text[1:]
            data={'availability':availability, 'price':price, 'quantity':int(quantity)}
            browser.close()
        except Exception as e:
            print(e)
            browser.close()
            data = {'availability':"out of stock", 'price':price, 'quantity':quantity}
        return json.dumps(data)
    elif(link is not None and "ebay" in link):
        opts = Options()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--headless')
        browser = Chrome(options=opts)
        browser.get(link)
        #time.sleep(5)
        soup=BeautifulSoup(browser.page_source, 'lxml')
        try:
            quantity = None
            quantity=soup.find("span",{'id':'qtySubTxt'}).text
	    quantity=re.findall("\d+",quantity)[0]
        except Exception as e:
            print(e)
        price = None
        availability = None
        try:
            availability = soup.find("span",{'id':'qtySubTxt'}).text.strip()
            price = soup.find("span",{'id':"prcIsum"}).text.split('$')[1] or soup.find("span",{'id':"mm-saleDscPrc"}).text.split('$')[1]
            data={'sku':sku, 'availability':availability, 'price':price, 'quantity':int(quantity)}
            browser.close()
        except Exception as e:
            browser.close()
            data = {'availability':"out of stock", 'price':price, 'quantity':quantity}
        return json.dumps(data)
    else:
        data={'availability':None, 'price':None, 'quantity':None}
        return json.dumps(data)


@app.route('/get-color-size/<sku>/<color>/<size>', methods=['GET'])
@auto.doc()
def get_color_size(sku, color, size):
    """
    Returns Stock and price
    """
    print(sku, size, color)
    url = get_url(sku, color, size,)
    print(url)
    user_agent = UserAgent()
    headers = {'User-Agent': str( user_agent.random )}
    #from selenium.webdriver import Firefox
    #from selenium.webdriver.firefox.options import Options
    if(url is not None and "amazon" in url):
        opts = Options()
	rotator = ProxyRotator('/root/Kashif_Server_API/server/app/views/Proxies.txt')
        opts.add_argument('--user-agent= Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
        #opts.add_argument('--proxy-server=104.202.147.26:61336')
	opts.add_argument('--no-sandbox')
        opts.add_argument('--headless')
	opts.add_argument('--proxy-server %s' % rotator.get_proxy())
        browser = Chrome(options=opts)
        browser.get(url)
        time.sleep(5)
	print(browser.title)
        # try:
        #     quantity = None
        #     select=Select(browser.find_element_by_id("quantity"))
        #     for opt in select.options:
        #         quantity=opt.text
        #     print(quantity)
        # except Exception as e:
        #     print(e)
        #     pass

        price = None
        availability = None
        quantity = None
        try:
            availability = browser.find_element_by_xpath('//*[@id="availability"]/span').text
            price = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text[1:]
            if(availability.strip()=='In Stock.'):
                #try:
                select=Select(browser.find_element_by_id("quantity"))
                for opt in select.options:
                    quantity=opt.text
                print(quantity)
                #except Exception as e:
                #print(e)
                data={'sku':sku, 'availability':availability, 'price':price, 'quantity':int(quantity)}
            else:
                quantity=re.findall('\d+',availability)[0]
                data={'sku':sku, 'availability':availability, 'price':price, 'quantity':int(quantity)}
            browser.close()
        except Exception as e:
            browser.close()
            data = {'availability':"out of stock", 'price':price, 'quantity':quantity}
        return json.dumps(data)
    elif(url is not None and "ebay" in url):
        opts = Options()
	rotator = ProxyRotator('/root/Kashif_Server_API/server/app/views/Proxies.txt')
        opts.add_argument('--user-agent= Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--headless')
	opts.add_argument('--proxy-server %s' % rotator.get_proxy())
        browser = Chrome(chrome_options=opts)
        browser.get(url)
        time.sleep(5)
        soup=BeautifulSoup(browser.page_source, 'lxml')
        try:
            quantity = None
            quantity=soup.find("span",{'id':'qtySubTxt'}).text.split()[0]
        except Exception as e:
            print(e)
        price = None
        availability = None
        try:
            availability = soup.find("span",{'id':'qtySubTxt'}).text.split()[1]
            price = soup.find("span",{'id':"prcIsum"}).text.split('$')[1] or soup.find("span",{'id':"mm-saleDscPrc"}).text.split('$')[1]
            data={'sku':sku, 'availability':availability, 'price':price, 'quantity':int(quantity)}
            browser.close()
        except Exception as e:
            browser.close()
            data = {'availability':"out of stock", 'price':price, 'quantity':quantity}
        return json.dumps(data)
    # elif(url is not None and "6pm" in url):
    #     opts = Options()
    #     opts.add_argument('--no-sandbox')
    #     opts.add_argument('--headless')
    #     browser = Chrome(options=opts)
    #     browser.get(url)
    #     time.sleep(5)
    #     soup=BeautifulSoup(browser.page_source, 'lxml')
    #     select=Select(browser.find_element_by_id("pdp-size-select"))
    #     price=None
    #     availability=None
    #     try:
    #         price=soup.find('span',{"class":'_1q0kwWbBMG _3pxa4LdwPN'}).text.split('$')[1]
    #         for opt in select.options:
    #             if(opt.text.strip('')==size):
    #                 select.select_by_visible_text(opt.text)
    #                 time.sleep(2)
    #                 try:
    #                     availability=browser.find_element_by_xpath('//*[@id="productRecap"]/div[7]/div/h1').text
    #                 except Exception as e:
    #                     pass
    #         data={'availability':availability}
    #     except:


    else:
        data={'availability':None, 'price':None, 'quantity':None}
        return json.dumps(data)


@app.route('/ebay_earings/<limit>/<offset>', methods=['GET'])
@auto.doc()
def return_accessories(limit, offset):
    """
    Returns accessories
    """
    return_data = get_ebay_earings(limit, offset)
    set_category_id = '91'
    category_text = 'earing'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


@app.route('/ebay_watches/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_watches(limit, offset):
    return_data = get_ebay_watches(limit, offset)
    set_category_id = '93'
    category_text = 'watches'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


@app.route('/ebay_bracelets/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_bracelets(limit, offset):
    return_data = get_ebay_bracelet(limit, offset)
    set_category_id = '90'
    category_text = 'bracelet'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


@app.route('/ebay_jewelry/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_jewelry(limit, offset):
    return_data = get_ebay_jewelry(limit, offset)
    set_category_id = '92'
    category_text = 'jewelry'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


@app.route('/ebay_handbags/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_handbags(limit, offset):
    return_data = get_ebay_handbags(limit, offset)
    set_category_id = '80'
    category_text = 'handbag'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


@app.route('/ebay_clutches/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_clutches(limit, offset):
    return_data = get_ebay_clutches(limit, offset)
    set_category_id = '81'
    category_text = 'clutches'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


@app.route('/ebay_bagpack/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_bagpack(limit, offset):
    return_data = get_ebay_bagpack(limit, offset)
    set_category_id = '82'
    category_text = 'bagpack'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response

@app.route('/ebay_running/<limit>/<offset>', methods=['GET'])
@auto.doc()
def ebay_running(limit, offset):
    return_data = get_ebay_running(limit, offset)
    print(return_data)
    set_category_id = '85'
    category_text = 'running'
    response = ebay_attributes(return_data, set_category_id, category_text)
    return response


def ebay_attributes(return_data, set_category_id, category_text):
    l1 = []
    weight = shape = gender = size = band_color = case_material = watch_shape = band_material = \
    display = features = jewel_type = metal = color = material = lenght = theme = detatils = \
    strap_drop = bag_length = bag_height = bag_depth = closure = pattern = product_line = \
    shade = texture =  None
    attributes=[]
    for ret_data in return_data: 
        l2=[]
        if ret_data[4] is not None:
            count = 0
            for x in ret_data[4].split(','):
                dict_object = {
                    
                    "src": x,
                    "position": count
                }
                count = count+1
                l2.append(dict_object)
        else:
            dict_object = {
            'src':ret_data[3],
            'position': 0
            }
            l2.append(dict_object)
        if ret_data[2] is not None:
            category=[{
                "id": set_category_id
            }]
        if not ret_data[6] == 'null':
            
            yes = json.loads(ret_data[6])
            for x in yes:
                for k, v in x.items():
                    if k == 'weight':
                        weight = v
                    if k == 'Watch Shape':
                        shape = v
                    if k == 'Gender':
                        gender = v
                    if k == 'Size':
                        size = v
                    if k == 'Band Color':
                        band_color = v
                    if k == 'Case Material':
                        case_material = v
                    if k == 'Watch Shape':
                        watch_shape = v
                    if k == 'Band Material':
                        band_material = v
                    if k == 'Display':
                        display = v
                    if k == 'Features':
                        features = v
                    if k == 'Jewelry Type':
                        jewel_type = v
                    if k == 'Metal':
                        metal = v
                    if k == 'Color':
                        color = v 
                    if k == 'Material':
                        material = v
                    if k == 'Length (inches)':
                        lenght = v
                    if k == 'Theme':
                        theme = v
                    if k == 'Details':
                        detatils = v
                    if k == 'Strap Drop':
                        strap_drop = v
                    if k == 'Bag Height':
                        bag_height = v
                    if k == 'Bag Depth':
                        bag_depth = v
                    if k == 'Closure':
                        closure = v
                    if k == 'Bag Length':
                        bag_length = v
                    if k == 'Pattern':    
                        pattern = v
                    if k == 'Texture':
                        texture = v
                    if k == 'Product Line':
                        product_line = v
                    if k == 'Shade':
                        shade = v

                    if size or color or jewel_type or material:
                        attributes = [{
                            'name': "Size",
                            'visible': True,
                            'options': size
                            },
                            {
                            'name': "Band Color",
                            "visible": True,
                            'options': band_color
                            },
                            {
                            'name': "Case Material",
                            "visible": True,
                            'options': case_material                           
                            },
                            {
                            'name': "Watch Shape",
                            "visible": True,
                            'options': watch_shape
                            },
                            {
                            'name': "Band Material",
                            "visible": True,
                            'options': band_material
                            },
                            {
                            'name': "Display",
                            "visible": True,
                            'options': display
                            },
                            {
                            'name': "Features",
                            "visible": True,
                            'options': features
                            },
                            {
                            'name':'Jewelry Type',
                            'visible':True,
                            'options': jewel_type
                            },
                            {
                            'name':'Metal',
                            'visible':True,
                            'options': metal
                            },
                            {
                            'name':'Color',
                            'visible': True,
                            'options': color
                            },
                            {
                            'name':'Material',
                            'visible':True,
                            'options':  material
                            },
                            {
                            'name': 'Length (inches)',
                            'visible': True,
                            'options': lenght
                            },
                            {
                            'name': 'Theme',
                            'visible': True,
                            'options': theme
                            },{
                            'name': 'Details',
                            'visible': True,
                            'options': detatils
                            },{
                            'name': 'Strap Drop',
                            'visible': True,
                            'options': strap_drop
                            },{
                            'name': 'Bag Height',
                            'visible': True,
                            'options': bag_height
                            },{
                            'name': 'Bag Length',
                            'visible': True,
                            'options': bag_length
                            },{
                            'name': 'Bag Depth',
                            'visible': True,
                            'options': bag_depth
                            },{
                            'name': 'Closure',
                            'visible': True,
                            'options': closure
                            },{
                            'name': 'Pattern',
                            'visible': True,
                            'options': pattern
                            },{
                            'name': 'Texture',
                            'visible': True,
                            'options': texture
                            },{
                            'name': 'Product Line',
                            'visible': True,
                            'options': product_line
                            },{
                            'name': 'Shade',
                            'visible': True,
                            'options': shade
                            }]

        price = ret_data[1]
        if price:
            if ret_data[5]:
                if price > 500:
                    percent_30 = float(price)*0.3
                    price = (float(price)+percent_30) * (dollar_price+3)   
                else:
                    brand = ret_data[5].replace(',', '').lower()
                    price = setting_price(brand, category_text, ret_data[1], dollar_price)
        accessories = {
            "name": ret_data[5],
            "regular_price": str(price),
            "categories": category,
            "image": ret_data[3],
            "brand": ret_data[5],
            "sku": ret_data[7],
            "images": l2,
            "weight": weight,
            "shape": shape,
            "gender": gender,
            "attributes": attributes
        }

        l1.append(accessories)
    response = Response(json.dumps(l1), status=200, mimetype='application/json')
    return response


@app.route('/amazon-sandals/<limit>/<offset>')
@auto.doc()
def amazon_sandals(limit, offset):
    asins = get_product_asin_sandals(int(limit), int(offset))
    category_id = '84'
    category_text = 'sandal'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-running/<limit>/<offset>')
@auto.doc()
def amazon_running(limit, offset):
    asins = get_product_asin_running(limit, offset)
    category_id = '85'
    category_text = 'running'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-sneakers/<limit>/<offset>')
@auto.doc()
def amazon_sneakers(limit, offset):
    asins = get_product_asin_sneakers(limit, offset)
    category_text = 'sneakers'
    category_id = '86'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-training/<limit>/<offset>')
@auto.doc()
def amazon_training(limit, offset):
    asins = get_product_asin_training(limit, offset)
    category_id = '87'
    category_text = 'training'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-flats/<limit>/<offset>')
@auto.doc()
def amazon_flats(limit, offset):
    asins = get_product_asin_flats(limit, offset)
    category_id = '88'
    category_text = 'flat'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-watches/<limit>/<offset>')
@auto.doc()
def amazon_watches(limit, offset):
    asins = get_product_asin_watches(limit, offset)
    category_id = '93'
    category_text = 'watches'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-bracelets/<limit>/<offset>')
@auto.doc()
def amazon_bracelet(limit, offset):
    asins = get_product_asin_bracelet(limit, offset)
    category_id = '90'
    category_text = 'bracelet'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-handbags/<limit>/<offset>')
@auto.doc()
def amazon_handbags(limit, offset):
    asins = get_product_asin_handbags(limit, offset)
    category_id = '80'
    category_text = 'handbags'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-clutches/<limit>/<offset>')
@auto.doc()
def amazon_clutches(limit, offset):
    asins = get_product_asin_clutches(limit, offset)
    category_id = '81'
    category_text = 'clutches'
    response = amazon_attributes(asins, category_id, category_text)
    return response


@app.route('/amazon-bagpack/<limit>/<offset>')
@auto.doc()
def amazon_bagpack(limit, offset):
    asins = get_product_asin_bagpack(limit, offset)
    category_id = '82'
    category_text = 'bagpack'
    response = amazon_attributes(asins, category_id, category_text)
    return response


def amazon_attributes(asins, category_id, category_text):
    all_data=[]
    description1=[]
    description2=[]
    for asin in asins:
        variation_list=[]
        size_list=[]
        color_list=[]
        data_against_main_asin = get_product_against_main_asin(asin[0])
        
        for single_row in data_against_main_asin:    
            # making variations in desired format
            price = single_row[1]
            if price:
                if single_row[3]:
                    if price > 500:
                        percent_30 = float(price) * 0.3
                        price = (percent_30 + float(price)) * (dollar_price + 3)
                    else:
                        brand = single_row[3].replace(',', '').lower()
                        price = setting_price(brand, category_text, single_row[1], dollar_price)
                        if not price:
                            price = float(single_row[1]) * (dollar_price+3)
            if single_row[1] or single_row[4]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': single_row[4] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':single_row[2]},
                    			{'slug':'size', 'name':"Size", 'option':single_row[6]}]
                }
                variation_list.append(variation)
            
            if single_row[6]:
                size_list.append(single_row[6])
            if single_row[2]:
                color_list.append(single_row[2])
            if single_row[8]:
                description1 = single_row[8].replace('{', '').replace('}','').replace('"', '')
            if single_row[9]:
                description2 = single_row[9].replace('{', '').replace('}', '').replace('"', '') 
            
            #change all images accroding to "woocomerece extension"
            image_list=[]
            if single_row[7] is not None:
                count = 0
                for x in single_row[7].split(','):
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                    count = count+1
                    image_list.append(dict_object)

        color_list = list(set(color_list))
        size_list = list(set(size_list))
        
        attributes = [{
                'name': "Color",
                "visible": True,
                "variation": True,
                "options": color_list

            },
            {
                'name': "Size",
                "visible": True,
                "variation": True,
                "options": size_list                
            }]
        data = {
            'sku': asin[0],
            'type': 'variable',
            'name': single_row[0],
            'variations': variation_list,
            'brand': single_row[3],
            'attributes': attributes,
            'images': image_list,
            'categories':[{ "id": category_id}],
            'short_description': description1,
            'description': description2
            }

        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/shopspring/<limit>/<offset>')
@auto.doc()
def shopspring_data(limit, offset):
    all_rows = get_all_data_of_shopspring(limit,offset)
    all_data=[]
    for row in all_rows:
        
        #setting up images
        l2=[]
        if row[7] is not None:
            count = 0
            for x in row[7].split(','):
                dict_object = {
                    
                    "src": x,
                    "position": count
                }
                count = count+1
                l2.append(dict_object)
        else:
            dict_object = {
            'src':row[9],
            'position': 0
            }
            l2.append(dict_object)
        
        attributes = [{
                'name': "Color",
                "visible": True,
                "variation": True,
                "options": row[3]

            },
            {
                'name': "Size",
                "visible": True,
                "variation": True,
                "options": row[6]                
            }]

        price = row[2]
        print price
        if price:
            if row[8]:
                if price > 500:
                    percent_30 = float(price) * 0.3
                    price = (percent_30 + price) * (dollar_price + 3)
                else:
                    brand = row[8].replace(',', '').lower()
                    price = setting_price(brand, row[10], row[2], dollar_price)
                    if not price:
                        price = float(row[2]) * (dollar_price+3)
        category_id = assign_category(row[10])

        data = {
            'sku': row[0],
            'type': 'variable',
            'regular_price': str(price),
            'name': row[1],
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/zara')
@auto.doc()
def zara_data():
    all_rows = get_all_data_of_zara()
    all_data=[]
    brand = 'zara'
    for row in all_rows:
        
        #setting up images
        l2=[]
        if row[7] is not None:
            count = 0
            for x in row[7].split(','):
                dict_object = {
                    
                    "src": x,
                    "position": count
                }
                count = count+1
                l2.append(dict_object)
        else:
            dict_object = {
            'src':row[9],
            'position': 0
            }
            l2.append(dict_object)
        
        attributes = [{
                'name': "Color",
                "visible": True,
                "variation": True,
                "options": row[3]

            },
            {
                'name': "Size",
                "visible": True,
                "variation": True,
                "options": row[6]                
            }]

        price = row[2]
        print price
        if price:
            if price > 500:
                percent_30 = float(price) * 0.3
                price = (percent_30 + price) * (dollar_price + 3)
            else:
                price = setting_price(brand, row[10], row[2], dollar_price)
                if not price:
                    price = float(row[2]) * (dollar_price+3)
        category_id = assign_category(row[10])

        data = {
            'sku': row[0],
            #'type': 'variable',
            'regular_price': str(price),
            'name': row[1],
            'brand': 'zara',
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/macys')
@auto.doc()
def macys_data():
    all_rows = get_all_data_of_macys()
    all_data=[]
    for row in all_rows:
        #setting up images
        l2=[]
        if row[7] is not None:
            count = 0
            for x in row[7].split('","'):
                if "{" in x:
                    dict_object = {
                        
                        "src": x.split('{')[1][1:],
                        "position": count
                    }
                elif "}" in x:
                    dict_object = {
                        
                        "src": x.split('}')[0][:-1],
                        "position": count
                    }
                else:
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                count = count+1
                l2.append(dict_object)
        else:
            dict_object = {
            'src':row[9],
            'positsion': 0
            }
            l2.append(dict_object)
        
        attributes = [{
                'name': "Color",
                "visible": True,
                "variation": True,
                "options": row[3]

            },
            {
                'name': "Size",
                "visible": True,
                "variation": True,
                "options": row[6]                
            }
            ]
        price = ""
        if row[2]:
            db_price = float(row[2])
        elif row[11]:
            db_price = float(row[11])
        #print(db_price)
        if db_price > 500:
            percent_30 = db_price * 0.3
            price = (percent_30 + db_price) * (dollar_price + 3)
        elif row[8]:
            brand = row[8].replace(',', '').lower()
            price = setting_price(brand, row[10], db_price, dollar_price)
            if not price:
                price = float(db_price) * (dollar_price+3)
        
        category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': row[0],
            #'type': 'variable',
            'regular_price': str(price),
            'name': row[1],
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/6pm')
@auto.doc()
def pm6_data():
    all_asin = get_all_main_asin_of_6pm()
    all_data=[]
    for asin in all_asin:
        all_rows = get_data_against_asin_6pm(asin[0])
        print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(' ,'):
                    if "{" in x:
                        dict_object = {
                            
                            "src": x.split('{')[1],
                            "position": count
                        }
                    elif "}" in x:
                        dict_object = {
                            
                            "src": x.split('}')[0],
                            "position": count
                        }
                    else:
                        dict_object = {
                            
                            "src": x.split(' ')[1],
                            "position": count
                        }

                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6][0]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[9]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[9] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/zappos')
@auto.doc()
def zappos_data():
    all_asin = get_all_main_asin_of_zappos()
    all_data=[]
    for asin in all_asin:
        #print(asin)
        #print(asin[0])
        all_rows = get_data_against_asin_zappos(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[7]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[7] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response
@app.route('/aldoshoes')
@auto.doc()
def aldoshoes_data():
    all_asin = get_all_main_asin_of_aldoshoes()
    all_data=[]
    #print all_asin
    for asin in all_asin:
        #print(asin)
        #print(asin[0])
        all_rows = get_data_against_asin_aldoshoes(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[7]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[7] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/tedbaker')
@auto.doc()
def tedbaker_data():
    all_asin = get_all_main_asin_of_tedbaker()
    all_data=[]
    #print all_asin
    for asin in all_asin:
        #print(asin)
        #print(asin[0])
        all_rows = get_data_against_asin_tedbaker(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[7]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[7] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/katespade')
@auto.doc()
def katespade_data():
    all_asin = get_all_main_asin_of_katespade()
    all_data=[]
    #print all_asin
    for asin in all_asin:
        #print(asin)
        #print(asin[0])
        all_rows = get_data_against_asin_katespade(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[7]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[7] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/michaelkors')
@auto.doc()
def michaelkors_data():
    all_asin = get_all_main_asin_of_michaelkors()
    all_data=[]
    #print all_asin
    for asin in all_asin:
        #print(asin)
        #print(asin[0])
        all_rows = get_data_against_asin_michaelkors(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    dict_object = {
                        
                        "src": x,
                        "position": count
                    }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[7]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[7] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/nordstromrack')
@auto.doc()
def nordstromrack_data():
    all_asin = get_all_main_asin_of_nordstromrck()
    all_data=[]
    #print all_asin
    for asin in all_asin:
        #print(asin)
        #print(asin[0])
        all_rows = get_data_against_asin_nordstromrack(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    if "{" in x:
                        dict_object = {
                            
                            "src": x.split('{')[1].split('}')[0],
                            "position": count
                        }
                    elif "}" in x:
                        dict_object = {
                            
                            "src": x.split('}')[0],
                            "position": count
                        }
                    else:
                        dict_object = {
                            
                            "src": x,
                            "position": count
                        }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[9]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[9] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0],
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

@app.route('/shopguess')
@auto.doc()
def shopguess_data():
    all_asin = get_all_main_asin_of_shopguess()
    all_data=[]
    print all_asin
    for asin in all_asin:
        print(asin)
        print(asin[0].strip())
        all_rows = get_data_against_asin_shopguess(asin[0])
        #print all_rows
        variation_list=[]
        for row in all_rows:
            l2=[]
            # setting up images
            if row[7] is not None:
                count = 0
                for x in row[7].split(','):
                    if "{" in x:
                        dict_object = {
                            
                            "src": x.split('{')[1],
                            "position": count
                        }
                    elif "}" in x:
                        dict_object = {
                            
                            "src": x.split('}')[0],
                            "position": count
                        }
                    else:
                        dict_object = {
                            
                            "src": x,
                            "position": count
                        }
                    count = count+1
                    l2.append(dict_object)
            else:
                dict_object = {
                'src':row[9],
                'position': 0
                }
                l2.append(dict_object)
            # setting up properties or attributes
            attributes = [{
                    'name': "Color",
                    "visible": True,
                    "variation": True,
                    "options": row[3]

                },
                {
                    'name': "Size",
                    "visible": True,
                    "variation": True,
                    "options": row[6]                
                }
                ]
            price = ""
            if row[2]:
                db_price = float(row[2])
            elif row[11]:
                db_price = float(row[11])
            if db_price > 500:
                percent_30 = db_price * 0.3
                price = (percent_30 + db_price) * (dollar_price + 3)
            elif row[8]:
                brand = row[8].replace(',', '').lower()
                price = setting_price(brand, row[10], db_price, dollar_price)
                if not price:
                    price = float(db_price) * (dollar_price+3)
            
            if price or row[9]: 
                variation = {
                    "regular_price": str(price),
                    "image":{ 'src': row[9] },
                    'attributes':[{'slug':'color', 'name':"Color", 'option':row[3]}]
                }
                variation_list.append(variation)

            category_id = assign_category(row[10].split(' ')[0])
        data = {
            'sku': asin[0].strip(),
            #'type': 'variable',
            'name': row[1],
            'variations': variation_list,
            'brand': row[8],
            'attributes': attributes,
            'images': l2,
            'categories':[{ "id": category_id}],
            'description': row[5]
            }        
        all_data.append(data)
    response = Response(json.dumps(all_data), status=200, mimetype='application/json')
    return response

def assign_category(category_text):
    category_id = 0
    if  'tshirt' in category_text:
        category_id = 150
    elif 'jeans' in category_text :
        category_id = 149
    elif 'handbag' in category_text :
        category_id = 80
    elif 'clutches' in category_text:
        category_id = 81
    elif 'bagpack' in category_text:
        category_id = 82
    elif 'bracelet' in category_text:
        category_id = 90
    elif 'earing' in category_text:
        category_id = 91
    elif 'jewelry' in category_text:
        category_id = 92
    elif 'watches' in category_text:
        category_id = 93
    elif 'sandal' in category_text:
        category_id = 84
    elif 'running' in category_text:
        category_id = 85
    elif 'sneaker' in category_text:
        category_id = 86
    elif 'training' in category_text:
        category_id = 87
    elif 'flat' in category_text:
        category_id = 88    
    return category_id


@app.route('/docs')
def return_api_docs():
    """
    api docs route
    :return:
    """
    return auto.html()
