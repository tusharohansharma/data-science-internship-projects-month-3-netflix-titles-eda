# Top 5 Insights

These findings are based on the 8,807 records in `data/raw/netflix_titles.csv`. Percentages are rounded to one decimal place.

1. **Movies make up most of the catalog.** The dataset contains 6,131 movies (69.6%) and 2,676 TV shows (30.4%), so movies appear about 2.3 times as often as TV shows.

2. **The catalog is concentrated in titles released during the 2010s.** There are 5,927 titles released from 2010 through 2019, or 67.3% of all records. 2018 is the most represented release year, with 1,147 titles.

3. **International Movies and Dramas are the most common categories.** After splitting each title's `listed_in` field into its individual labels, International Movies leads with 2,752 titles, followed by Dramas (2,427) and Comedies (1,674). A title may belong to more than one category.

4. **The United States is the most represented country.** Splitting the `country` field into individual labels gives 3,689 titles for the United States, followed by India (1,046) and the United Kingdom (804). These are country-title credits, not exclusive totals: co-productions can count under multiple countries.

5. **Netflix additions peaked in 2019 in this dataset.** Of the titles with a recorded `date_added`, 2,016 were added in 2019, more than in 2020 (1,879) or 2021 (1,498). Addition year is not the same as release year, and 2021 is only partially represented in this dataset.

## Interpretation notes

- The release-year and addition-year figures describe different events and should not be treated as interchangeable trends.
- Genre and country totals can overlap because titles may have multiple labels or production countries.
- These results describe this dataset snapshot; they do not by themselves establish current Netflix availability or predict future catalog changes.