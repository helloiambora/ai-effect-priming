# Data dictionary

## `trials_anonymized.csv`

One row per response, 20 rows per participant (780 rows, 39 participants). This is the Resultal export with timestamps and platform IDs removed and participant IDs replaced by codes.

| Column | Meaning |
|---|---|
| `participant` | anonymised participant code (P01 to P39, shuffled) |
| `question_type` | `CRT`, `LOGIC` or `TRIVIA` for the ten task questions, empty for the cover task and demographics |
| `question_id` | which question: `CRT1`–`CRT4`, `Logic1`–`Logic2`, `Trivia1`–`Trivia4`, the five demographic questions, or a number for the cover task pairs |
| `response` | the answer given. For the cover task this is the file name of the chosen image |
| `accuracy` | `Correct`, `Wrong` or `I don't know` (task questions only) |
| `attribute` | cover task only: whether the left or right image was chosen |
| `response_time` | time spent on this question, in milliseconds |
| `task_id` | Resultal's ID for the block the question belongs to |
| `experiment_id` | condition: `Neutral Condition`, `Google Effect Control`, `AI Semantic Priming` or `AI Brand Priming` |
| `time_elapsed` | time since the start of the experiment, in milliseconds |

Note: the correct answer to `CRT3` is the word `None`. Read the file with `keep_default_na=False`, otherwise pandas turns it into a missing value.

## `participants_clean.csv`

One row per participant (39 rows), created by `notebooks/01_data_cleaning.ipynb`.

| Column | Meaning |
|---|---|
| `participant` | participant code |
| `condition` | `Neutral`, `Google control`, `AI semantic` or `AI brand` |
| `n_trials` | number of task questions answered (always 10) |
| `prop_correct`, `prop_wrong`, `prop_idk` | share of the ten questions answered correctly, wrongly, or with "I don't know". They add up to 1 |
| `median_rt_s`, `mean_rt_s` | median and mean response time on the ten questions, in seconds |
| `acc_when_attempted` | correct answers as a share of the questions that were attempted (not answered with "I don't know") |
| `n_idk` | number of "I don't know" answers |
| `giveup_median_s`, `giveup_mean_s` | median and mean time before choosing "I don't know", in seconds. Empty for participants who never chose it |
| `crt_correct`, `crt_wrong`, `crt_idk` | the three shares for the four CRT items only |
| `logic_correct`, `logic_wrong`, `logic_idk` | the same for the two logic questions |
| `trivia_correct`, `trivia_wrong`, `trivia_idk` | the same for the four trivia questions |
| `crt_lure_rate` | share of CRT items answered with the intuitive but wrong "lure" answer |
| `age`, `gender`, `education` | self-reported, in categories |
| `english` | self-reported English proficiency: `A1-A2`, `B1-B2`, `C1-C2` or `Native` |
| `english_high` | `True` for C1-C2 and Native |
| `ai_use` | self-reported frequency of AI tool use |
| `ai_use_num` | the same as a number: 1 = rarely or never, 2 = a few times a month, 3 = a few times a week, 4 = daily |
| `cover_median_rt_s` | median time per choice in the cover task (where the prime was shown), in seconds |
| `total_duration_s` | total time from start to last answer, in seconds |
| `flag_clickthrough` | `True` if the participant spent less than 0.5 s per cover task choice. These two participants are excluded from the main analysis |
