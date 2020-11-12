['key',
 'date',
 'wikidata',
 'datacommons',
 'country_code',
 'country_name',
 'subregion1_code',
 'subregion1_name',
 'subregion2_code',
 'subregion2_name',
 'locality_code',
 'locality_name',
 '3166-1-alpha-2',
 '3166-1-alpha-3',
 'aggregation_level',
 'new_confirmed',
 'new_deceased',
 'new_recovered',
 'new_tested',
 'total_confirmed',
 'total_deceased',
 'total_recovered',
 'total_tested',
 'new_hospitalized',
 'total_hospitalized',
 'current_hospitalized',
 'new_intensive_care',
 'total_intensive_care',
 'current_intensive_care',
 'new_ventilator',
 'total_ventilator',
 'current_ventilator',
 'population',
 'population_male',
 'population_female',
 'rural_population',
 'urban_population',
 'largest_city_population',
 'clustered_population',
 'population_density',
 'human_development_index',
 'population_age_00_09',
 'population_age_10_19',
 'population_age_20_29',
 'population_age_30_39',
 'population_age_40_49',
 'population_age_50_59',
 'population_age_60_69',
 'population_age_70_79',
 'population_age_80_89',
 'population_age_90_99',
 'population_age_80_and_older',
 'gdp',
 'gdp_per_capita',
 'human_capital_index',
 'open_street_maps',
 'latitude',
 'longitude',
 'elevation',
 'area',
 'rural_area',
 'urban_area',
 'life_expectancy',
 'smoking_prevalence',
 'diabetes_prevalence',
 'infant_mortality_rate',
 'adult_male_mortality_rate',
 'adult_female_mortality_rate',
 'pollution_mortality_rate',
 'comorbidity_mortality_rate',
 'hospital_beds',
 'nurses',
 'physicians',
 'health_expenditure',
 'out_of_pocket_health_expenditure',
 'mobility_retail_and_recreation',
 'mobility_grocery_and_pharmacy',
 'mobility_parks',
 'mobility_transit_stations',
 'mobility_workplaces',
 'mobility_residential',
 'school_closing',
 'workplace_closing',
 'cancel_public_events',
 'restrictions_on_gatherings',
 'public_transport_closing',
 'stay_at_home_requirements',
 'restrictions_on_internal_movement',
 'international_travel_controls',
 'income_support',
 'debt_relief',
 'fiscal_measures',
 'international_support',
 'public_information_campaigns',
 'testing_policy',
 'contact_tracing',
 'emergency_investment_in_healthcare',
 'investment_in_vaccines',
 'stringency_index',
 'noaa_station',
 'noaa_distance',
 'average_temperature',
 'minimum_temperature',
 'maximum_temperature',
 'rainfall',
 'snowfall',
 'dew_point',
 'relative_humidity']


# STATE NAMES  ['subregion1_name']
[nan,
 'Alaska',
 'Alabama',
 'Arkansas',
 'American Samoa',
 'Arizona',
 'California',
 'Colorado',
 'Connecticut',
 'District of Columbia',
 'Delaware',
 'Florida',
 'Georgia',
 'Guam',
 'Hawaii',
 'Iowa',
 'Idaho',
 'Illinois',
 'Indiana',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Massachusetts',
 'Maryland',
 'Maine',
 'Michigan',
 'Minnesota',
 'Missouri',
 'Northern Mariana Islands',
 'Mississippi',
 'Montana',
 'North Carolina',
 'North Dakota',
 'Nebraska',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'Nevada',
 'New York',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Puerto Rico',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Virginia',
 'Virgin Islands',
 'Vermont',
 'Washington',
 'Wisconsin',
 'West Virginia',
 'Wyoming']



# ## DTYPES

