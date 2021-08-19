import pandas as pd
import random
import string
import datetime


def create_mock(rownum, colnum):
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    for x in range(rownum):
        s1.append(random.randrange(rownum))
        s2.append(random.uniform(0, 1))
        s3.append(random.choice(string.ascii_letters))
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        s4.append(random_date)
        list = ["cat", "dog", "rabbit", "horse", "mouse"]
        s5.append(list[random.randrange(5)])
    df = pd.DataFrame({"s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5})
    for x in range(colnum-5):
        add = df.iloc[:, random.randrange(5)]
        df["s"+str(x+6)] = add

    return df


amount_rows = 3000
amount_cols = 50
a = create_mock(amount_rows, amount_cols)
print(a)

savename = f"./mock_{amount_rows}rowsx{amount_cols}cols.csv"
a.to_csv(savename, index=False)
