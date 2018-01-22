import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# The mo variable name is just a generic name to use for Match objects.
mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My number is 415-555-4242.')
#mo.group(1)
#'415'

#mo.group(2)
#'555-4242'

#mo.group(0)
#'415-555-4242'

#mo.group()
#'415-555-4242'

#the plural groups(), will retrieve all the groups at once
#mo.groups()
#('415', '555-4242')

areaCode, mainNumber = mo2.groups()
print(areaCode)
#415
print(mainNumber)
#555-4242