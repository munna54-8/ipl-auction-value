# IPL 2026: Are Players Worth What They're Paid?

## Problem
Using real career performance data, which IPL players deliver the most value relative to their auction/retention price — and which are the biggest overpays?

## Data source & collection method
Career IPL statistics for 37 players collected via CricAPI.com (free tier), cross-referenced with real 2026 IPL auction/retention prices compiled from public sports-media reporting. 3 players were excluded due to missing/zero stats data, and 15 more due to conflicting price figures across sources — leaving 19 players with high-confidence data on both sides.

## Approach
- Python + CricAPI to pull career IPL batting/bowling stats, with deduplication logic for conflicting stat blocks found in the raw API response
- Manually compiled and cross-checked auction/retention price table — excluded rather than guessed at any player with conflicting reported prices
- Built an "impact score" (runs + wickets × 20, a standard rough T20 equivalence) and divided by price to rank value-per-crore

## Key findings
- **MS Dhoni delivers the best value by a wide margin**: retained for just ₹4 crore, his 1,360 value-points-per-crore is 3.3x the #2 player
- **Rishabh Pant, the most expensive player in IPL auction history (₹27Cr), ranks 16th of 19** on value — a real gap between market price and statistical output
- Bowlers and all-rounders (Boult, Chahal, Jadeja, Narine) cluster near the top of the value ranking — wicket-taking talent is comparatively cheap relative to marquee batting

## Methodology honesty
The impact-score formula favors bowlers somewhat (a wicket is weighted heavily). Auction price data came from public reporting rather than an official structured source, since no clean API exists for this — players with contradictory reported prices were excluded rather than resolved by guessing.

## Tools
Python, Pandas, CricAPI, Chart.js

## Dashboard
https://munna54-8.github.io/ipl-auction-value/dashboard/ipl_value_dashboard.html