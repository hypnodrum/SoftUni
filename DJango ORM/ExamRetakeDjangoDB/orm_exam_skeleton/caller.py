import os
import django
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match


def get_tennis_players(search_name=None, search_country=None):
    if search_name is not None and search_country is not None:
        players = TennisPlayer.objects.filter(
            full_name__icontains=search_name,
            country__icontains=search_country
        )

    elif search_name is not None:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name)

    elif search_country is not None:
        players = TennisPlayer.objects.filter(country__icontains=search_country)

    else:
        return ""

    if players.exists():
        players = players.order_by('ranking')
        result = "\n".join([
            f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}"
            for player in players
        ])
        return result

    return ""


def get_top_tennis_player():
    players_with_wins = TennisPlayer.objects.annotate(
        num_of_wins=models.Count('matches_won')
    ).order_by('-num_of_wins', 'full_name')

    if players_with_wins.exists():
        top_player = players_with_wins.first()
        return f"Top Tennis Player: {top_player.full_name} with {top_player.num_of_wins} wins."

    return ""


def get_tennis_player_by_matches_count():
    most_exp_player = TennisPlayer.objects.annotate(
        num_of_matches=models.Count('matches_played')
    ).order_by('-num_of_matches', 'ranking').first()

    if most_exp_player is not None and most_exp_player.num_of_matches > 0:
        return f"Tennis Player: {most_exp_player.full_name} with {most_exp_player.num_of_matches} matches played."

    return ""


def get_tournaments_by_surface_type(surface=None):
    if surface is not None:
        tournaments = Tournament.objects.filter(surface_type__icontains=surface).order_by('-start_date')

        if tournaments.exists():
            result = "\n".join([
                f"Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {tournament.matches.count()}"
                for tournament in tournaments
            ])
            return result

    return ""


def get_latest_match_info():
    latest_match = Match.objects.order_by('-date_played', '-id').first()

    if latest_match is not None:
        player1_full_name = latest_match.players.all()[0].full_name
        player2_full_name = latest_match.players.all()[1].full_name
        winner_full_name = latest_match.winner.full_name if latest_match.winner is not None else "TBA"

        return f"Latest match played on: {latest_match.date_played}, " \
               f"tournament: {latest_match.tournament.name}, " \
               f"score: {latest_match.score}, " \
               f"players: {player1_full_name} vs {player2_full_name}, " \
               f"winner: {winner_full_name}, " \
               f"summary: {latest_match.summary}"

    return ""


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is not None:
        try:
            tournament = Tournament.objects.get(name=tournament_name)
            matches = Match.objects.filter(tournament=tournament).order_by('-date_played')

            if matches.exists():
                result = "\n".join([
                    f"Match played on: {match.date_played}, score: {match.score}, winner: {'TBA' if match.winner is None else match.winner.full_name}"
                    for match in matches
                ])
                return result

            return "No matches found."

        except Tournament.DoesNotExist:
            return "No matches found."

    return "No matches found."

