DB_PATH = '/home/airflow/dags/Lead_scoring_data_pipeline/database/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'

DATA_DIRECTORY = '/home/airflow/dags/Lead_scoring_data_pipeline/data/'
INTERACTION_MAPPING = '/home/airflow/dags/Lead_scoring_data_pipeline/mapping/interaction_mapping.csv'


INDEX_COLUMNS_TRAINING = ['created_date', 'city_tier', 'first_platform_c',
                'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped',
                'referred_lead', 'app_complete_flag']

INDEX_COLUMNS_INFERENCE = ['created_date', 'city_tier', 'first_platform_c',
                'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped',
                'referred_lead']



