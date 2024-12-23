from infra.sql_manager import SQLManager
from infra.virustotal import VTScanner
import os


def __get_url_vt_report(url, api_key):
    scanner = VTScanner(api_key)
    url_analysis_report = scanner.get_url_report(url=url)
    return url_analysis_report


def etl_step(db_name, table_name, timerange, vp_api_key):
    try:
        db_cursor = SQLManager(db=db_name)
        query = f"SELECT * FROM companies where date(created_at) >= date('now', '-{timerange} days');"
        results = db_cursor.execute_query(query)

        url_list = []
        data = []
        url_status = False

        for row in results:
            url_status = False
            url_readable = row[3].replace('[.]', '.')
            url_spliter = parts = url_readable.split('/')
            url_host = '/'.join(url_spliter[:3])
            print(f'-----> {url_host}')

            ## validate url with VT and manage urls by host
            if url_host not in url_list:
                vt_report_status = __get_url_vt_report(url=url_host, api_key=vp_api_key)
                print(vt_report_status)
                url_status = any(vt_report_status.get(key, 0) > 1 for key in ['malicious', 'suspicious'])
                if url_status:
                    url_list.append(url_host)

            name = row[0]
            employee = row[1]
            country = row[2]
            filtered_url = url_readable if not url_status else None
            created_at = row[4]

            data.append({
                "Name": url_readable,
                "Employees": employee,
                "Country": country,
                "Filtered_URL": filtered_url,
                "created_at": created_at
            })

        db_cursor.insert_many(table_name=table_name, data=data)
    except Exception as e:
        print(f"Error while trying to run ETL Step: {e}")
        return None



def query_step(db_name, query):
    db_cursor = SQLManager(db=db_name)
    results = db_cursor.execute_query(query)
    return results


if __name__ == "__main__":
    VT_API_KEY = os.environ.get('VT_API_KEY')
    DB_NAME = os.environ.get('VT_DB_NAME')
    TABLE_NAME = 'world_companies'

    TIMERANGE = 32

    ## ETL: insert data into world_companies
    # etl_step(db_name=DB_NAME, table_name=TABLE_NAME, timerange=TIMERANGE, vp_api_key=VT_API_KEY)

    ## Querying: query data from world_companies table
    query = 'Select * from world_companies'
    results = query_step(db_name=DB_NAME, query=query)
    print(results)