import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
from backend.stats_classes import Game, Event, EventType, LineType, Player
import string

def get_team_data(file:str) -> tuple[pd.DataFrame, list[list[str,str,str]]]:
    csv = pd.read_csv(file)
    csv.rename(columns={"Tournamemnt":"Tournament"}, inplace=True)
    unique = csv.groupby(['Date/Time','Tournament', 'Opponent'])[['Date/Time','Tournament', 'Opponent']].apply(lambda x: list(np.unique(x)))
    csv['Date/Time']= pd.to_datetime(csv['Date/Time'])

    return csv, unique.values.tolist()

def get_game_data(csv, tournament: str, opponent: str, game_date: datetime, video_offset_s:int) -> pd.DataFrame:
    game_data = csv[
        (csv["Tournament"] == tournament)
        & (csv["Opponent"] == opponent)
        & (
            (csv["Date/Time"] >= game_date)
            & (csv["Date/Time"] <= (game_date + timedelta(hours = 24)))
        )
    ].copy()
    game_data["Elapsed Time (secs)"] = game_data["Elapsed Time (secs)"] + video_offset_s
    return game_data

# get data objects from data
def get_game_objects(game_data: pd.DataFrame) -> Game:

    # getting data to use for creating game object
    first_row = game_data.iloc[0]
    last_row = game_data.iloc[-1]

    opponent = first_row["Opponent"]
    tournament = first_row["Tournament"]
    datetime_of_game = first_row["Date/Time"]
    starting_line_type = LineType[first_row["Line"]]
    their_final_score = last_row["Their Score - End of Point"]
    our_final_score = last_row["Our Score - End of Point"]
    elapsed_time_of_first_pull = int(first_row["Elapsed Time (secs)"])
    game_duration_s = int(last_row["Elapsed Time (secs)"]) - elapsed_time_of_first_pull

    active_players = set()
    events = []

    previous_event_start = int(first_row["Elapsed Time (secs)"])

    # looping through each event
    for index, row in game_data.iterrows():
        event_type = EventType[
            row["Action"]
            .translate(str.maketrans("", "", string.punctuation))
            .upper()
        ]
        line_type = LineType[row["Line"]]
        players_on = []
        for x in range(28):
            if pd.notnull(row[f"Player {x}"]):
                players_on.append(Player(row[f"Player {x}"]))
        active_players.update(players_on)
        event_start_elapsed = int(row["Elapsed Time (secs)"])
        event_start_datetime = datetime_of_game + timedelta(seconds=event_start_elapsed)
        passer = row["Passer"] if pd.notnull(row["Passer"]) else None
        reciever = row["Receiver"] if pd.notnull(row["Receiver"]) else None
        defender = row["Defender"] if pd.notnull(row["Defender"]) else None
        hang_time = float(row["Hang Time (secs)"]) if pd.notnull(row["Hang Time (secs)"]) else None

        events.append(
            Event(
                event_type=event_type,
                opponent=opponent,
                tournament=tournament,
                datetime_game=datetime_of_game,
                event_start_datetime=event_start_datetime,
                event_start_elapsed=event_start_elapsed,
                players_on=players_on,
                line_type=line_type,
                our_score=row["Our Score - End of Point"],
                their_score=row["Their Score - End of Point"],
                passer=passer,
                reciever=reciever,
                defender=defender,
                hang_time=hang_time,
            )
        )

    return Game(
        opponent=opponent, 
        tournament = tournament,
        active_players = list(active_players),
        datetime_of_first_pull = datetime_of_game,
        elapsed_time_of_first_pull = elapsed_time_of_first_pull, 
        starting_line_type = starting_line_type,
        our_final_score = our_final_score, 
        their_final_score = their_final_score, 
        duration_s = game_duration_s,
        events = events
    )

def get_point_clips(file, game_date, tournament, opponent, video_offset):
    csv, unique_games = get_team_data(file)
    game_data = get_game_data(csv, tournament, opponent, game_date, video_offset)
    game_object = get_game_objects(game_data)

    clips = []
    point_start_event = game_object.events[0]
    update_point_start_event = False
    for event in game_object.events:
        if update_point_start_event:
            point_start_event = event
            update_point_start_event = False
        if event.event_type == EventType.GOAL:
            clips.append({
                'timestamp': point_start_event.event_start_elapsed + video_offset,
                'duration': event.event_start_elapsed - point_start_event.event_start_elapsed,
                'tags': {
                    'side': {LineType.O: 'Offense', LineType.D: 'Defense'}[event.line_type],
                    'opponent': opponent,
                    'tournament': tournament,
                    'date': game_date.date(),
                },
            })
            update_point_start_event = True
    return clips
