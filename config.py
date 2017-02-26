# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:2412luke@flasktest.ctevqckl1xy1.us-west-2.rds.amazonaws.com:3306/'
# Uncomment the line below if you want to work with a local DB
#secret access key for flaskdemo user in admin group
# /ebtaannHvwOB8s7OlFWnsIkSBOH9GwAmfqfRZG2
#access key ID 
# AKIAIENDO6BQDAUBGN6A
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
