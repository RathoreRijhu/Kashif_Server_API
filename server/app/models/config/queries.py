QUERIES = {
    "GetEarings": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='162' limit 60",

    "GetLink": "SELECT product_link FROM public.sorted_amazon_products_details "
               "WHERE main_product_asin=%s "
               "UNION SELECT product_link FROM public.sorted_ebay_scraped_data "
               "WHERE product_asin=%s limit 1",

    "GetWatches": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='watches'",

    "GetBracelet": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='161' ",

    "GetJewelry": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='163' ",

    "GetHandbags": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='handbags' ",

    "GetClutches": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='clutches' ",

    "GetBagpack": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='bagpacks' ",

    "GetRunning": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM public.sorted_ebay_scraped_data where category='running' ",
    
    "GetMainProductAsinSandals": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                                  "WHERE category='sandals' OR category='sandal' "       ,

    "GetDataAgainstAsin": "SELECT title, price, color, brand, image_link, category, product_size, "
                          "all_images_links, description1, description2 "
                          "FROM public.sorted_amazon_products_details "
                          "WHERE main_product_asin=%s",

    "GetMainProductAsinRunnings": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                          "WHERE category='running'",

    "GetMainProductAsinFlats": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                          "WHERE category='flat'",

    "GetMainProductAsinSneakers": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                          "WHERE category='sneaker'",


    "GetMainProductAsinTrainings": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                              "WHERE category='training'",

    "GetMainProductAsinBracelets": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                              "WHERE category='bracelet'",

    "GetMainProductAsinWatches": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                              "WHERE category='watches' LIMIT %s OFFSET %s",

    "GetMainProductAsinHandbags": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                              "WHERE category='handbags'",

    "GetMainProductAsinClutches": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                              "WHERE category='clutches' OR category='cultches'",

    "GetMainProductAsinBagpacks": "SELECT DISTINCT(main_product_asin) FROM public.sorted_amazon_products_details "
                              "WHERE category='bagpacks'",

    "GetShopSpringData": "SELECT  product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_links, brand_name, image_link, category " 
      "FROM shopify_db.spring_scraped_data",

    "ZaraData": "SELECT  product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_links, title, image_link, category " 
      "FROM shopify_db.zara_scraped_data",

    "MacysData": "SELECT  product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price " 
      "FROM shopify_db.macys_scraped_data",

    "DillardsData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price " 
      "FROM shopify_db.dillards_scraped_data",

    "6PmDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.pm6_scraped_data",

    "6PmData": "SELECT product_asin, title, new_price, color, category, " 
      "product_descr, allsizes, allimages_link, brand_name, image_link, category, old_price " 
      "FROM shopify_db.pm6_scraped_data where main_asin=%s",  

    "ZapposDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.zappos_scraped_data",

    "ZapposData": "SELECT product_asin, title, new_price, color, category, " 
      "product_descr, allsizes, allimages_link, brand_name, image_link, category, old_price, total_reviews " 
      "FROM shopify_db.zappos_scraped_data where main_asin=%s",

    "AldoDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.aldo_shoes_data",

    "AldoData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price, total_reviews " 
      "FROM shopify_db.aldo_shoes_data where main_asin=%s",

    "TedbakerDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.tedbaker_data",

    "TedbakerData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price, total_reviews " 
      "FROM shopify_db.tedbaker_data where main_asin=%s",

    "KatespadeDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.katespade_data",
    "KatespadeData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price, total_reviews " 
      "FROM shopify_db.katespade_data where main_asin=%s",

    "MichaelkorsDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.michael_products_details",
    "MichaelkorsData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price, total_reviews " 
      "FROM shopify_db.michael_products_details where main_asin=%s",

    "NordstromrackDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.nordstromrack_scraped_data",
    "NordstromrackData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price, total_reviews " 
      "FROM shopify_db.nordstromrack_scraped_data where main_asin=%s",
      
    "ShopguessDataAsin": "SELECT DISTINCT(main_asin) from shopify_db.shop_guess_scraped_data",
    "ShopguessData": "SELECT product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price " 
      "FROM shopify_db.shop_guess_scraped_data where main_asin=%s"




}