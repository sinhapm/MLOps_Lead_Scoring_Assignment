# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/home/Assignment/unit_test/'
DB_FILE_NAME = 'utils_output.db'

# DB_PATH = '/home/airflow/dags/Lead_scoring_data_pipeline/database/'
# DB_FILE_NAME = 'lead_scoring_data_cleaning.db'


DATA_DIRECTORY = '/home/Assignment/unit_test/'
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'

DATA_FILE = 'leadscoring_test.csv'

INTERACTION_MAPPING = '/home/Assignment/unit_test/interaction_mapping.csv'


INDEX_COLUMNS_TRAINING = ['created_date', 'city_tier', 'first_platform_c',
                'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped',
                'referred_lead', 'app_complete_flag']

INDEX_COLUMNS_INFERENCE = ['created_date', 'city_tier', 'first_platform_c',
                'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped',
                'referred_lead']

