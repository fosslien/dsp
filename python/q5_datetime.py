# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

from datetime import datetime

d0 = datetime.strptime('01-02-2013', '%m-%d-%Y')
d1 = datetime.strptime('07-28-2015', '%m-%d-%Y')
print d1 - d0
 

####b)  
date_start = '12312013'  
date_stop = '05282015'  

from datetime import datetime

d0 = datetime.strptime('12312013', '%m%d%Y')
d1 = datetime.strptime('05282015', '%m%d%Y')
print d1 - d0


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

from datetime import datetime

d0 = datetime.strptime('15-Jan-1994', '%d-%b-%Y')
d1 = datetime.strptime('14-Jul-2015', '%d-%b-%Y')
print d0 - d1
