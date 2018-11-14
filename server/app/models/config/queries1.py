QUERIES = {
    "GetEarings": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='162' "
                      "LIMIT %s OFFSET %s",

    "GetLink": "SELECT product_link FROM sorted_db.sorted_amazon_products_details "
               "WHERE main_product_asin=%s "
               "UNION SELECT product_link FROM sorted_db.sorted_ebay_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.dillards_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.macys_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.pm6_scraped_data "
               "WHERE main_asin=%s "
               "UNION SELECT product_link FROM shopify_db.spring_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.zappos_scraped_data "
               "WHERE product_asin=%s "
               "UNION SELECT product_link FROM shopify_db.zara_scraped_data "
               "WHERE product_asin=%s",

    "GetWatches": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='164' "
                      "LIMIT %s OFFSET %s",

    "GetBracelet": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='161' "
                      "LIMIT %s OFFSET %s",

    "GetJewelry": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='163' "
                      "LIMIT %s OFFSET %s",

    "GetHandbags": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='handbags' "
                      "LIMIT %s OFFSET %s",

    "GetClutches": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='handbags' "
                      "LIMIT %s OFFSET %s",

    "GetBagpack": "SELECT title, price, category, image_link, all_images, brand, item_specification, product_asin "
                      "FROM sorted_db.sorted_ebay_scraped_data where category='handbags' "
                      "LIMIT %s OFFSET %s",
    
    "GetMainProductAsinSandals": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                                  "WHERE category='sandals' OR category='sandal' "
                                  "LIMIT %s OFFSET %s"       ,

    "GetDataAgainstAsin": "SELECT title, price, color, brand, image_link, category, product_size, "
                          "all_images_links, description1, description2 "
                          "FROM sorted_db.sorted_amazon_products_details "
                          "WHERE main_product_asin=%s",

    "GetMainProductAsinRunnings": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                          "WHERE category='running' LIMIT %s OFFSET %s",

    "GetMainProductAsinFlats": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                          "WHERE category='flat' LIMIT %s OFFSET %s",

    "GetMainProductAsinSneakers": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                          "WHERE category='sneaker' or category = 'sneakers' "
                          "LIMIT %s OFFSET %s",

    "GetMainProductAsinTrainings": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='training' LIMIT %s OFFSET %s",

    "GetMainProductAsinBracelets": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='bracelet' LIMIT %s OFFSET %s",

    "GetMainProductAsinWatches": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='watches' LIMIT %s OFFSET %s",

    "GetMainProductAsinHandbags": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='handbags' LIMIT %s OFFSET %s",

    "GetMainProductAsinClutches": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='clutches' OR category='cultches' "
                              "LIMIT %s OFFSET %s",

    "GetMainProductAsinBagpacks": "SELECT DISTINCT(main_product_asin) FROM sorted_db.sorted_amazon_products_details "
                              "WHERE category='bagpacks' LIMIT %s OFFSET %s",

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
}