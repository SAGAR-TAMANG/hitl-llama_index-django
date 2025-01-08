import json

df_dict = {
"over_all_df": "This data frame consists of a single line item showing the top line metrices, dimensions and fields of a campaign. In case the user asks anything about some metric with specifying any added breakdown or filter, or anything about the campaign, you have to refer to this df.",
"daily_df": "This dataframe consists of daily level data of the campaign or the adaccount. Each line item/ row would represent a different date. This data is to be used whenever the user asks about the DoD analysis, or trend analysis, or anything that involves an analysis on the daily level insights of the campaign. Also when there is a query on the day of week analysis, you have to use this data.",
"hourly_df": "Dataframe with hourly level data of the campaign. Each row represents a different hour. This data is to be used whenever the user asks questions that involve hour of the day or time of the day, hourly level trends of a campaign (overall or for some specific days), etc.",
"placements_df": "Dataframe with publisher platform and placement level data of the campaign. Each row represents dimensions and metrics of different publisher platform-placement combinations. Publisher is the first in hierarchy (like Facebook, Insta), and placement is second in hirearcy (like reel, feed, stories, etc.)",
"age_gender_df": "Dataframe with gender and age level data of the camapign. Each row represent a gender and agegroup combination.",
"region_df": "Dataframe with region-level data of the campaign, with several metrics against every region. Each row represents dimensions and metrics in different regions. This will be used to answer any question about the region, location or geography bifurcated metrics.",
"copies_body_asset_df": "This consists of copies of different ads within the campaign with other important dimensions and metrics. This can be used if the user asks specifically about the copies or ads that have performed",
"adsets_df":"This dataframe provides the adset level metrices to anything specific to the adset, you have to refer to this df ",
"ads_specific_df":"This dataframe contains the values regarging the specific ads used , any question related to specic ads and alll you should refer to this dataframe",
}

dfs_description_str = ""

# Iterate through the dictionary items and format them
for df_name, df_description in df_dict.items():
    dfs_description_str += (
        f"DataFrame Name: {df_name}\nDescription: {df_description}\n\n"
    )

select_df_prompt_str = (
"You are an expert Facebook Marketer and Data Analyst and understand all the relevant metrics and dimensions of marketing.\n"
"You will be provided with a query and the previous chat history, and you have to figure out which of the dataframes from the following set would be appropriate to look at for the particular query\n"
"You have the following set of dataframes:\n\n"
f"{dfs_description_str}\n"

"You have to tell me the names of the dataframes which you think are suitable to use for the user's query "
"**It can be a single dataframe, or multiple dataframes. You have to think carefully which all data can be used to answer the query.** In case of multiple dataframes, give me a comma separated list"
"Examples where you may use multiple dataframes can involve general EDA (e.g. give me an overall analysis of my spends [here you can return many dtaframes except the ones which are not at all relevant.]), or if the user asks multiple questions in a single query\n"
"**ONLY RETURN THE NAME OF THE DATAFRAME / DATAFRAMES**\n"

"In case you think that the user's query refers to no dataframe but is a normal chit chat message/ question/ gibberish, and doesn't require any querying to any dataframes, **then simply say 'none'. Nothing else.** \n"

"New query: {query_str},\n\n"

"Previous Context: {chat_history_str}. \n\n"

"Dataframe/ dataframes to be used: "
)



chart_types = {

"table": "to be used when there's data that is simpler to be shown in a tabular format than on charts. This majorly involves analysis of long tail data like the copies, body assets, written text, etc.",

"bar": "to be used when we have to compare a categorical variable with a continuous metric, like day of week with leads, clicks, CTR, spend, or any other metric.",

"line": "also usually to compare understand a trend of a metric wrt a categorical variable, but in this case the categorical variable is likely to have large number of values, like dates",

"pie": "again to compare a metric between categorical variables, but this time the categorical variable is likely to have a small number of values. Like to compare a metric among different publishers (Facebook & Instagram)",

"composed": "to compare two different metrics with a categorical variable, like number of leads and spend with day of week.",

"bubble": "Usually to be used when we are comparing a primary and secondary metric with an additional metric are to be compared for some categorical variable. Like we want to analyse Leads and CPL with placements along with spends for each placement, or Clicks and CPC with age-gender. When asked a question like this, you can also include spends to define the size of the bubble.",

"heatmap": "To identify patterns or relationships between two categorical variables and a continuous metric, like day of week and hour of day with clicks or impressions. Best for understanding concentration or intensity. For example, if you're asked to analyze day of week and hour of day for some metric, you'll return hour of the day for x field, day of the week for y field, and the metric for z field",

"scatter": "To show relationships or correlations between two continuous metrics, like clicks vs spend or leads vs CPL. Useful for identifying trends or outliers.",

"stackedBar": "To compare parts of a whole across categories, like spend breakdown by publisher (Facebook, Instagram, etc.) over different campaigns.",

"funnel": "To represent a sequential process and visualize drop-offs, like leads progressing from clicks to conversions at different stages of the funnel.",
}


