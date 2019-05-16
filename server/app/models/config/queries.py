QUERIES = {
    "GetEarings": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='162' LIMIT %s OFFSET %s",

    "GetLink": "SELECT product_link FROM shopify_db.amazon_products_details "
               "WHERE main_product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.ebay_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.dillards_scraped_data "
               "WHERE main_asin=%s "
               "UNION SELECT product_link FROM shopify_db.macys_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.pm6_scraped_data "
               "WHERE main_asin=%s "
               "UNION SELECT product_link FROM shopify_db.spring_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.zappos_scraped_data "
               "WHERE main_asin=%s "
               "UNION SELECT product_link FROM shopify_db.zara_scraped_data "
               "WHERE product_asin=%s ",
               "UNION SELECT product_link FROM shopify_db.ashford_data WHERE product_asin=%s",

    "GetWatches": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='watches' "
                      "LIMIT %s OFFSET %s",

    "GetBracelet": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='161' "
                      "LIMIT %s OFFSET %s ",

    "GetJewelry": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='163' "
                      "LIMIT %s OFFSET %s",

    "GetHandbags": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='handbags' "
                      "LIMIT %s OFFSET %s",

    "GetClutches": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM shopify_db.ebay_scraped_data where category='clutches' "
                      "LIMIT %s OFFSET %s",

    "GetBagpack": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='bagpacks' "
                      "LIMIT %s OFFSET %s",

    "GetRunning": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='running' "
                      "LIMIT %s OFFSET %s",
    
    "GetMainProductAsinSandals": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                      "WHERE category='sandals' OR category='sandal' "
                      "LIMIT %s OFFSET %s",

    "GetDataAgainstAsin": "SELECT title, price, color, brand, image_link, category, product_size, "
                          "all_images_links, description1, description2 "
                          "FROM shopify_db.amazon_products_details "
                          "WHERE main_product_asin=%s",

    "GetMainProductAsinRunnings": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                          "WHERE category='running' LIMIT %s OFFSET %s",

    "GetMainProductAsinFlats": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                          "WHERE category='flat' LIMIT %s OFFSET %s",

    "GetMainProductAsinSneakers": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                          "WHERE category='sneaker' LIMIT %s OFFSET %s",


    "GetMainProductAsinTrainings": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                              "WHERE category='training' LIMIT %s OFFSET %s",

    "GetMainProductAsinBracelets": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='bracelet' LIMIT %s OFFSET %s",

    "GetMainProductAsinWatches": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                              "WHERE category='watches' LIMIT %s OFFSET %s",

    "GetMainProductAsinHandbags": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                              "WHERE category='handbags' LIMIT %s OFFSET %s",

    "GetMainProductAsinClutches": "SELECT DISTINCT(main_product_asin) FROM shopify_db.amazon_products_details "
                              "WHERE category='clutches' OR category='cultches' LIMIT %s OFFSET %s",

    "GetMainProductAsinBagpacks": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='bagpacks' LIMIT %s OFFSET %s",

    "GetShopSpringData": "SELECT  product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_links, brand_name, image_link, category " 
      "FROM shopify_db.spring_scraped_data LIMIT %s OFFSET %s",

    "ZaraData": "SELECT  product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_links, title, image_link, category " 
      "FROM shopify_db.zara_scraped_data",

    "MacysData": "SELECT  product_asin, title, new_price, color, category, " 
      "production_descr, allsizes, allimages_link, brand_name, image_link, category, old_price " 
      "FROM shopify_db.macys_scraped_data",

    "DillardsMainAsinData": "SELECT DISTINCT(main_asin) from shopify_db.dillards_scraped_data",

    "DillardsData": "SELECT product_asin, title, new_price, color, category, " 
      "product_descr, allsizes, allimages_link, brand_name, image_link, category, old_price " 
      "FROM shopify_db.dillards_scraped_data where main_asin=%s",

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
      "FROM shopify_db.shop_guess_scraped_data where main_asin=%s",

    "GetUrl": "SELECT product_link from shopify_db.amazon_products_details "
          "where  main_product_asin=%s and color=%s and  product_size=%s"
          "UNION SELECT product_link from shopify_db.ebay_scraped_data where product_asin=%s "
          "UNION SELECT product_link from shopify_db.zappos_scraped_data where main_asin=%s and color=%s "
          "UNION SELECT product_link from shopify_db.pm6_scraped_data where main_asin=%s and color=%s "
          "UNION SELECT product_link from shopify_db.dillards_scraped_data where main_asin=%s and color=%s",


    # "GetEbayUrl": "SELECT product_link from shopify_db.ebay_scraped_data "
    #         "where main_product_asin=%s and color=%s and  product_size=%s"


    "AshfordData": "SELECT * FROM shopify_db.ashford_data;",

    "ToryBurchData": "SELECT * FROM shopify_db.tory_burch_data;"

}
