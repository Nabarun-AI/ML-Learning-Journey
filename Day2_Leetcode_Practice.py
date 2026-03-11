# Leetcode Problem 1 - recyclable and low fat products #1757
# Link - https://leetcode.com/problems/recyclable-and-low-fat-products/
# Topic - Pandas

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return filtered_df[['product_id']]
#=======================================================================================================
#=======================================================================================================

# Leetcode Problem 2 - Big countries #595
# Link - https://leetcode.com/problems/big-countries/description/
# Topic - Panda

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filtered_df=world[(world["area"]>=3000000) | (world["population"]>=25000000)]
    return filtered_df[["name","population","area"]]
#=======================================================================================================
#=======================================================================================================

# Leetcode Problem 3 - Find customer referee #584
# Link - https://leetcode.com/problems/find-customer-referee/description/
# Topic - Panda

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
   X = customer[(customer["referee_id"]!=2) | (customer["referee_id"].isna())]
   return X[["name"]]
#=======================================================================================================
#=======================================================================================================