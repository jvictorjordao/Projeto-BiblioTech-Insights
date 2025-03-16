import pandas as pd
import plotly.express as px

# Function to create a horizontal bar graph for any categorical column
def create_horizontal_bar_plot(dataframe, column_name, graph_title=None):
    df_plot = dataframe[column_name].value_counts().reset_index()
    df_plot.columns = [column_name.replace('_', ' ').title(), 'Count']
    df_plot = df_plot.sort_values('Count', ascending=True)
    if graph_title is None:
        graph_title =f'{df_plot.columns[0]} distribution'

    fig = px.bar(
    df_plot,
    x=df_plot.columns[1],
    y=df_plot.columns[0],
    title=graph_title,
    orientation='h',
    color_discrete_sequence=['seagreen']
    )

    fig.update_layout(
    template='plotly_white',
    title_font_size=16,
    xaxis_title='Count',
    yaxis_title=df_plot.columns[0],
    height=600,
    width=800
    )

    fig.show()

# Function to create a vertical bar graph for any categorical column
def create_vertical_bar_plot(dataframe, column_name, graph_title=None):
    df_plot = dataframe[column_name].value_counts().reset_index()
    df_plot.columns = [column_name.replace('_', ' ').title(), 'Count']
    df_plot = df_plot.sort_values('Count', ascending=False)
    if graph_title is None:
        graph_title =f'{df_plot.columns[0]} distribution'

    fig = px.bar(
    df_plot,
    x=df_plot.columns[0],
    y=df_plot.columns[1],
    title=graph_title,
    color_discrete_sequence=['seagreen']
    )

    fig.update_layout(
    template='plotly_white',
    title_font_size=16,
    xaxis_title=df_plot.columns[0],
    yaxis_title='Count',
    height=600,
    width=800
    )

    fig.show()

# Function to create a box plot for any numeric column
def create_box_plot(dataframe, column_name, graph_title=None):
    if graph_title is None:
        graph_title = f'Box Plot Distribution of {column_name.title()}'

    fig = px.box(
        dataframe,
        x=column_name,
        title=graph_title,
        labels={column_name: f'{column_name.title()} Amount'},
        color_discrete_sequence=['seagreen']
    )
    fig.update_layout(
        template='plotly_white',
        height=400,
        width=1000
    )
    fig.show()

# Function to create a horizontal bar graph for aggregated high values
def create_horizontal_high_value_bar_plot(dataframe, column_name, aggregation_column, graph_title=None, quantile=0.75):
    high_value_threshold = dataframe[aggregation_column].quantile(quantile)

    filtered_df = dataframe[dataframe[aggregation_column] >= high_value_threshold]

    grouped_df = filtered_df.groupby(column_name, as_index=False).agg({
        aggregation_column: 'sum'
    })

    grouped_df = grouped_df.sort_values(aggregation_column, ascending=True).round(2)

    if graph_title is None:
        graph_title = f'Highest {aggregation_column.replace('_', ' ').title()} by {column_name.replace('_', ' ').title()}'

    fig = px.bar(
        grouped_df,
        x=aggregation_column,
        y=column_name,
        title=graph_title,
        labels={column_name: column_name.replace('_', ' ').title(), aggregation_column: aggregation_column.replace('_', ' ').title()},
        orientation='h',
        color_discrete_sequence=['seagreen']
    )

    fig.update_layout(
        # xaxis_title=aggregation_column.replace('_', ' ').title(),
        # yaxis_title=column_name.replace('_', ' ').title(),
        template='plotly_white',
        height=800,
        width=1200
    )

    fig.show()

# Function to create a vertical bar graph for aggregated high values
def create_vertical_high_value_bar_plot(dataframe, column_name, aggregation_column, graph_title=None, quantile=0.75):
    high_value_threshold = dataframe[aggregation_column].quantile(quantile)

    filtered_df = dataframe[dataframe[aggregation_column] >= high_value_threshold]

    grouped_df = filtered_df.groupby(column_name, as_index=True).agg({
        aggregation_column: 'sum'
    })

    grouped_df = grouped_df.sort_values(aggregation_column, ascending=False).round(2)

    if graph_title is None:
        graph_title = f'Highest {aggregation_column.replace('_', ' ').title()} by {column_name.replace('_', ' ').title()}'

    fig = px.bar(
        grouped_df,
        x=column_name,
        y=aggregation_column,
        title=graph_title,
        labels={column_name: column_name.replace('_', ' ').title(), aggregation_column: aggregation_column.replace('_', ' ').title()},
        color_discrete_sequence=['seagreen']
    )

    fig.update_layout(
        # xaxis_title=column_name.replace('_', ' ').title(),
        # yaxis_title=aggregation_column.replace('_', ' ').title(),
        template='plotly_white',
        height=800,
        width=1200
    )

    fig.show()