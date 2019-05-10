from app.common.db.postgres import PgPool
from app.models.config.queries import QUERIES
import random


pg_ = PgPool()

def get_product_link(sku):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetLink"]
    params = (sku, sku, sku, sku, sku, sku, sku, sku,sku,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        print(res)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None



def get_ebay_earings(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetEarings"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None



def get_ebay_watches(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetWatches"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_ebay_bracelet(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetBracelet"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_ebay_jewelry(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetJewelry"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_ebay_handbags(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetHandbags"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_ebay_clutches(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetClutches"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_ebay_bagpack(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetBagpack"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_ebay_running(limit, offset):
    """
    Returns sentiment labels of product
    :param product_id: id of product
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetRunning"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_sandals(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinSandals"]
    params = (limit, offset, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_against_main_asin(main_product_asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetDataAgainstAsin"]
    param = (main_product_asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, param)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_running(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinRunnings"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_flats(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinFlats"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_sneakers(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinSneakers"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_training(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinTrainings"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None


def get_product_asin_watches(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinWatches"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_bracelet(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinBracelets"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_handbags(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinHandbags"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_clutches(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinClutches"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_product_asin_bagpack(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetMainProductAsinBagpacks"]
    params = (limit, offset,)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None


def get_url(sku, color, size):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetUrl"]
    params = (sku, color, size,sku,sku,color,sku, color)
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res[0][0]
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_all_data_of_shopspring(limit, offset):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetShopSpringData"]
    params=(limit, offset,)

    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None    

def get_all_data_of_zara():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["ZaraData"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None 

def get_all_data_of_macys():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["MacysData"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_all_main_asin_of_6pm():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["6PmDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_data_against_asin_6pm(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["6PmData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_all_main_asin_of_zappos():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["ZapposDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_data_against_asin_zappos(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["ZapposData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_all_main_asin_of_aldoshoes():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["AldoDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_data_against_asin_aldoshoes(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["AldoData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_all_main_asin_of_tedbaker():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["TedbakerDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_data_against_asin_tedbaker(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["TedbakerData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_all_main_asin_of_katespade():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["KatespadeDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_data_against_asin_katespade(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["KatespadeData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_all_main_asin_of_michaelkors():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["MichaelkorsDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_data_against_asin_michaelkors(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["MichaelkorsData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_all_main_asin_of_nordstromrck():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["NordstromrackDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_data_against_asin_nordstromrack(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["NordstromrackData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_all_main_asin_of_shopguess():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["ShopguessDataAsin"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_data_against_asin_shopguess(asin):
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["ShopguessData"]
    params = (asin, )
    try:
        res = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None


def get_data_against_asin_ashford():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["AshfordData"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None


def get_data_against_asin_toryburch():
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["ToryBurchData"]

    try:
        res = pg_.execute_query(pg_cursor, query, params='')
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return res
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None