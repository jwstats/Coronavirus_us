import data_clean
from data_clean import daily_totals, start_time
import time
import plotly.offline as pyo
import plotly.graph_objects as go


if __name__ == "__main__":
    pass
else:
    print('\n4: {} module imported'.format(__name__))

    #### Plots ####
    frames = []
    for frame in range(len(daily_totals)):
        # while len(frames) <= len(daily_totals)-1:  # While loop to limit frames
        confirmed = go.Scatter(x=daily_totals.iloc[:frame+1]['ObservationDate'], y=daily_totals.iloc[:frame+1]
                               ['Confirmed'], name='Confirmed', marker=dict(color="#51ABFB"))
        deaths = go.Scatter(x=daily_totals.iloc[:frame+1]['ObservationDate'], y=daily_totals.iloc[:frame+1]
                            ['Deaths'], name='Deaths', marker=dict(color="#EA2916"))
        recovered = go.Scatter(x=daily_totals.iloc[:frame+1]['ObservationDate'], y=daily_totals.iloc[:frame+1]
                               ['Recovered'], name='Recovered', marker=dict(color="#35C33E"))
        curr_frame = go.Frame(
            data=[confirmed, deaths, recovered])
        frames.append(curr_frame)

    # print(curr_frame) -- Check Frames

    layout = go.Layout(title='US Daily Totals since Jan 22nd, 2020',
                       xaxis=dict(title="Date", range=[
                           daily_totals.iloc[1]['ObservationDate'],
                           max(daily_totals.iloc[:]['ObservationDate'])]),
                       yaxis=dict(title="Cases Count (Millions)", range=[
                           0, max(daily_totals.iloc[:]['Confirmed'])+1000]),
                       hovermode="x",
                       updatemenus=[dict(
                           type="buttons",
                           buttons=[dict(label="Play",
                                         method="animate",
                                         args=[None, dict(frame=dict(duration=100,
                                                                     redraw=False),
                                                          fromcurrent=True,
                                                          transition=dict(duration=100))]),
                                    dict(label="Stop",
                                         method="animate",
                                         args=[[None], dict(frame=dict(duration=0,
                                                                       redraw=False),
                                                            mode="immediate",
                                                            transition=dict(duration=0))])]
                       )]
                       )
    fig = go.Figure(data=[confirmed, deaths, recovered],
                    layout=layout, frames=frames)

    # fig.add_shape(
    #     # Line Vertical
    #     dict(
    #         type="line",
    #         x0=daily_totals["ObservationDate"][121],
    #         y0=0,
    #         x1=daily_totals["ObservationDate"][121],
    #         y1=max(daily_totals["Confirmed"]),
    #         line=dict(
    #             color="gray",
    #             width=3,
    #             dash="dot"
    #         )
    #     ))

    print('\n5: Plots generated in {} seconds'.format(time.time() - start_time))