chart_types_str = ""

# Iterate through the dictionary items and format them
for chart_name, chart_description in chart_types.items():
    chart_types_str += (
        f"Chart Name: {chart_name}\nDescription: {chart_description}\n\n"
    )

json_format_ = {
    "approach": "<string to define approach to the solution for query>",
    "analytics": [
        {
            "desc": "Short description for the particular analysis",
            "expression": "pandas expression to get data for analytics",
            "visualization_expression": "Pandas expression to get data for visualization. This when applied to the dataframe should transform it into the input for the chart. Only in case if visualization is needed for this particular analysis, otherwise give an empty string",
            "chart_type": "The name of the chart from the list of available charts, in case visualization is applicable, otherwise give an ampty string",
            "chart_title": "Short title for visualization, if visualization is applicable, otherwise give empty string",
            "chart_fields" : "List of different column names of the returned data that need to be used in this particular visualization chart. This should be of the format - [x_field, y_field, z_field, ...]"
        },
    ],
}

json_format_str = json.dumps(json_format_)


instruction_str = (
"1. Understand the query from a very analytical lens and the context (if the query has a dependency on the context), and look at the dataframe columns/ fields provided\n"
"2. Turn that query into executeable Python Scripts **strictly using Pandas**. These scripts majorly return the codes that can transform the data into relevant analyses for analytics and relevant data for visualizations\n"
"3. You need to return a nested json object with these Python scripts. The json would be of the following format:\n"
f"""<json_format>\n{json_format_str}\n</json_format>\n\n"""
"4. The approach essentially defines what will be the steps to get a solution to the query. (In case you see that what the user is asking about is not in the df provided, then mention that it seems like the data is not available and what the user can ask for instead.\n"
"Analytics is a list of dictionaries (format provided above). Each of these dictionaries has thew following fields:\n"
"- desc: a short string description of what this particular analysis is about\n"
"- expression: pandas expression to get the answer for this particular analysis\n"
"- visualization_expression: in case visualization is relevant for this analysis, it would be a pandas expression to get the data for that visualization\n"
"- chart_type: the type of chart that would be relevant for this visualization\n"
"- chart_title: a short title for the chart\n\n"
"- chart_fields: list of fields that are used in the chart. Start with the categorical/ dimension fields and then add the continuous/ metric fields"
"5. When taking care of the analytics part, you have to resolve the main query into relevant analyses that can be used to answer that query. You have to use your understanding of Digital Marketing Analytics and use the right approaches and aggregations wherever required! Make sure that you avoid writing multiple expressions where only a single expression can do the job, for example, if the query asks for top level insights, instead of writing the multipe expressions for different metrics, you can write a single that aggregates different metrics appropriately. In case the expression returns a pandas object only, remember to add '.to_json()' at the end of the expression. **Be smart while writing expressions.**\n"
"6. You have to think carefully before deciding whether visualization is needed or not for each of the analysis you return, for example you don't need a visualization for a query that demands a straight forward single line answer (what is the total spend of my campaign) or whil querying single lineitem dfs like over_all_dataframe.\n"
"While writing the visualization_expressions you have to make sure that the Pandas expression returns the data that would be required as inputs to the chart. You can keep the chronology of the columns such that the main categorical columns come first and the metric columns come later.\n"
"I have the following kinds of charts that are available\n"
f"""<chart_types>\n{chart_types_str}</chart_types>\n\n"""
"""**VERY IMPORTANT - In case of visualizations, the PANDAS EXPRESSION should return a JSON. For this, use `.to_json(orient="records")`**\n"""
"7. The expression parts of all the dictionaries should consist only of the relevant Pandas code\n"
"8. ONLY GIVE THE PANDAS EXPRESSIONS, DO NOT DEFINE ANY VARIABLES IN THE PANDAS EXPRESSIONS, KEEP EACH EXPRESSION INDEPENDENT OF OTHER EXPRESSIONS. Refer to the dataframe as df\n"
"9. DO NOT QUOTE THESE EXPRESSIONS!\n"
)

pandas_prompt_str = (
    "You are an expert Facebook Marketer and Data Analyst and understand all the relevant metrics and dimensions of marketing. "
    "You will be provided with a query, some previous context, and a set of dataframes that are available to you to run some python scripts on to resolve that query\n"
    "I will provide you the heads of the dataframes (df.head()) one by one and you have to follow the following steps to get the relevant analytics from that data.\n\n"
    "<instructions> "
    f"{instruction_str}\n"
    "</instructions>\n\n"
)


query_prompt = (
    "Here's the query:\n"
    "<query> **{query_str}** </query>\n\n"

    "And here's the previous context, **MAKE SURE that you use the following chat history only for the purpose of understanding of understanding the context and nothing else**:\n"
    "<chat_history> {chat_history_str} </chat_history>\n\n"

    "Say yes if you are ready"
)
