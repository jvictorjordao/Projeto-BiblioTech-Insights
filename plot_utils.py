import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# Function to create a generical bar plot
def create_bar_plot(dataframe, column_name, aggregation_column, graph_title=None):
    df_plot = dataframe.groupby(column_name).agg({aggregation_column:'sum'}).reset_index()
    df_plot = df_plot.sort_values(aggregation_column, ascending=False).round(2)
    if graph_title is None:
        graph_title =f'{column_name.replace("_", " ").title()} by {aggregation_column.replace("_", " ").title()}'

    fig = px.bar(
    df_plot,
    x=column_name,
    y=aggregation_column,
    title=graph_title,
    color_discrete_sequence=['seagreen']
    )

    fig.update_layout(
    template='plotly_white',
    title_font_size=16,
    xaxis_title=column_name.replace("_", " ").title(),
    yaxis_title=aggregation_column.replace("_", " ").title(),
    height=600,
    width=800
    )

    fig.show()

# Function to create a box plot for any numeric column
def create_box_plot(dataframe, column_name, graph_title=None):
    if graph_title is None:
        graph_title = f'Box Plot Distribution of {column_name.replace('_', ' ').title()}'

    fig = px.box(
        dataframe,
        x=column_name,
        title=graph_title,
        labels={column_name: f'{column_name.replace('_', ' ').title()} Amount'},
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

    grouped_df = grouped_df.sort_values(aggregation_column, ascending=False).round(2).reset_index()

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
        template='plotly_white',
        height=800,
        width=1200
    )

    fig.show()

# Function to create a vertical bar graph for aggregated high values but normalized
def create_vertical_high_value_bar_plot_normalized(dataframe, column_name, aggregation_column, graph_title=None, quantile=0.75):
    high_value_threshold = dataframe[aggregation_column].quantile(quantile)

    filtered_df = dataframe[dataframe[aggregation_column] >= high_value_threshold]

    grouped_df = filtered_df.groupby(column_name).agg(
        total_revenue=(aggregation_column, 'sum'),
        books_count=('isbn', 'count')
    ).reset_index()

    grouped_df['proportional'] = grouped_df['total_revenue'] / grouped_df['books_count']

    grouped_df = grouped_df.sort_values('proportional', ascending=False).round(2).reset_index()

    if graph_title is None:
        graph_title = f'Highest {aggregation_column.replace('_', ' ').title()} by {column_name.replace('_', ' ').title()} (Normalized)'

    fig = px.bar(
        grouped_df,
        x=column_name,
        y='proportional',
        title=graph_title,
        labels={column_name: column_name.replace('_', ' ').title(), 'proportional': aggregation_column.replace('_', ' ').title()+' per book'},
        color_discrete_sequence=['darkgreen']
    )

    fig.update_layout(
        template='plotly_white',
        height=800,
        width=1200
    )

    fig.show()


# Function to create a vertical bar graph for aggregated high values and a line plot for the normalized values
def create_vertical_high_value_bar_line_plot(df, column_name, aggregation_column, graph_title=None, quantile=0.75, legend_pos=[0.95, 0.95]):
    high_value_threshold = df[aggregation_column].quantile(quantile)

    filtered_df = df[df[aggregation_column] >= high_value_threshold]

    grouped_df = filtered_df.groupby(column_name).agg(
        total_revenue=(aggregation_column, 'sum'),
        books_count=('isbn', 'count')
    ).reset_index()

    grouped_df['normalized_sales'] = grouped_df['total_revenue'] / grouped_df['books_count']

    grouped_df = grouped_df.sort_values('total_revenue', ascending=False).round(2).reset_index()

    if graph_title is None:
        graph_title = f'{aggregation_column.replace("_", " ").title()} and {aggregation_column.replace("_", " ").title()} Normalized by {column_name.replace("_", " ").title()}'

    fig = go.Figure()

    # Adicionar barras para as vendas totais (eixo primário)
    fig.add_trace(go.Bar(
        x=grouped_df[column_name],
        y=grouped_df['total_revenue'],
        name=f'{aggregation_column.replace("_", " ").title()}',
        marker_color='seagreen'
    ))

    # Adicionar linha para as vendas normalizadas (eixo secundário)
    fig.add_trace(go.Scatter(
        x=grouped_df[column_name],
        y=grouped_df['normalized_sales'],
        name=f'{aggregation_column.replace("_", " ").title()} Normalized by book',
        mode='lines+markers',
        marker_color='royalblue',
        yaxis='y2'
    ))

    # Atualizar layout para dois eixos Y
    fig.update_layout(
        title=graph_title,
        xaxis_title=f'{column_name.replace("_", " ").title()}',
        yaxis=dict(
            title=f'{aggregation_column.replace("_", " ").title()}',
            title_font_color='seagreen',
            tickfont_color='seagreen'
        ),
        yaxis2=dict(
            title=f'{aggregation_column.replace("_", " ").title()} Normalized',
            overlaying='y',
            side='right',
            tickmode='sync',
            title_font_color='royalblue',
            tickfont_color='royalblue'
        ),
        legend=dict(y=legend_pos[1], xanchor='right', x=legend_pos[0]),
        template="plotly_white",
        height=800,
        width=1200
    )

    fig.show()

def plot_top_quartile_and_sales(df, column_name, aggregation_column, graph_title=None, quantile=0.5, legend_pos=[0.5, 1.1]):
    high_value_threshold = df[aggregation_column].quantile(quantile)

    filtered_df = df[df[aggregation_column] >= high_value_threshold].sort_values(aggregation_column, ascending=False)

    if graph_title is None:
        graph_title = f'Top quartile {aggregation_column.replace("_", " ").title()} and {column_name.replace("_", " ").title()}'

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=filtered_df['title'],
        y=filtered_df[aggregation_column],
        name=f'{aggregation_column.replace("_", " ").title()}',
        marker_color='seagreen'
    ))

    fig.add_trace(go.Scatter(
        x=filtered_df['title'],
        y=filtered_df[column_name],
        name=f'{column_name.replace("_", " ").title()}',
        mode='lines+markers',
        marker_color='royalblue',
        yaxis='y2'
    ))

    fig.update_layout(
        title=graph_title,
        xaxis_title='Book Title',
        yaxis=dict(
            title=f'{aggregation_column.replace("_", " ").title()}',
            title_font_color='seagreen',
            tickfont_color='seagreen',
            range=[filtered_df[aggregation_column].min()-0.1, filtered_df[aggregation_column].max()+0.1]
        ),
        yaxis2=dict(
            title=f'{column_name.replace("_", " ").title()}',
            overlaying='y',
            side='right',
            tickmode='sync',
            title_font_color='royalblue',
            tickfont_color='royalblue'
        ),
        template="plotly_white",
        height=600,
        width=1400,
        legend=dict(orientation="h", x=legend_pos[0], y=legend_pos[1])
    )

    fig.show()