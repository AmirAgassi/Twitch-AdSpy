# Twitch AdSpy

Twitch AdSpy is an advanced analytics tool designed to monitor and display live revenue statistics for bulk Twitch affiliate accounts simultaneously. Leveraging the power of real-time data aggregation, AdSpy offers unparalleled insights into revenue streams from Twitch channels.

## Key Features

- **Bulk Affiliate Account Monitoring:** Seamlessly tracks multiple Twitch affiliate accounts, providing comprehensive analytics in one unified dashboard.
- **Real-Time Revenue Tracking:** Monitors and updates revenue data in real time, including bits, ads, turbo, and prime subscriptions.
- **Advanced Data Analytics:** Utilizes sophisticated algorithms to calculate total revenue and other key performance indicators (KPIs) for each tracked account.
- **Rich Visual Display:** Integrates Rich library for Python to render elegant and intuitive tables and progress bars, enhancing the user experience with clear and digestible data presentation.
- **Automated Data Fetching:** Automatically retrieves up-to-date statistics using Twitch's GraphQL API, ensuring timely and accurate information.
- **Customizable Data Granularity:** Offers flexibility in data granularity, ranging from daily to monthly statistics, tailored to the user's preferences.
- **OAuth Token Support:** Securely connects to Twitch accounts using OAuth tokens, ensuring data privacy and security.
- **Live Dashboard:** Features a dynamic live dashboard that refreshes periodically, providing a snapshot of the latest revenue statistics.
- **Payout Tracking:** Includes a progress bar to visually track and compare actual revenue against predefined targets.

## Disclaimer

Twitch AdSpy is not affiliated with or endorsed by Twitch. It is intended for analytical purposes only and should be used in accordance with Twitch's terms of service.

## Installation

1. Clone the repository.
2. Install required Python packages: `requests`, `rich`.
3. Add your OAuth tokens, channel IDs, and channel names to `oauth_tokens.txt`.
4. Run the script: `python twitch_adspy.py`.

## Example Dashboard

- Channel Analytics Overview with real-time updates.
- Revenue breakdown for each channel including Bits, Ads, Turbo, and Prime Subscriptions.
- Progress towards revenue targets visualized in an intuitive progress bar.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.
