import pandas as pd
import os
import sys


file = os.path.join(sys.path[0], "most_followed_ig.csv")
# Read file as dataframe
df = pd.read_csv(file, encoding='latin-1')
# Select RANK,BRAND columns
rank_brand = pd.DataFrame(df, columns=['RANK', 'BRAND', 'FOLLOWERS'])


def rank_follower(name):
    """Search rank and follower from name"""
    res_df = rank_brand[rank_brand['BRAND'].str.startswith(name)]
    lst = res_df.values.tolist()
    return lst[0][0], lst[0][2][:5]


def random_brand(datafram=rank_brand):
    """Generate random brand"""
    return datafram.sample().values.tolist()[0][1]


if __name__ == '__main__':
    score = 0
    while True:
        brand_1, brand_2 = random_brand(), random_brand()  # Generate random brands
        if brand_1 == brand_2:  # incase duplicate brands
            brand_2 = random_brand()
        b1_rank, b1_follower = rank_follower(brand_1)
        b2_rank, b2_follower = rank_follower(brand_2)
        if b1_rank < b2_rank:  # whcik brand had more followers
            answer = 'Y'
        else:
            answer = 'N'
        print(f'\'{brand_1}\' has more follower than \'{brand_2}\'')
        guess = input('Y or N: ')  # input guess

        if answer in guess.upper():  # get score if correct, end if incorrect
            score += 1
            print(
                f'Good job! {brand_1}: {b1_follower},  {brand_2}: {b2_follower}\nScore:{score}')
            continue
        else:
            print(
                f'Failed! {brand_1}: {b1_follower},  {brand_2}: {b2_follower}\nScore:{score}')
            break
