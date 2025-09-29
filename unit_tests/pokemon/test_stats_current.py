### tests for stats current attribute for pokemon class. 
import logging
from poke_env.battle import Battle, Move, Pokemon
from poke_env.battle.side_condition import SideCondition
from poke_env.stats import compute_raw_stats_dvs
from typing import List
from poke_env.teambuilder import Teambuilder
from poke_env.player import Player
attack_team = """
Venusaur  
Ability: No Ability  
- Stun Spore 
- Swords Dance
- Rest
- Growl

Jolteon  
Ability: No Ability  
- Thunder Wave 
- Agility
- Growl
- Rest  
"""
defense_team = """
Pikachu  
Ability: No Ability  
Level: 1    
- Seismic Toss  
- Quick Attack
- Thunder Wave

Magnemite  
Ability: No Ability  
- Thunder Wave  
"""

class Attack_Player(Player):
    def __init__(self, account_configuration = None, *, avatar = None, battle_format = "gen1ou", log_level = None, max_concurrent_battles = 1, accept_open_team_sheet = False, save_replays = False, server_configuration = ..., start_timer_on_battle_start = False, start_listening = True, open_timeout = 10, ping_interval = 20, ping_timeout = 20, team = attack_team):
        self.flag1 = False
        self.flag2 = False
        super().__init__(account_configuration, avatar=avatar, battle_format=battle_format, log_level=log_level, max_concurrent_battles=max_concurrent_battles, accept_open_team_sheet=accept_open_team_sheet, save_replays=save_replays, server_configuration=server_configuration, start_timer_on_battle_start=start_timer_on_battle_start, start_listening=start_listening, open_timeout=open_timeout, ping_interval=ping_interval, ping_timeout=ping_timeout, team=team)

    def choose_move(self, battle):
        return super().choose_move(battle)

# class TestTeamBuilder(Teambuilder):
#     def __init__(self,team_string):
#         self.team_string =  team_string
#         super().__init__()
#     def yield_team(self):
#         return self.team_string


def create_player_base(
    p1_team: List[Pokemon] = [Pokemon(1, species="jolteon"),Pokemon(1, species="venusaur")],
    p2_team:List[Pokemon] = [Pokemon(1, species="jolteon"),Pokemon(1, species="venusaur")]
) -> Battle:




    battle = Battle("tag", "test_battle", logging.Logger(""), gen=1)
    battle._format = f"gen1ou"
    battle.player_role = "p1"
  
    for mon in p1_team:
        if any(map(lambda x: x is None, mon.stats.values())):
            mon.stats = {
                k: v
                for k, v in zip(
                    ["hp", "atk", "def", "spa", "spd", "spe"],
                    compute_raw_stats_dvs(
                        mon.species,
                        [15] * 6,
                        mon.level,
                        mon._data,
                    ),
                )
            }
    for mon in p2_team:
        if any(map(lambda x: x is None, mon.stats.values())):
            mon.stats = {
                k: v
                for k, v in zip(
                    ["hp", "atk", "def", "spa", "spd", "spe"],
                    compute_raw_stats_dvs(
                        mon.species,
                        [15] * 6,
                        mon.level,
                        mon._data,
                    ),
                )
            }
    team_1 = {}
    for p in p1_team:
        team_1[f'p1: {p.name}'] = p
    team_2 = {}
    for p in p2_team:
        team_1[f'p2: {p.name}'] = p      
    battle._team = team_1
    battle._opponent_team = team_2

    for position, mon in zip(["p1", "p2"], [p1_team[0], p2_team[0]]):
        battle.switch(
            f"{position}: {mon.name}",
            f"{mon.species}, L{mon.level}",
            f"{mon.current_hp}/{mon.max_hp}",
        )
    return battle

# def test_base_cases_singles():

#     # gen 1
#     p1_team = [Pokemon(1, species="jolteon"),Pokemon(1, species="venusaur")]
#     p2_team = [Pokemon(1, species="jolteon"),Pokemon(1, species="venusaur")]
#     battle = create_battle(p1_team=p1_team, p2_team=p2_team)

    