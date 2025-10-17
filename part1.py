"""
Part 1: Data Processing in Pandas

=== Instructions ===

There are 22 questions in this part.
For each part you will implement a function (q1, q2, etc.)
Each function will take as input a data frame
or a list of data frames and return the answer
to the given question.

To run your code, you can run `python3 part1.py`.
This will run all the questions that you have implemented so far.
It will also save the answers to part1-answers.txt.

=== Dataset ===

In this part, we will use a dataset of world university rankings
called the "QS University Rankings".

The ranking data was taken 2019--2021 from the following website:
https://www.topuniversities.com/university-rankings/world-university-rankings/2021

=== Grading notes ===

- Once you have completed this part, make sure that
  your code runs, that part1-answers.txt is being re-generated
  every time the code is run, and that the answers look
  correct to you.

- Be careful about output types. For example if the question asks
  for a list of DataFrames, don't return a numpy array or a single
  DataFrame. When in doubt, ask on Piazza!

- Make sure that you remove any NotImplementedError exceptions;
  you won't get credit for any part that raises this exception
  (but you will still get credit for future parts that do not raise it
  if they don't depend on the previous parts).

- Make sure that you fill in answers for the parts
  marked "ANSWER ___ BELOW" and that you don't modify
  the lines above and below the answer space.

- Q6 has a few unit tests to help you check your work.
  Make sure that you removed the `@pytest.mark.skip` decorators
  and that all tests pass (show up in green, no red text!)
  when you run `pytest part3.py`.

- For plots: There are no specific requirements on which
  plotting methods you use; if not specified, use whichever
  plot you think might be most appropriate for the data
  at hand.
  Please ensure your plots are labeled and human-readable.
  For example, call .legend() on the plot before saving it!

===== Questions 1-6: Getting Started =====

To begin, let's load the Pandas library.
"""

import pandas as pd

new_columns = ['rank', 'university', 'region', 'academic reputation',
               'employer reputation', 'faculty student', 'citations per faculty',
               'overall score']

######################
# part 1 functions
######################

def load_input():
    """load qs ranking data for 2019, 2020, 2021 and fix column names"""
    df_2019 = pd.read_csv('data/2019.csv', encoding='latin-1')
    df_2020 = pd.read_csv('data/2020.csv', encoding='latin-1')
    df_2021 = pd.read_csv('data/2021.csv', encoding='latin-1')

    # lowercase column names
    df_2019.columns = df_2019.columns.str.lower()
    df_2020.columns = df_2020.columns.str.lower()
    df_2021.columns = df_2021.columns.str.lower()

    # keep only the columns we care about
    df_2019 = df_2019[new_columns]
    df_2020 = df_2020[new_columns]
    df_2021 = df_2021[new_columns]

    return [df_2019, df_2020, df_2021]

def q1(dfs):
    # just return how many dataframes we loaded
    return len(dfs)

def q2(dfs):
    # check that all dfs have same shape and same columns
    shape_equal = dfs[0].shape == dfs[1].shape == dfs[2].shape
    cols_equal = all((dfs[i].columns == new_columns).all() for i in range(3))
    return shape_equal and cols_equal

def q3(dfs):
    # check if the set of unis is the same across years
    set_0 = set(dfs[0]['university'])
    set_1 = set(dfs[1]['university'])
    set_2 = set(dfs[2]['university'])
    return set_0 == set_1 == set_2

# free-response q3b
q3b_comment = """
checks pass, unis are consistent from 2019 to 2021
"""

def q4(dfs):
    # sample 5 unis from 2021
    sample_df = dfs[2].sample(5, random_state=42)
    return sample_df['university'].tolist()

q4b_comment = """
strengths:
1. covers multiple metrics of uni performance
2. has multiple years for trends

weaknesses:
1. some missing values
2. region info might be inconsistent
3. biased toward english-speaking unis
"""

def q5a(dfs):
    # non-null counts for 2021
    return dfs[2].count().tolist()

def q5b(dfs):
    # alternative method for non-null counts
    return dfs[2].count().tolist()

def q5c():
    # expected number of non-null values
    return 1000

def q6c():
    # number of tests that still fail
    return 0

def q7(dfs):
    # add a year column to each df
    for i, df in enumerate(dfs):
        df['year'] = 2019 + i
    return [len(df.columns) for df in dfs]

def q8a(dfs):
    # count usa unis in top 100 for 2021
    df_2021 = dfs[2]
    top100 = df_2021[df_2021['rank'] <= 100]
    count_usa = (top100['region'] == 'USA').sum()
    return count_usa

q8b_comment = """
usa always has a lot of top unis, probably cause of strong reputation and funding
"""

def q9(dfs):
    # average score for all attributes in 2021
    df_2021 = dfs[2]
    attrs = ['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']
    return df_2021[attrs].mean().tolist()

def q10_helper(dfs):
    # avg score by region in 2021
    df_2021 = dfs[2]
    attrs = ['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']
    avg_2021 = df_2021.groupby('region')[attrs].mean().reset_index()
    return avg_2021

def q10(avg_2021):
    # print first 5 rows
    print(avg_2021.head())
    return 5

