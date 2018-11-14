import os, sys
import requests
import math

def setting_price(brand, category, price , dollar_price):
	brand_list_1=['gucci', 'chanel', 'prada', 'christian dior', 'dolce&gabbana', 
	'versace', 'tag', 'tag heuer', 'dior', 'versace collection', 'burberry', 'jimmy choo', 
	'ysl', 'hublot', 'patek philippe', 'audemars piguet', 'louis vuitton', 'saint laurent',
	'mega','bvlgari', 'juicy couture', 'rolex', 'breitling', 'fendi', 'valentino', 
	'red valentino', 'dolce & gabbana']

	brand_list_2=['michael kors', 'michael michael kors', 'michaell michael', 'tory burch', 'coach', 
	'kate spade new york', 'kate spade', 'cole haan', 'lauren ralph lauren', 'ralph lauren', 
	'ted baker', 'emporio armani', 'diesel', 'givenchy', 'juicy couture', 'dune', 
	'lauren by ralph lauren', 'polol ralph lauren', 'calvin', 'salvatore ferragamo', 'ferragamo']

	brand_list_3=['dkny', 'r.guess', 'guess', 'gbyguess', 'clarks', 'tommy hilfiger', 'lacoste', 
	'marc jacobs', 'tommy bahama', 'calvin klein', 'armani exchange', 'gigi', 
	'french connection', 'marc by marc jacobs', 'mbm1315 marc', 'mk5970 michael']

	brand_list_4=['skechers', 'nike', 'puma', 'converse', 'reebok', 'toms', 'asics', 'bobs', 
	'under armour', 'disney', 'kenneth cole', 'kenneth', 'cole', 'columbia', 'nine west', 
	'original', 'alice', 'bubbles', 'fossil', 'nine', 'vail', 'marvel', 'womens']

	brand_list_5=['toms', 'aldo', 'crocs', 'zara', 'levis', 'american apparel', 
	'steve madden', 'steve', 'anne klein', 'anne', 'jessica simpson', 'u.s. polo assn', 'h&m', 
	'forever 21', 'gap', 'logo', 'genuine', 'jessica', 'muppets', 'walt']

	brand_list_6=['nyx', 'loreal', 'maybelline', 'maybelline174', 'benefit', 'too faced',
	 'e.l.f', 'n.y.c', 'baby', 'elf', 'neutrogena', 'precisely', 'star', 'ka-brow!',
	 'lorealcolour', 'shiseido', 'covergirl', 'colorburst', 'lip', 'victoria', 'revlon', 
	 'loreal', 'coral', 'loreal paris', 'victorias', 'victorias secret', 'vicrtorias',
	 'maybellline', 'anastasia beverly hills', 'butter london']


	dollar_price = dollar_price + 3

	if 'flat' in category :
		if brand in brand_list_1:
			pkr_price = float(price) * dollar_price+7000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price) * dollar_price+4500
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+4000
			return math.ceil(pkr_price)
		elif brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+3500
			return math.ceil(pkr_price)

	elif 'running' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+8000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)
		elif brand in brand_list_3 or brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+4500
			return math.ceil(pkr_price)

	elif 'sandal' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+8000
			return math.ceil(pkr_price)
		elif brand in brand_list_2 or brand in brand_list_3:
			pkr_price = float(price)*dollar_price+4500
			return math.ceil(pkr_price)
		elif brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+4000
			return math.ceil(pkr_price)

	elif 'sneaker' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+8000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+5500
			return math.ceil(pkr_price)
		elif brand in brand_list_3 or brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)

	elif 'training' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+8000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+5500
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)
		elif brand in brand_list_4:
			pkr_price = float(price)*dollar_price+4500
			return math.ceil(pkr_price)
		elif brand in brand_list_5:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)

	elif 'handbag' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+15000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+12000
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+8500
			return math.ceil(pkr_price)
		elif brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+7500
			return math.ceil(pkr_price)

	elif 'clutches' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+9000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+7000
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+6000
			return math.ceil(pkr_price)
		elif brand in brand_list_4:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)
		elif brand in brand_list_5:
			pkr_price = float(price)*dollar_price+4500
			return math.ceil(pkr_price)

	elif 'bagpack' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+15000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = (float(price) * dollar_price) + 11000
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+9000
			return math.ceil(pkr_price)
		elif brand in brand_list_4:
			pkr_price = float(price)*dollar_price+8000
			return math.ceil(pkr_price)
		elif brand in brand_list_5:
			pkr_price = float(price)*dollar_price+7000
			return math.ceil(pkr_price)

	elif 'tshirt' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+4000
			return math.ceil(pkr_price)
		elif brand in brand_list_3 or brand in brand_list_4:
			pkr_price = float(price)*dollar_price+3500
			return math.ceil(pkr_price)
		elif brand in brand_list_5:
			pkr_price = float(price)*dollar_price+3200
			return math.ceil(pkr_price)

	elif 'jean' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+4500
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+4000
			return math.ceil(pkr_price)
		elif brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+3500
			return math.ceil(pkr_price)

	elif 'watches' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+10000
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+6500
			return math.ceil(pkr_price)
		elif brand in brand_list_3:
			pkr_price = float(price)*dollar_price+5500
			return math.ceil(pkr_price)
		elif brand in brand_list_4 or brand in brand_list_5:
			pkr_price = float(price)*dollar_price+5000
			return math.ceil(pkr_price)

	elif 'earing' in category or 'bracelet' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+7500
			return math.ceil(pkr_price)
		elif brand in brand_list_2:
			pkr_price = float(price)*dollar_price+4000
			return math.ceil(pkr_price)
		elif brand in brand_list_3 or brand in brand_list_4:
			pkr_price = float(price)*dollar_price+3500
			return math.ceil(pkr_price)
		elif brand in brand_list_5:
			pkr_price = float(price)*dollar_price+3000
			return math.ceil(pkr_price)

	elif 'jewelry' in category:
		if brand in brand_list_1:
			pkr_price = float(price)*dollar_price+7500
			return math.ceil(pkr_price)
		elif brand in brand_list_2 or brand in brand_list_3 or brand in brand_list_4:
			pkr_price = float(price)*dollar_price+3500
			return math.ceil(pkr_price)
		elif brand in brand_list_5:
			pkr_price = float(price)*dollar_price+3000
			return math.ceil(pkr_price)

	elif 'eyes' in category or 'lips' in category or 'face' in category:
		if brand in brand_list_6:
			pkr_price = float(price)*dollar_price+2500
			return math.ceil(pkr_price)

	elif 'brushes_and_tools' in category:
		if brand in brand_list_6:
			pkr_price = float(price)*dollar_price+3000
			return math.ceil(pkr_price)