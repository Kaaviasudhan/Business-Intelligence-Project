import requests
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time

# Initialize Elasticsearch client
endpoint = "<Elasticsearch_Endpoint>"
username = "<USERNAME>"
password = "<PASSWORD>"

es = Elasticsearch([endpoint], http_auth=(username, password))

def fetch_data_from_api(url):
    try:
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for non-200 status codes

        data = response.json()

        for appid, app_data in data.items():
            # print(data[appid]['price'], type(data[appid]['price']))
            data[appid]['price'] = int(app_data['price'])
            data[appid]['initialprice'] = int(app_data['initialprice'])
            data[appid]['discount'] = int(app_data['discount'])

        
        # for appid, app_data in data.items():
        #     print(data[appid]['price'], type(data[appid]['price']))

        return data
    except requests.exceptions.RequestException as ex:
        print(f"Failed to fetch data from API: {ex}")
        return None

def ingest_data_into_es(index_name, data):
    if data:
        try:
            # Check if the index already exists
            if not es.indices.exists(index=index_name):
                es.indices.create(index=index_name, ignore=400)
                print(f"Index '{index_name}' created successfully!")

            # Prepare bulk data for indexing
            bulk_data = []
            for page_num, page_data in data.items():
                for appid, game_data in page_data.items():
                    bulk_data.append({
                        "_index": index_name,
                        "_id": appid,
                        "_source": game_data
                    })

            # Use Elasticsearch's bulk API for efficient indexing
            success, _ = bulk(es, bulk_data)
            print(f"Indexed {success} documents successfully!")
        except Exception as ex:
            print(f"Error indexing data: {ex}")
    else:
        print("No data fetched from the API.")

# API Endpoint
api_url_base = "https://steamspy.com/api.php?request=all&page="


# Fetch data from the API and index into Elasticsearch
for i in range(31, 33):
    url = api_url_base + str(i)
    api_data = fetch_data_from_api(url)
    if api_data:
        ingest_data_into_es("steam_collection_updt_4", {i: api_data})
    time.sleep(150)  # Adding a small delay to avoid hitting rate limits or overwhelming the API

print("Data indexing completed.")