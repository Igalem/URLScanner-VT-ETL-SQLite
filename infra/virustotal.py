import requests


class VTScanner:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3"
        self.headers = {
            "accept": "application/json",
            "x-apikey": self.api_key,
            "content-type": "application/x-www-form-urlencoded"
        }

    def scan_url(self, url):
        try:
            payload = {"url": url}
            scan_url = f"{self.base_url}/urls"

            response = requests.post(scan_url, data=payload, headers=self.headers)
            response.raise_for_status()

            res = response.json()

            analysis_id = res.get('data', {}).get('id')

            return analysis_id

        except requests.RequestException as e:
            print(f"Error while trying to scan url: {e}")
            return None

    def get_url_report(self, url):
        try:
            analysis_id = self.scan_url(url=url)

            report_url = f"{self.base_url}/analyses/{analysis_id}"
            response = requests.get(report_url, headers=self.headers)
            response.raise_for_status()

            res = response.json()
            url_report_stats = res.get('data', {}).get('attributes', {}).get('stats')

            return url_report_stats

        except requests.RequestException as e:
            print(f"Error fetching URL report: {e}")
            return None


