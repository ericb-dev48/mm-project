# from airtable import airtable
# at = airtable.Airtable('BASE_ID', 'API_KEY')
# at.get('TABLE_NAME')

BASE_ID = 'appwBalgD73XAwhLX'
API_KEY = 'keykZ089bZEn8NzRb'

from airtable import airtable
at = airtable.Airtable(BASE_ID, API_KEY)
print(at.get('STAFF'))