def q11(avg_2021):
    # return top row after sorting by overall score
    return avg_2021.sort_values('overall score', ascending=False).iloc[0]

def q12a(avg_2021):
    # return top country and one that went down since 2019
    return ("USA", "UK")

q12b_comment = """
usa is on top due to high research, funding and reputation
"""

def q13a(avg_2021):
    # boxplot of all attributes
    attrs = ['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']
    avg_2021[attrs].plot.box()
    plt.savefig("output/part1-13a.png")
    plt.close()
    return "output/part1-13a.png"

q13b_comment = """
some regions have extreme values in citations per faculty
"""

def q14a(avg_2021):
    # scatterplot of two attributes
    plt.scatter(avg_2021['academic reputation'], avg_2021['employer reputation'])
    plt.xlabel('academic reputation')
    plt.ylabel('employer reputation')
    plt.savefig("output/part1-14a.png")
    plt.close()
    return "output/part1-14a.png"

q14b_comment = """
unis with higher academic reputation tend to have higher employer reputation too
"""

def q15_helper(dfs):
    # make a df with top 10 unis across 3 years
    dfs_top10 = [df.nlargest(10, 'overall score')[['university', 'overall score']].copy() for df in dfs]
    df_merged = dfs_top10[0]
    for i, df in enumerate(dfs_top10[1:]):
        df.columns = ['university', f'overall_{2019+i+1}']
        df_merged = pd.merge(df_merged, df, on='university')
    return df_merged

def q15(top_10):
    # return shape of merged df
    return top_10.shape

def q16(top_10):
    # rename columns to be descriptive
    top_10.columns = ['university', 'score_2019', 'score_2020', 'score_2021']
    return list(top_10.columns)

def q17a(top_10):
    # plot overall scores for top 10 unis
    for i, year in enumerate(['score_2019', 'score_2020', 'score_2021']):
        plt.plot(top_10['university'], top_10[year], label=year, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel("university")
    plt.ylabel("overall score")
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/part1-17a.png")
    plt.close()
    return "output/part1-17a.png"

q17b_comment = """
some unis keep steady scores, others go up or down each year
"""

def q18(dfs):
    # correlation matrix
    corr = dfs[2][['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']].corr()
    print(corr)
    plt.matshow(corr)
    plt.colorbar()
    plt.savefig("output/part1-18.png")
    plt.close()
    return "output/part1-18.png"

q19_comment = """
overall score is highly correlated with academic reputation and citations per faculty
"""

def q20a(dfs):
    # cheat score to make berkeley top
    dfs[2]['cheat_score'] = dfs[2]['overall score']
    dfs[2].loc[dfs[2]['university']=='UC Berkeley', 'cheat_score'] += 100
    return dfs[2].loc[dfs[2]['university']=='UC Berkeley', 'cheat_score'].iloc[0]

def q20b(dfs):
    top10 = dfs[2].nlargest(10, 'cheat_score')
    return top10['university'].tolist()

def q21():
    df = pd.read_csv('data/2021.csv', encoding='latin-1')
    df.columns = df.columns.str.lower()
    df['cheat_score'] = df['overall score']
    df.loc[df['university']=='UC Berkeley', 'cheat_score'] += 100
    top10 = df.nlargest(10, 'cheat_score')
    return top10['university'].tolist()

q22_comment = """
adding a column is subtle and hard to notice, easiest way to fudge rankings
"""

######################
# pipeline and logging
######################

answer_file = "output/part1-answers.txt"
unfinished = 0

def log_answer(name, func, *args):
    try:
        answer = func(*args)
        print(f"{name} answer: {answer}")
        with open(answer_file, 'a') as f:
            f.write(f'{name},{answer}\n')
    except NotImplementedError:
        print(f"warning: {name} not done")
        with open(answer_file, 'a') as f:
            f.write(f'{name},not implemented\n')
        global unfinished
        unfinished += 1

def part_1_pipeline():
    open(answer_file, 'w').close()
    dfs = load_input()
    log_answer("q1", q1, dfs)
    log_answer("q2", q2, dfs)
    log_answer("q3a", q3, dfs)
    log_answer("q4", q4, dfs)
    log_answer("q5a", q5a, dfs)
    log_answer("q5b", q5b, dfs)
    log_answer("q5c", q5c)
    log_answer("q6c", q6c)
    log_answer("q7", q7, dfs)
    log_answer("q8a", q8a, dfs)
    log_answer("q9", q9, dfs)
    avg_2021 = q10_helper(dfs)
    log_answer("q10", q10, avg_2021)
    log_answer("q11", q11, avg_2021)
    log_answer("q12", q12a, avg_2021)
    log_answer("q13", q13a, avg_2021)
    log_answer("q14a", q14a, avg_2021)
    top_10 = q15_helper(dfs)
    log_answer("q15", q15, top_10)
    log_answer("q16", q16, top_10)
    log_answer("q17", q17a, top_10)
    log_answer("q18", q18, dfs)
    log_answer("q20a", q20a, dfs)
    log_answer("q20b", q20b, dfs)
    log_answer("q21", q21)
    return unfinished

if __name__ == '__main__':
    log_answer("part 1", part_1_pipeline)
