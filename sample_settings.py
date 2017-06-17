# here paste nofluffjobs page where you want to search
LOOKUP_URL = 'https://nofluffjobs.com/#/criteria=python%20category=backend'
OUTPUT_FILENAME = 'test.json'

# CSS selectors
OFFERS_SELECTOR = '.col-sm-12.ng-isolate-scope'
LOAD_MORE_SELECTOR = 'more-button'
REQUIREMENTS_SELECTORS = {
    'class': 'ng-scope ng-isolate-scope',
    'qtip': 'item.value'}
SALARY_SELECTOR = {
    'ng-if': 'formData.essentials.salaryFrom'
}
SPECS_SELECTOR = {'class': 'panel border-top2'}

# KEYWORDS
MUST = 'Python'
MUST_NOT = 'Senior'

# OTHER
WAIT_INTERVAL = 2
