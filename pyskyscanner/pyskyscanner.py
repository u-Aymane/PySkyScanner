import uuid
from pycookies import COOKIES
import requests
import json


class PySkyScanner:
    def __init__(self):
        self.keyword = None
        self.destination_bool = 'false'
        self.destination = None
        self.current_loc = None
        self.date = None
        self.id = None
        self.cookies = '__Secure-anon_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImM3ZGZlYjI2LTlmZjUtNDY4OC1iYjc3LWRiNTY2NWUyNjFkZSJ9.eyJhenAiOiIyNWM3MGZmZDAwN2JkOGQzODM3NyIsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvbG9naW5UeXBlIjoiYW5vbnltb3VzIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC91dGlkIjoiNTVhZmZhN2EtMjZjNS00Y2IxLWE2YTItMjU1NThhNTkyNTE3IiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC9jc3JmIjoiZjQ1MTRmMTZlZGFhNGU5MTM1ZmYxOWZhNDYzMmIxMzUiLCJodHRwczovL3NreXNjYW5uZXIubmV0L2p0aSI6IjE0MzA4ZmJlLWM4NzgtNGRiZS05ZDhhLWNlYjZkODZlNjVkOSIsImlhdCI6MTY1ODMxOTcxNywiZXhwIjoxNzIxMzkxNzE3LCJhdWQiOiJodHRwczovL2dhdGV3YXkuc2t5c2Nhbm5lci5uZXQvaWRlbnRpdHkiLCJpc3MiOiJodHRwczovL3d3dy5za3lzY2FubmVyLm5ldC9zdHRjL2lkZW50aXR5L2p3a3MvcHJvZC8ifQ.Ws1e6w2_GEjvkZnn03aLIOjEqYF_-H1ygHs7UfUDYoVMHw_4Rd_b5ryZFivQMagkzjdEo3pVhMz4qXKzMGPqBsMnGRNRLjDHYZKXd_L9qItS1JEvtpuLPPsFTQp5hhV4Wz4L78JIT509l7w3ucuEkUwWZ-drAEH3zal9YtjT6i1IVgSPieRHNDTp9dg_HfhojXc9rBK-k6ld4o0dE6PlFTB-48Lc5ptn3IcBPYufMb3SHT28i1BToJHDtLuGd6lpBowKLwbnScAmb3wn8k1NP6qVfWSaudKPj1E56H3OQUiMcGLMl3Hy8jYhSbbiP9auoxqEp7sK8FpmFbAuXvSdUA; __Secure-anon_csrf_token=f4514f16edaa4e9135ff19fa4632b135; abgroup=23229857; __Secure-ska=144b0900-21f1-47b4-9ce1-d78bde8bc794; device_guid=144b0900-21f1-47b4-9ce1-d78bde8bc794; b_opt_out=true; preferences=55affa7a26c54cb1a6a225558a592517; ssculture=locale:::en-GB&market:::MA&currency:::EUR&seenNotice:::true; _ga=GA1.2.1842396654.1658319719; _pxvid=8c155f2a-0826-11ed-ace5-764679715967; __pxvid=8efa925f-0826-11ed-a251-0242ac120003; _fbp=fb.1.1658319720796.1876232055; _gcl_au=1.1.820679851.1658319893; __gads=ID=0901657673f13f07:T=1658319896:S=ALNI_MbZmX7IzfZ2DdDanEm1-clOCLJ6ww; g_state={"i_p":1658870673449,"i_l":2}; _pxhd=kmELXnPJDZgCdMZL13eGAWu9jUNPRzBEcxif5SkzIT5M254Z8IUNROtdooM6BwMTagvZM/7VZDawppgzGIj2uw==:m6SQTMjjch0oWbCm9Xo5fU3R/lkjYrXzo83KaeOsP9OrjvX7BSD38AizZfevAaQJPzIWnmSZeJJ9wxmMBQ5urRNKUPumphSOQBvLmWjq8uo=; traveller_context=55affa7a-26c5-4cb1-a6a2-25558a592517; ssab=AAExperiment_V9:::b&ATBT_show_new_group_detail_on_web_V3:::b&EUR_flights_dbook_coupon_flow_V2:::b&FAQPricingConsolidationFromLipsToUssExperiment_V8:::a&Pay_Button_CTA_V4:::b&Ranking_for_Google_popular_hotel_desktop_V4:::b&Space_travel_web_experiment_V1:::b&TRIPLANE_236_FALCON_FalconShowLcDestinationsExplorer_V6:::a&WPD_HideFSCCheapestMonthButton_V2:::b&ads_filtering_V7:::a&banana_increase_dayview_initial_result_count_V1:::a&dbook_eurw_trafficcontrol_web_desktop_100_V2:::a&dbook_uair_trafficcontrol_web_V2:::a&fps_mr_fqs_flights_ranking_ceres__25i_desktop_V2:::c&fps_mr_fqs_flights_ranking_haumea_retrained__25i_web_V2:::a&fps_ttlr_early_timeout_web_V17:::a&global_inline_test_v2_V3:::g&heimdallr_split_ap_northeast_1_V5:::a&heimdallr_split_ap_southeast_1_V6:::a&heimdallr_split_eu_west_1_V10:::a&hercules_cancel_for_any_reason_V1:::b&mr_migration_proxy_test_always_50_percent_V8:::a&mr_migration_proxy_test_always_on_V4:::a&test_traffic_splitting_V2:::a; experiment_allocation_id=be9b9b0d098727bd6428e7be1f1813c13c92ce1c540f1772f83d7010c0088b8d; ssaboverrides=; _gid=GA1.2.50906979.1658887939; pxcts=8b25d86d-0d51-11ed-8737-765845635372; _clck=jdsas1|1|f3i|0; __gsas=ID=b4d1ba284e0e9106:T=1658887944:S=ALNI_MYKJx-Cc0lR5VRnB8L2RzrIvTTp-w; __gpi=UID=00000a55567e9c2d:T=1658319896:RT=1658887945:S=ALNI_MYIBYw7r1yxvFuJGCwEEgZIAPidQg; scanner=currency:::EUR&legs:::RBA|2022-08-01|PARI|||&tripType:::one-way&rtn&from:::AGP&to:::LOND; sid_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZEVNa000UmtZek1FSTJOVFkwUWtJd09ETkNSRFJCTURjeFEwSXpNVUUwTTBVeU9EUkJRUSJ9.eyJodHRwczovL3NreXNjYW5uZXIubmV0L3V0aWQiOiI1NWFmZmE3YS0yNmM1LTRjYjEtYTZhMi0yNTU1OGE1OTI1MTciLCJodHRwczovL3NreXNjYW5uZXIubmV0L2lzTmV3VXNlciI6dHJ1ZSwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC9jc3JmIjoiNjZkNGMwN2M0NTAyM2VkNTM1NGY4MGJhNmQxYTlhZmIiLCJodHRwczovL3NreXNjYW5uZXIubmV0L2xvZ2luVHlwZSI6Imdvb2dsZSIsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvaXNTb2NpYWwiOnRydWUsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvanRpIjoiNDQzYzcwNTctMjRkMC00ZjAxLWJhZGQtNjM5Y2U4NWI1YTA0IiwiaXNzIjoiaHR0cHM6Ly9za3lzY2FubmVyLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjg5MjYyOTE3NzEyODg2MDI1MyIsImF1ZCI6WyJodHRwczovL2dhdGV3YXkuc2t5c2Nhbm5lci5uZXQvaWRlbnRpdHkiLCJodHRwczovL3NreXNjYW5uZXIuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY1ODg4OTcxMSwiZXhwIjoxNjU4OTE4NTExLCJhenAiOiJYZTMzc0xEZ0dvVEpaUDdZNUxuSnZnZ0xrNk9PY0F5byIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgb2ZmbGluZV9hY2Nlc3MifQ.J1detPXZCslvEuSeVG2SnBte3ZhyJwv9Q8vncuRCtfhx8ciZ_ehMEJ5ZAXcLsD72D8Yct5Kg51U_XNB-7J6z8KVeRiaw6q3FneUjlzqwZXZv8TOpNvHFljS9IQ4Zvk-Ga2malxi-HzY5nghbrVVOxZl31UFLl7eVMnXfzHq7hwa8f9Unq0hGqZh97IJs2VI29RmV6qsR66j_YGGlCFeD3QOqEM4naIIyhEoevs6ft5TL4RVlJrcpVQZLLnQEmEDMGcKEqCeYkTxTN_jbzIpFnVgMCFruiJuj9dPz6nN2w0R8ud5z3t5M2NY07MYLiDsvhEQCgfnODxY289IRBjKjuQ; sid_id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZEVNa000UmtZek1FSTJOVFkwUWtJd09ETkNSRFJCTURjeFEwSXpNVUUwTTBVeU9EUkJRUSJ9.eyJodHRwczovL3NreXNjYW5uZXIubmV0L3V0aWQiOiI1NWFmZmE3YS0yNmM1LTRjYjEtYTZhMi0yNTU1OGE1OTI1MTciLCJodHRwczovL3NreXNjYW5uZXIubmV0L2NzcmYiOiI2NmQ0YzA3YzQ1MDIzZWQ1MzU0ZjgwYmE2ZDFhOWFmYiIsImdpdmVuX25hbWUiOiJKYWNrIiwiZmFtaWx5X25hbWUiOiJEb2VzIiwibmlja25hbWUiOiJzaXh0b3BzdHJpbmdoYXQwMSIsIm5hbWUiOiJKYWNrIERvZXMiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUl0YnZtbVJkS0RsbF9LTEZ2YkJ5S01sMjgzYkgyVWtydUktRGpCQkktdnI9czk2LWMiLCJsb2NhbGUiOiJlbiIsInVwZGF0ZWRfYXQiOiIyMDIyLTA3LTI3VDAyOjQxOjQ5LjQ4NVoiLCJpc3MiOiJodHRwczovL3NreXNjYW5uZXIuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEyODkyNjI5MTc3MTI4ODYwMjUzIiwiYXVkIjoiWGUzM3NMRGdHb1RKWlA3WTVMbkp2Z2dMazZPT2NBeW8iLCJpYXQiOjE2NTg4ODk3MTEsImV4cCI6MTY2MTMwODkxMX0.YY3dN5VPWtA4qhM7ONWfVQ31GOPo6Yh0iScKexToWsfbjAmriiTVYmNa1WZ2q1YbnscweOo0dIN1rD2iLzy7gLr-YFf7yQiqv0034S9DNgl5CgG7BxpyZMX1G3Sxo12YMUaVbqEPyubJFv86L2YCMuzcZ-vJey2FughJJ1yT9T-zAoljJ3G2Nma8fJ2ZyIja9WWv-97iFP03decubAQGc3QrsPhacuLNopTMR_C2ZPhqMxN_duZha0jozanhO7tDe4DAbKKeAWHGUM2ZDtmlePm0f2_TckD7Zaafv_TV_PT7wMCr6AhHAts-z_TBCwC0Mt0woN_cNomSFLHnRa57fw; __Secure-sid_csrf_token=66d4c07c45023ed5354f80ba6d1a9afb; sid_utid=55affa7a-26c5-4cb1-a6a2-25558a592517; sid_session_token=eyJraWQiOiIyYTc5NTk3Ny1iNjdhLTQ2MTQtOTQxMS03N2Q2MjE0N2UwNGQiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NTg4ODk3MTEsInN1YiI6IjU1YWZmYTdhLTI2YzUtNGNiMS1hNmEyLTI1NTU4YTU5MjUxNyIsImlzcyI6Imh0dHBzOi8vd3d3LnNreXNjYW5uZXIubmV0L3N0dGMvaWRlbnRpdHkvandrcy9wcm9kLyIsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvc2Vzc2lvblR5cGUiOiJQRVJTSVNURU5UIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC9sYXN0QXV0aGVudGljYXRpb25UaW1lIjoxNjU4ODg5NzExODUxLCJodHRwczovL3NreXNjYW5uZXIubmV0L2FjY2Vzc1Rva2VuRXhwaXJ5IjoxNjU4OTE3OTEyMDM4fQ.KCndB_BERkMOAGTMGzI3WUgAX5iVFmCwR9Qk1DDoAxy3dfGySxn9-bmiq0oTu7qO5Rx72X7PBIx9vBE_Z0RGEHkMHX95owzzGzpQdnuY4Vqje9FOuVsWHoqUqCQVfsMT3xV3rWW3qShBfjufGELk9QwO2AEmnA4FwNZiFESshoEVwVTlBk4cgAsodzxtRo68FtVkcMq_XK5s7z0lDbv-cT0gxtgV5-JbdeXGVXLThpsNF3JJBVobPSP4Cx2QsVLMJlQjafh0B7LBnmk_IYXH_LbD6cH8oZauBzcjReIfjm_7l5UK4NGFC61Md6iVOeHtmDw-ehdDhMW5NjONCEuk1A; _pxff_tm=1; _uetsid=8b9cdbf00d5111edb45ce5817ec4d2e8; _uetvid=8e27fb00082611edb19fa9540965fb40; _px3=5d4f6874ac10cc7ac733ca18bd06b938c88785bb154c414c0b8f874627b84daf:ulj285aums8YC0c4DR9XJ2b1ozocvjqc0eDaxEu3Iezkyuue/AB53Lj/V4ou6Ih2Mytn6360gRjShLCICbFo3w==:1000:xFNzDsOii7P+BqkvcS7qVnwqE3dqNE3IJXiaDZP/mHIFLrIabMgi9Kf0jQfZYRFrGBpLrPeV0WXAUAilDvZ2+TirEHAosdrHsf68qc8yiT/x2Wrieo/VlX8Dt81ebBlA2W9TpEP58biuIszBaDCuxaj9uR0vHgTS7TYcH6DndKUyg0OrqGo7IZ1wpZcvR0dqqk7RIH1QlYCXlSWtiWT0KQ==; _clsk=1g2h0lt|1658891562242|14|1|l.clarity.ms/collect; _gat=1'
        self.cookies = COOKIES(self.cookies).cookies_function()
        self.session_id = None
        self.header = ['id', 'flight agent', 'price', 'departure', 'arrival', 'duration', 'booking url']
        with open('results.csv', 'w', encoding='utf-8') as f:
            f.writelines(f"{','.join(self.header)}\n")
        f.close()

    def constructe_json(self, informated: dict):
        return {'id': informated['PlaceId'], 'name': informated['PlaceName'], 'cityId': informated['CityId'],
                'cityName': informated['CityName'], 'countryId': informated['CountryId'], 'type': "City",
                'centroidCoordinates': informated['Location'].split(','),
                'geoContainerId': informated['GeoContainerId']}

    def generate_uuid(self):
        self.id = str(uuid.uuid4())

    def get_suggestions(self):
        url = f"https://www.skyscanner.fr/g/autosuggest-search/api/v1/search-flight/EU/en-GB/{self.keyword[:3]}?isDestination={self.destination_bool}&enable_general_search_v2=true"

        headers = {
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Accept': 'application/json',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("GET", url, headers=headers, cookies=self.cookies)
        cities = {}
        i = 1
        for city in response.json():
            cities[i] = self.constructe_json(city)
            i += 1

        return cities

    def show_menu(self):
        elements = self.get_suggestions()
        print('Suggestions:')
        for i, val in elements.items():
            print(f'{i}. {val["name"]}')

        choice = int(input('Choice: '))

        return elements[choice]

    def run(self):
        self.keyword = input('CURRENT LOCATION (eg. London): ')
        self.current_loc = self.show_menu()

        self.keyword = input('DESTINATION (eg. Malaga): ')
        self.destination = self.show_menu()

        self.date = input('Date (eg 2022-08-01): ')

        self.get_flights()

    def create_session(self):
        self.generate_uuid()
        url = "https://www.skyscanner.fr/g/delivery-service/api/v3/request"

        payload = "{\"id_placements\":{\"adslot-7ca7f308\":\"desktop.flights.dayview/leaderboard\",\"adslot-e7f813c0\":\"desktop.flights.dayview/skyscraper\"},\"targeting\":{\"culture_settings\":{\"country\":\"MA\",\"currency\":\"EUR\",\"locale\":\"en-GB\"},\"os\":\"windows\",\"page_type\":\"flights.dayview\",\"cabin_class\":\"ECONOMY\",\"passengers\":{\"adult_count\":1,\"child_count\":0,\"infant_count\":0},\"origin\":{\"airport\":{\"location_attribute\":{\"location_attribute_encoding\":\"IATA\",\"location_id\":\"AGP\",\"location_name\":\"Malaga\"}},\"city\":{\"location_attribute\":{\"location_attribute_encoding\":\"IATA\",\"location_id\":\"MALA\",\"location_name\":\"Málaga\"}},\"country\":{\"location_attribute\":{\"location_attribute_encoding\":\"IATA\",\"location_id\":\"ES\",\"location_name\":\"ES\"}}},\"destination\":{\"city\":{\"location_attribute\":{\"location_attribute_encoding\":\"IATA\",\"location_id\":\"LOND\",\"location_name\":\"London\"}},\"country\":{\"location_attribute\":{\"location_attribute_encoding\":\"IATA\",\"location_id\":\"UK\",\"location_name\":\"UK\"}}},\"itinerary_type\":\"ONE_WAY\",\"search_start_timestamp\":{\"unix_time_millis\":1659312000000,\"date_time_kind\":\"DAY\",\"timezone_offset_mins\":-60,\"daylight_savings_offset_mins\":60},\"duration\":0},\"user_features\":{\"request_id\":\"" + self.id + "\",\"is_new_user\":false,\"client\":{\"browser_name\":\"Chrome\",\"is_browser\":true,\"is_mobilephone\":false,\"is_tablet\":false,\"display_height\":1080,\"display_width\":1920,\"referrer_url\":\"www.skyscanner.fr\"},\"is_optedin_for_personalised\":true,\"platform\":\"DESKTOP_WEB\",\"ga_cid\":\"1842396654.1658319719\",\"authentication_status\":\"AUTHENTICATED\",\"utid\":\"55affa7a-26c5-4cb1-a6a2-25558a592517\"}}"
        headers = {
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'x-skyscanner-viewid': self.id,
            'Content-Type': 'application/json; charset=utf-8',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*'
        }

        response = requests.request("POST", url, headers=headers, data=payload, cookies=self.cookies)

        if response.status_code == 200:
            return 1
        else:
            return -1

    def write_csv(self, response: dict):
        i = 0

        itineraries_ = response['itineraries']
        with open('results.csv', 'a', encoding='utf-8') as f:
            for itineraries in itineraries_:
                f.writelines(f'"{itineraries["id"]}",{itineraries["pricing_options"][0]["agent_ids"][0]},{itineraries["pricing_options"][0]["price"]["amount"]} EUR,{response["legs"][i]["departure"].replace("T", " ")},{response["legs"][i]["arrival"].replace("T", " ")},{"{:.2f}".format(response["legs"][i]["duration"]/60)},"https://skyscanner.com/{itineraries["pricing_options"][0]["items"][0]["url"]}"\n')
                i += 1
        f.close()

    def get_flights(self):
        self.create_session()
        url = "https://www.skyscanner.fr/g/conductor/v1/fps3/search/?geo_schema=skyscanner&carrier_schema=skyscanner&response_include=query%3Bdeeplink%3Bsegment%3Bstats%3Bfqs%3Bpqs"

        payload = json.dumps({
            "market": "MA",
            "locale": "en-GB",
            "currency": "EUR",
            "alternativeOrigins": False,
            "alternativeDestinations": False,
            "destination": self.destination,
            "adults": 1,
            "cabin_class": "economy",
            "child_ages": [],
            "options": {
                "include_unpriced_itineraries": True,
                "include_mixed_booking_options": True
            },
            "origin": self.current_loc,
            "outboundDate": self.date,
            "prefer_directs": False,
            "state": {},
            "viewId": self.id,
            "travellerContextId": "55affa7a-26c5-4c11-a6a2-25558a592517",
            "trusted_funnel_search_guid": self.id,
            "legs": [
                {
                    "origin": self.current_loc['id'],
                    "destination": self.destination['id'],
                    "date": self.date,
                    "add_alternative_origins": False,
                    "add_alternative_destinations": False
                }
            ]
        })
        headers = {
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'X-Skyscanner-DeviceDetection-IsTablet': 'false',
            'X-Skyscanner-ChannelId': 'website',
            'X-Skyscanner-Utid': '55affa7a-26c5-4cb1-a6a2-25558a592517',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'X-Skyscanner-Traveller-Context': '55affa7a-26c5-4cb1-a6a2-25558a592517',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Skyscanner-ViewId': self.id,
            'X-Skyscanner-DeviceDetection-IsMobile': 'false',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload, cookies=self.cookies)
        if response.status_code == 200:
            self.session_id = response.json()['context']['session_id']
            self.write_csv(response.json())
        else:
            print(f'Please pass the captcha: https://www.skyscanner.fr/sttc/px/captcha-v2/index.html{response.json()["redirect_to"].split("index.html")[1]}')
            input('CLICK ENTER WHEN YOU PASS THE CAPTCHA...')
            return self.get_flights()

        print("Operation Successful")

