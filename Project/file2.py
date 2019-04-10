import requests as r
import pprint,json,yaml
data = r.get('https://5wH3X9CZ4r:dQPfw4VC@api.performancehorizon.com/reporting/report_publisher/publisher/1101l59001/conversion?start_date=2018-01-01&timezone=UTC')
dd = data.json()
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(data.json())


final={}
list_of_dicts = []
for every in list(dd.keys()):
    try:
        if 'conversions' not in every and 'meta_data' not in every:
            list_of_dicts.append({every:dd.get(every)})
            for each in list_of_dicts:

                for k in dd['conversions']:
                    #print(k.keys())
                    for k_i, k_j in k.items():
                        #print(k_j)
                        for k_j_k, k_j_v in k_j.items():
                            if k_j_k != 'click' and k_j_k != 'conversion_items' and k_j_k != 'conversion_value':
                                #list_of_dicts.append(k_j[k_j_k])
                                #print(k_j[k_j_k])
                                pass

        elif 'conversions' not in every and 'meta_data' not in every:
            final.update({every:dd[every]})
        elif 'meta_data' in every:
            for item in dd['meta_data']:
                final.update({'meta_data':item})

            
    except Exception as e:
        print(e,'this is exception')
    finally:
        if len(final)>1:
            list_of_dicts.append(final) 
print(list_of_dicts)




