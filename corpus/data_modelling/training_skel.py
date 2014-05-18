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
      'field',
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

print rp.T['arcolife']
