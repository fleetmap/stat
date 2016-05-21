import datetime
from django.utils.timezone import get_current_timezone
tz = get_current_timezone()

format = '%b %d %Y %I:%M%p'
date_object = datetime.datetime.strptime('Jun 1 2005  1:33PM', format)
date_obj = tz.localize(date_object)