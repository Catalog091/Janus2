# # from DomainUtil import DomainUtil
# #
# # ports = pd.read_csv('ports_chunk_dupes.csv')
# #
# # u_ports = list(set(ports.Ports.tolist()))
# #
# #
# # u_ports_df = pd.DataFrame(u_ports)
# #
# # u_ports_df.to_csv('clean_ports.csv')
#
#
# # domains['Domain'] = 'idn:' + domains.Domain
# #
# # # domain_list = domains.Domain.tolist()
# # file_name = 'dib_owners'
# #
# # du = DomainUtil()
# #
# # du.owner_check(domains, True, file_name).to_csv('exports.csv')
# #
# #
# # extracted_owners = pd.read_csv('exports.csv')
# #
# # owners = extracted_owners.Harvested_Domain_Owners.tolist()
# # clean_owners = list(filter(lambda x: x != 'No Owner', owners))
# #
# # extracted_owners['Harvested_Domain_Names'] = extracted_owners.Harvested_Domain_Owners.map(
# #     du.eid_to_name_finder(clean_owners))
# #
# # extracted_owners.to_csv('name_exports.csv')
#
#
# # domains = pd.read_csv('extracted_small_test_output.csv')
# #
# # TP = domains[domains['eid'] == domains['Harvested_Domain_Owners']]
# # TN = domains[domains['Harvested_Domain_Owners'] == 'No Owner']
# # FP = domains[(domains['Harvested_Domain_Owners'] != 'No Owner')
# #              & (domains['eid'] != domains['Harvested_Domain_Owners'])]
# #
# # eids = set(domains.eid.tolist())
# # c_eids = set(TP.eid.tolist())
# #
# #
# # print('True Postives:', len(TP))
# # print('True Negatives:', len(TN))
# # print('False Postives:', len(FP))
# # print('Missed eids:', len(eids) - len(c_eids))
# # print('Missed Entities: ', eids - c_eids)
#
# # print('True Negatives:\n', TN)
#
# # print('False Positives:\n', FP)
#
#
# # from recordedfuture.api import rfq
# # from recordedfuture.api.rfq import APIUtil
# # import json
# #
# # RF_TOKEN = 'c3f8b00bc737400b96c36e78060586a4'
# # token = rfq.APIUtil(RF_TOKEN)
#
#
# # def feb_domain_query(token):
# #      """
# # #     :param query_list: list of each query dictionary
# # #     :param eid_list:   list of each eid (chunked)
# # #     :return: Each eid is queried and appended to a dictionary so it can be mapped to the main dataset
# # #     (nothing is updated!)
# # #     """
# #
# #      airports_unstructured = pd.read_csv('us-airports.csv')
# #      rel_airports = airports_unstructured[['LOCID', 'SITE_NO', 'FULLNAME', 'FAA_ST', 'FAA_REGION',
# #                                            'LAN_FA_TY', 'STATE_NAME', 'COUNTY_NAM',
# #                                            'CITY_NAME', 'OWNER_TYPE', 'INTERNATIO',
# #                                            'JOINT_USE', 'MIL_LNDG_R', 'LATITUDE', 'LONGITUDE']]
# #
# #      filt_lis = ['BALOONPORT', 'SEAPLANE BASE', 'GLIDERPORT', 'HELIPORT', 'ULTRALIGHT']
# #
# #      rel_airports = rel_airports[~rel_airports['LAN_FA_TY'].isin(filt_lis)]
# #      rel_airports = rel_airports[~((rel_airports['LATITUDE'].isnull()) &
# #                                    (rel_airports['LONGITUDE'].isnull()))]
# #
# #      un_states = list(set(rel_airports.STATE_NAME.tolist()))
# #      # un_lis = json.dumps(un_states)
# #
# #      terror_querys_eid ={
# #        "entity": {
# #          "type": "Company",
# #          "name": 'Ritchie Bros'
# #        }
# #      }
# #
# #      ret_terror = token.query(terror_querys_eid)
# #
# #      df_terror = pd.DataFrame(ret_terror['entity_details']).T
# #
# #      df_terror.to_csv('domain_util_test.csv')
# #
# #      return df_terror
# #
# # feb_domain_query(token)
# #
# # reddy_comps = pd.read_csv('reddy_companies_groups.csv').reset_index()
# # reddy_comps = reddy_comps.rename(columns={"Unnamed: 0": "eid"})
# #
# # adjusted_comps = reddy_comps[['eid', 'name']]
# # adjusted_comps.to_csv('domain_util_test.csv')
# #
# # print(adjusted_comps.head(5))
#
# import pandas as pd
# import os
# pd.set_option('display.max_columns', None)
#
# # files = os.listdir('Airport_Harvests')
#
# # def df_formatter(files):
# #
# #     df_list = []
# #
# #     for df in files:
# #         old_df = pd.read_csv('Airport_Harvests/' + df)
# #
# #         new_df = old_df.rename(columns={"Unnamed: 0": "Name"})
# #         # df_list.append(new_df)
# #
# #     return df_list
# #
# # form_dfs = df_formatter(files)
# #
# # print(len(form_dfs))
#
# # df = pd.concat([pd.read_csv('Airport_Harvests/' + f) for f in os.listdir('Airport_Harvests')], ignore_index=True)
# # df.to_csv('All_Harvested_AP.csv')
# # print(df)
#
# facs = pd.read_csv('port_parse8.csv')
# ports = pd.read_csv('existing_ports_comparison.csv')
#
# tran_facs = facs[['Unnamed: 0', 'name', 'containers', 'hits', 'owner', 'external_links', 'curated']]
# tran_facs['low_name'] = tran_facs['name'].str.lower()
# tran_ports = ports[['Unnamed: 0', 'name', 'containers', 'hits']]
# tran_ports['low_name'] = tran_ports['name'].str.lower()
#
# tran_facs = tran_facs.rename(columns={'Unnamed: 0': "facility_eid"})
# tran_ports = tran_ports.rename(columns={'Unnamed: 0': "eid"})
#
# eid_only_facs = tran_facs['facility_eid']
# eid_only_ports = tran_ports['eid']
#
# # all_ents = eid_only_ports.append(eid_only_facs)
#
# all_ents = tran_ports.merge(tran_facs, how="outer", on="low_name", suffixes=(1, 2))
# all_ents = all_ents[all_ents['facility_eid'].notnull()]
# all_ents = all_ents[all_ents['eid'].notnull()]
#
# all_ents = all_ents.rename(columns={'name1': 'port_name',
#                                     'name2': 'facility_name',
#                                     'containers1': 'containers',
#                                     'containers2': 'facility_containers',
#                                     'hits1': 'hits',
#                                     'hits2': 'facility_hits',
#                                     'curated': 'facility_curated',
#                                     'owner': 'facility_owner',
#                                     'external_links': 'facility_links'})
#
# values = {'facility_containers': 'None',
#           'facility_hits': 0.0,
#           'hits': 0.0,
#           'facility_owner': 'None',
#           'facility_links': 'None'}
#
# all_ents = all_ents.fillna(value=values)
# all_ents = all_ents.drop(['low_name'], axis=1)
# all_ents['containers'] = all_ents['containers'].str.strip('[]').astype(str)
#
# all_ents = all_ents.copy()
#
# # all_ents.to_csv('transformed_existing_ports_new.csv')
#
# def f(row):
#
#     try:
#         if (row['containers'] in row['facility_containers']) and (row['hits'] < row['facility_hits']) or \
#                 (row['facility_owner'] != 'None'):
#             val = 'Syn_Port_Change_Type'
#
#         elif (row['containers'] not in row['facility_containers']) and \
#                 (row['facility_containers'] != 'None') and (row['hits'] > row['facility_hits']) or \
#                 (row['facility_links'] != 'None'):
#             val = 'Inspect_Facility'
#
#         elif (row['facility_containers'] == 'None') and (row['hits'] >= row['facility_hits']) and \
#                 (row['facility_owner'] == 'None') and (row['facility_links'] == 'None'):
#             val = 'Smooth_Syn_Fac'
#
#         else:
#             val = 'Rough_Syn_Fac'
#         return val
#     except TypeError as e:
#         print(e, ':', row)
#
#
# all_ents['Synonymization_Value'] = all_ents.apply(f, axis=1)
# all_ents = all_ents[all_ents['facility_eid'].notnull()]
#
# all_ents = all_ents.sort_values(by='Synonymization_Value', ascending=False)
#
# # all_ents.to_csv('transformed_existing_ports_with_conditions_New.csv')
#
# test_ents_smooth = all_ents[all_ents['Synonymization_Value'] == 'Smooth_Syn_Fac']
# test_ents_SP = all_ents[all_ents['Synonymization_Value'] == 'Syn_Port_Change_Type']
# test_ents_rough = all_ents[all_ents['Synonymization_Value'] == 'Rough_Syn_Fac']
# test_ents_inspect = all_ents[all_ents['Synonymization_Value'] == 'Inspect_Facility']
#
# print('Ready to synonymize the Facility to the Port: ', len(test_ents_smooth))
# print('Synonymize the Port to the Facility and change type to Port: ', len(test_ents_SP))
# print('Double check best course of action to synonymize the Facility to the Port: ', len(test_ents_rough))
# print('Manual Inspection required: ', len(test_ents_inspect))
#
# test_smooth_frac = test_ents_smooth[0:3]
# print(test_smooth_frac)
#
# from recordedfuture.apps.februus.handlers.entity_api_util import EntityAPIUtilHandler
#
# e = EntityAPIUtilHandler
#
# eid_zip = dict(zip(test_smooth_frac.eid,
#                    test_smooth_frac.facility_eid))  # Dictionary of target eid : redundant entity eid
#
# for a, b in eid_zip.items():
#     e.synonymize(a, b)
#
# """
# Locations Intel Card
# """

