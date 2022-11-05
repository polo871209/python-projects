import pandas as pd
import os
import sys


file = os.path.join(sys.path[0], "most_followed_ig.csv")
# Read file as dataframe
df = pd.read_csv(file, encoding='latin-1')
# Select RANK,BRAND columns
rank_brand = pd.DataFrame(df, columns=['RANK', 'BRAND', 'FOLLOWERS'])


def search_rank(name):
    """Search rank from name"""
    res_df = rank_brand[rank_brand['BRAND'].str.startswith(name)]
    return res_df.values.tolist()[0][0]


def search_follower(name):
    """Search follower from name"""
    res_df = rank_brand[rank_brand['BRAND'].str.startswith(name)]
    return res_df.values.tolist()[0][2][:5]


def random_brand(datafram=rank_brand):
    """Generate random brand"""
    return datafram.sample().values.tolist()[0][1]


score = 0
while True:
    brand_1, brand_2 = random_brand(), random_brand()  # Generate guessing brand
    if brand_1 == brand_2:
        brand_2 = random_brand()
    brand_1_rank, brand_2_rank = search_rank(brand_1), search_rank(brand_2)
    brand_1_follower, brand_2_follower = search_follower(
        brand_1), search_follower(brand_2)
    if brand_1_rank > brand_2_rank:
        answer = 'Y'
    else:
        answer = 'N'

    print(f'\'{brand_1}\' has more follower than \'{brand_2}\'')
    guess = input('Y or N: ')

    if answer in guess.upper():
        score += 1
        print(f'Good job! {brand_1}: {brand_1_follower},  {brand_2}: {brand_2_follower}\nScore:{score}')
        continue
    else:
        print(f'Failed! {brand_1}: {brand_1_follower},  {brand_2}: {brand_2_follower}\nScore:{score}')
        break
