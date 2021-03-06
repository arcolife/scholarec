import pandas as pd

# steps to form a skeleton for sample training data of ratings
'''
# here fields used are: Physics, Probability & Mathematics (in order)
# total entries ~43 (around 15 for each)
 
id = ['1401.0828v1',
      '1010.5976v1',
      '0706.0750v2',
      '1103.4289v1',
      '0611347v1',
      '1304.3144v1',
      '9809193v1',
      '1310.0361v1',
      '0207047v3',
      '9509004v1',
      '0008244v1',
      '0701181v1',
      '1304.1684v1',
      '1101.0426v1',
      '0911.4426v1',
      '0701121v1',
      '1402.5513v1',
      '0305165v1',
      '0212092v1',
      '1007.3838v1',
      '1201.3611v1',
      '0604144v1',
      '9803035v2',
      '1106.1524v1',
      '1108.5491v1',
      '0907.5143v2',
      '0501183v1',
      '0903.4244v1',
      '0608268v1',
      '0203017v1',
      '0901.0902v2',
      '1110.3036v1',
      '1306.1166v1',
      '0205220v2',
      '1011.1841v1',
      '0504141v1',
      '0808.2923v2',
      '0610139v1',
      '0004030v1',
      '0509171v1',
      '1310.3473v1']

uid = ['arcolife',
       'caftlegs',
       'AnonymousUser',
       'ArchitSharmacfe32b0780384656',
       'arcolife7a0cc2bd622c4127',
       'arcshams',
       'ArchitSharma']

data = pd.DataFrame(columns=list(set(id)), index=uid)
data.unstack().to_csv('sample.csv')

# now add this as the first line of the csv: 
# paper_id,user_id,rating
'''

rating  = pd.read_csv('sample.csv')
rp = rating.pivot_table(cols=['paper_id'], rows=['user_id'], values='rating')

# print rating

print "\nIndex: \n",rp.index
print "\nColumns: \n",rp.columns
print "\nValues: \n",rp.values

#print rp.T.to_string() 

# Access through rp.T['arcolife'] 
# or through rp.ix['arcolife']
# or rating.user_id / rating.paper_id

# rp.T.to_html('sample.html')
# rp.T.to_json('sample.json')


''' 
# Collaborative filtering is done through the following:
# provided there are required amount of ratings present 
# in cells of the matrix, using Pearson correlation score
rating_arcolife = rp.T['arcolife']
sim_arcolife = rp.corrwith(rp.T['arcolife'])

# To make recommendation for Toby, we calculate a rating 
# of others weighted by the similarity. Note that we only 
# need to calculate rating for movies Toby has not yet seen. 
# The first line below filter out irrelevant data. It then 
# assigns the similarity score and the weighted rating.

papers = ((rating_arcolife[rating.paper_id].isnull()) & (rating.user_id != 'arcolife')).values
rating_c = rating[papers]
rating_c['similarity'] = rating_c['user_id'].map(sim_arcolife.get)
rating_c['sim_rating'] = rating_c.similarity * rating_c.rating

print rating_c
'''