# import pandas as pd
# from geopy.geocoders import Bing
# from geopy.extra.rate_limiter import RateLimiter
#
# geo = Bing('AgcMxnI9WqIklf09OV0WimmYCl1qVPd0WHxOfNxRKvKaEywsbWk8UOFWF__KG6UH')
# rate = RateLimiter(geo.geocode, min_delay_seconds=1)
#
# pd.set_option('display.max_columns', None)
#
# county_dict = {'Alameda': '1225 Fallon Street, Oakland, California, 94612',
#                'Alpine': '99 Water Street, Markleeville, California, 96120',
#                'Amador': '810 Court Street, Jackson, California, 95642-2132',
#                'Butte': '155 Nelson Ave, Oroville, California, 95965-3411',
#                'Calaveras': '891 Mountain Ranch Road San Andreas, California, 95249',
#                'Colusa' : '546 Jay Street, Suite 200 Colusa, California, 95932',
#                'Contra Costa': '555 Escobar St. Martinez, California, 94553',
#                'Del Norte': '981 H Street, Room 160 Crescent City, California, 95531',
#                'El Dorado': '2850 Fairlane Court Placerville, California, 95667',
#                'Fresno': '2221 Kern Street Fresno, California, 93721',
#                'Glenn': '516 W. Sycamore Street, 2nd Street Willows, California, 95988',
#                'Humboldt': '2426 6th Street Eureka, California, 95501',
#                'Imperial': '940 W. Main Street, Suite 206 El Centro, California, 92243',
#                'Inyo': '168 N. Edwards Street Independence, California, 93526',
#                'Kern': '1115 Truxtun Avenue, First Floor Bakersfield, California, 93301',
#                'Kings': '1400 W. Lacey Blvd. Hanford, California, 93230',
#                'Lake': '255 N. Forbes Street Lakeport, California, 95453',
#                'Lassen': '220 S. Lassen Street, Suite 5 Susanville, California, 96130',
#                'Los Angeles': '12400 Imperial Hwy. Norwalk, California, 90650',
#                'Madera': '200 W. 4th Street Madera, California, 93637',
#                'Marin': '3501 Civic Center Drive, Room 121 San Rafael, California, 94903',
#                'Mariposa': '4982 10th Street Mariposa, California, 95338',
#                'Mendocino': '501 Low Gap Road, Room 1020 Ukiah, California, 95482',
#                'Merced': '2222 M Street Merced, California, 95340',
#                'Modoc': '108 E. Modoc Street Alturas, California, 96101',
#                'Mono': '74 N. School Street, Annex I Bridgeport, California, 93517',
#                'Monterey': '1441 Schilling Place North Building Salinas, California, 93901',
#                'Napa': '1127 First St. Ste. E Napa, California, 94559',
#                'Nevada': '950 Maidu Avenue, Suite 210 Nevada City, California, 95959',
#                'Orange': '1300 South Grand Avenue, Bldg. C Santa Ana, California, 92705',
#                'Placer': '2956 Richardson Drive Auburn, California, 95603',
#                'Plumas': '520 Main Street, Room 102, Courthouse Quincy, California, 95971',
#                'Riverside': '2724 Gateway Drive Riverside, California, 92507-0918',
#                'Sacremento': '7000 65th Street, Suite A Sacramento, California, 95823',
#                'San Benito': '440 Fifth Street, Hollister, California, 95023-3843',
#                'San Bernardino': '777 E. Rialto Avenue San Bernardino, California, 92415-0770',
#                'San Diego': '5600 Overland Avenue San Diego, California, 92123',
#                'San Franciso': '1 Dr. Carlton B Goodlett Place San Francisco, California, 94102-4635',
#                'San Joaquin': '44 N. San Joaquin Street, Stockton, California, 95202',
#                'San Luis Obispo': '1055 Monterey Street, San Luis Obispo, California, 93408',
#                'San Mateo': '40 Tower Road San Mateo, California, 94402',
#                'Santa Barbara': '4440-A Calle Real Santa Barbara, California, 93110',
#                'Santa Clara': '1555 Berger Drive, Bldg. 2 San Jose, California, 95112',
#                'Santa Cruz': '701 Ocean Street, Santa Cruz, California, 95060',
#                'Shasta': '1643 Market Street Redding, California, 96001',
#                'Sierra': '100 Courthouse Square, Downieville, California, 95936-0398',
#                'Siskiyou': '510 N. Main Street Yreka, California, 96097-9910',
#                'Solano': '675 Texas Street, Suite 2600 Fairfield, California, 94533',
#                'Sonoma': '435 Fiscal Drive Santa Rosa, California, 95403',
#                'Stanislaus': '1021 I Street, Suite 101 Modesto, California, 95354-2331',
#                'Sutter': '1435 Veterans Memorial Circle Yuba City, California, 95993',
#                'Tehama': '633 Washington Street, Room 17 Red Bluff, California, 96080',
#                'Trinity': '11 Court Street Weaverville, California, 96093',
#                'Tulare': '5951 S. Mooney Blvd. Visalia, California, 93277',
#                'Tuolumne': '2 S. Green Street Sonora, California, 95370-4618',
#                'Ventura': '800 S. Victoria Avenue Hall of Administration, Lower Plaza Ventura, California, 93009-1200',
#                'Yolo': '625 Court Street Room B-05, Woodland, California, 95695'
#                }
# county_df = pd.DataFrame.from_dict(county_dict, orient='index').reset_index()
# county_df = county_df.rename(index=str, columns={'index': 'County_name', 0: 'address'}).reset_index()
# county_df['New_Entity'] = county_df.County_name.apply(lambda x: x + ' ' + 'County Election Office')
# county_df['County_name'] = county_df.County_name.apply(lambda x: x + ' ' + 'County')
#
#
#
# geo_coded = pd.read_csv('geo_coded_counties.csv')
#
# lat_dict = dict(zip(geo_coded.Address, round(geo_coded.Latitude, 4)))
# lon_dict = dict(zip(geo_coded.Address, round(geo_coded.Longitude, 4)))
#
# county_df['Lat'] = county_df.address.map(lat_dict)
# county_df['Lon'] = county_df.address.map(lon_dict)
#
# # county_df['Lat'] = county_df.Lat.apply(lambda x: 'latitude: ' + str(x))
# # county_df['Lon'] = county_df.Lon.apply(lambda x: 'longitude: ' + str(x))
#
# # from curation_mambo import QueryHandler
# #
# # que = QueryHandler()
# # county_list = county_df.County_name.tolist()
# #
# # query = que.standard_query(county_list, 'ProvinceOrState', False)
# # print(query)
# # query.to_csv('cross_val_que.csv')
#
#
# county_df['containers'] = [['B_GRZ','B_FAG','I2EnW9']] * len(county_df)
#
# cross = pd.read_csv('cross_val_que.csv')
# cross = cross[['Unnamed: 0.1.1', 'name']]
#
# count_cross_ls = {}
#
# for i, j in cross.iterrows():
#     county = j['name']
#     if 'County' not in county:
#         county_new = county + ' ' + 'County'
#         count_cross_ls[county_new] = j['Unnamed: 0.1.1']
#     else:
#         count_cross_ls[county] = j['Unnamed: 0.1.1']
#
# county_df['County_eid'] = county_df.County_name.map(count_cross_ls)
#
#
# map_d = {}
#
# for c, r in county_df.iterrows():
#     pos = {r['Lat'], r['Lon']}
#     map_d[r['County_name']] = pos
#
# county_df['pos'] = county_df.County_name.map(map_d)
#
# county_df['containers'] = county_df.containers.apply(lambda x: ",".join(i for i in x))
# county_df['containers'] = county_df['containers'] + ',' + county_df['County_eid']
# county_df['containers'] = county_df.containers.apply(lambda x: str(x).split(','))
#
# final_df = county_df[['New_Entity', 'address', 'Lat', 'Lon', 'containers']]
# final_df.to_csv('New_County_Ents.csv')

print('Hello World!')