# data.info(109)
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 969075 entries, 0 to 969074
# Data columns (total 109 columns):
#  #   Column                              Dtype  
# ---  ------                              -----  
#  0   Unnamed: 0                          int64  
#  1   key                                 object 
#  2   date                                object 
#  3   wikidata                            object 
#  4   datacommons                         object 
#  5   country_code                        object 
#  6   country_name                        object 
#  7   subregion1_code                     object 
#  8   subregion1_name                     object 
#  9   subregion2_code                     float64
#  10  subregion2_name                     object 
#  11  locality_code                       object 
#  12  locality_name                       object 
#  13  3166-1-alpha-2                      object 
#  14  3166-1-alpha-3                      object 
#  15  aggregation_level                   int64  
#  16  new_confirmed                       float64
#  17  new_deceased                        float64
#  18  new_recovered                       float64
#  19  new_tested                          float64
#  20  total_confirmed                     float64
#  21  total_deceased                      float64
#  22  total_recovered                     float64
#  23  total_tested                        float64
#  24  new_hospitalized                    float64
#  25  total_hospitalized                  float64
#  26  current_hospitalized                float64
#  27  new_intensive_care                  float64
#  28  total_intensive_care                float64
#  29  current_intensive_care              float64
#  30  new_ventilator                      float64
#  31  total_ventilator                    float64
#  32  current_ventilator                  float64
#  33  population                          float64
#  34  population_male                     float64
#  35  population_female                   float64
#  36  rural_population                    float64
#  37  urban_population                    float64
#  38  largest_city_population             float64
#  39  clustered_population                float64
#  40  population_density                  float64
#  41  human_development_index             float64
#  42  population_age_00_09                float64
#  43  population_age_10_19                float64
#  44  population_age_20_29                float64
#  45  population_age_30_39                float64
#  46  population_age_40_49                float64
#  47  population_age_50_59                float64
#  48  population_age_60_69                float64
#  49  population_age_70_79                float64
#  50  population_age_80_89                float64
#  51  population_age_90_99                float64
#  52  population_age_80_and_older         float64
#  53  gdp                                 float64
#  54  gdp_per_capita                      float64
#  55  human_capital_index                 float64
#  56  open_street_maps                    float64
#  57  latitude                            float64
#  58  longitude                           float64
#  59  elevation                           float64
#  60  area                                float64
#  61  rural_area                          float64
#  62  urban_area                          float64
#  63  life_expectancy                     float64
#  64  smoking_prevalence                  float64
#  65  diabetes_prevalence                 float64
#  66  infant_mortality_rate               float64
#  67  adult_male_mortality_rate           float64
#  68  adult_female_mortality_rate         float64
#  69  pollution_mortality_rate            float64
#  70  comorbidity_mortality_rate          float64
#  71  hospital_beds                       float64
#  72  nurses                              float64
#  73  physicians                          float64
#  74  health_expenditure                  float64
#  75  out_of_pocket_health_expenditure    float64
#  76  mobility_retail_and_recreation      float64
#  77  mobility_grocery_and_pharmacy       float64
#  78  mobility_parks                      float64
#  79  mobility_transit_stations           float64
#  80  mobility_workplaces                 float64
#  81  mobility_residential                float64
#  82  school_closing                      float64
#  83  workplace_closing                   float64
#  84  cancel_public_events                float64
#  85  restrictions_on_gatherings          float64
#  86  public_transport_closing            float64
#  87  stay_at_home_requirements           float64
#  88  restrictions_on_internal_movement   float64
#  89  international_travel_controls       float64
#  90  income_support                      float64
#  91  debt_relief                         float64
#  92  fiscal_measures                     float64
#  93  international_support               float64
#  94  public_information_campaigns        float64
#  95  testing_policy                      float64
#  96  contact_tracing                     float64
#  97  emergency_investment_in_healthcare  float64
#  98  investment_in_vaccines              float64
#  99  stringency_index                    float64
#  100 noaa_station                        float64
#  101 noaa_distance                       float64
#  102 average_temperature                 float64
#  103 minimum_temperature                 float64
#  104 maximum_temperature                 float64
#  105 rainfall                            float64
#  106 snowfall                            float64
#  107 dew_point                           float64
#  108 relative_humidity                   float64
# dtypes: float64(94), int64(2), object(13)
# memory usage: 805.9+ MB
    
    
