import requests
import time
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, BarColumn
from rich import box
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.live import Live
from rich.console import Group
from rich.table import Table

def calculate_totals(response):
    total_revenue = 0
    total_bits = 0
    total_turbo = 0
    total_prime_subs = 0
    total_ads = 0
    for data in response:
        if 'data' in data and 'revenues' in data['data']:
            revenue_timeseries = data['data']['revenues']['revenueTimeSeries']
            for item in revenue_timeseries:
                total_revenue += item.get('total', 0)
                total_bits += item.get('bits', 0)
                total_turbo += item.get('turbo', 0)
                total_prime_subs += item.get('primeSubscriptions', 0)
                total_ads += item.get('ads', 0)

    return {
        'Total Revenue': total_revenue,
        'Total Bits': total_bits,
        'Total Turbo': total_turbo,
        'Total Prime Subscriptions': total_prime_subs,
        'Total Ads': total_ads
    }

def fetch_data(oauth_token, channel_id):
    url = "https://gql.twitch.tv/gql"
    headers = {
        "Authorization": f"OAuth {oauth_token}"
    }
    data = [
        {
            "operationName": "Channel_Analytics_Revenue",
            "variables": {
                "startAt": "2021-01-01T00:00:00.000Z",
                "endAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "timeZone": "UTC",
                "granularity": "DAY",
                "channelID": channel_id
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "bcf988e9ee3597a7683cc7f682a4b78e76f0b9bf07e921de1a46e8838c410eab"
                }
            }
        },
    ]

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return calculate_totals(response.json())
    else:
        return f"Failed with status code: {response.status_code}"


def format_result(result):
    return {key: f"${value / 100:.2f}" if isinstance(value, int) else value for key, value in result.items()}

def display_results(identifier, formatted_result):
    table = Table(box=box.ROUNDED)
    table.add_column(f"{identifier}", style="cyan", no_wrap=True)
    table.add_column("Amount", style="magenta")
    for key, value in formatted_result.items():
        table.add_row(key, value)
    spacer = Text("\n")
    total_revenue = float(formatted_result['Total Revenue'][1:])
    target_revenue = 50.0
    percentage = (total_revenue / target_revenue) * 100 
    progress = Progress("[progress.description]{task.description}", BarColumn(bar_width=24), "[progress.percentage]{task.percentage:>3.0f}%", expand=False)
    progress.add_task("Payout:", total=100, completed=min(percentage, 100))
    return Group(table, progress, spacer)

def main():
    console = Console()
    with Live(console=console, refresh_per_second=0.2, transient=True) as live:
        while True:
            groups = []
            with open("oauth_tokens.txt", "r") as file:
                lines = file.readlines()
            for line in lines:
                oauth_token, channel_id, identifier = line.strip().split()
                if oauth_token == "oauth_token_here":
                    continue
                result = fetch_data(oauth_token, channel_id)
                formatted_result = format_result(result)
                group = display_results(identifier, formatted_result)
                groups.append(group)
            columns = Columns(groups, expand=True)
            console.clear()
            live.update(columns)
            current_time = datetime.now().strftime("%I:%M %p")
            console.print(f"\nLast Updated: {current_time}\n\n")
            time.sleep(240)

if __name__ == "__main__":
    main()