import csv
import ast
#from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
#from cassandra.policies import WhiteListRoundRobinPolicy, DowngradingConsistencyRetryPolicy
#from cassandra.query import tuple_factory
#
#profile = ExecutionProfile(
#    load_balancing_policy=WhiteListRoundRobinPolicy(['127.0.0.1']),
#    retry_policy=DowngradingConsistencyRetryPolicy(),
#    consistency_level=ConsistencyLevel.LOCAL_QUORUM,
#    serial_consistency_level=ConsistencyLevel.LOCAL_SERIAL,
#    request_timeout=15,
#    row_factory=tuple_factory
#)
#cluster = Cluster(execution_profiles={EXEC_PROFILE_DEFAULT: profile})
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('mc_transactions')

#rows = session.execute("describe tables")
#for row in rows:
    #print(row)

with open('TRANSACTION_DATA/young_adults_male_urban_5000-5999.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    session.execute("CREATE TABLE transaction_by_merchant ( ssn text, cc_num text, first text, last text, gender text, street text, city text, state text, zip text, lat text, long text, city_pop text, job text, dob text, acct_num text, profile text, trans_num text, trans_date text, trans_time text, unix_time text, category text, amt text, is_fraud text, merchant text, merch_lat text, merch_long text, PRIMARY KEY ((merchant), trans_num));")
    for row in reader:
        #print(row.keys())
        #row = ast.literal_eval(row)
#        row['lat'] = ast.literal_eval(row['lat'])
        #import ipdb; ipdb.set_trace()
        print(row)
        #query = f'INSERT INTO transaction_by_merchant {tuple(row.keys())} '.replace('\'','\"') + f'VALUES{tuple(row.values())}'
        query = """
            INSERT INTO transaction_by_merchant (ssn, cc_num, first, last,
            gender, street, city, state, zip, lat, long, city_pop, job,
            dob, acct_num, profile, trans_num, trans_date, trans_time,
            unix_time, category, amt, is_fraud, merchant, merch_lat, merch_long
            ) 
            VALUES (%(ssn)s, %(cc_num)s, %(first)s, %(last)s,
            %(gender)s, %(street)s, %(city)s, %(state)s, %(zip)s, %(lat)s, %(long)s, %(city_pop)s, %(job)s,
            %(dob)s, %(acct_num)s, %(profile)s, %(trans_num)s, %(trans_date)s, %(trans_time)s,
            %(unix_time)s, %(category)s, %(amt)s, %(is_fraud)s, %(merchant)s, %(merch_lat)s, %(merch_long)s
            )
            """
        print(query)
        session.execute(query, row)
        #break
